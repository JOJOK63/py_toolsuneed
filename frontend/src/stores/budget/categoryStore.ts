import { defineStore } from 'pinia'
import { ref } from 'vue'
import {
  type Category,
  fetchCategoryApi,
  type CategoryCreate,
} from '@/api/modules/budget/category.ts'
import axios from 'axios'

// defineStore('category', ...) → 'category' nom unique
// identifier ce store dans l'app. 1 par application :
// 'category', 'toolbox', 'currency'...
export const useCategoryStore = defineStore('categoryStore', () => {
  const categories = ref<Category[]>([])
  const loading = ref<boolean>(false) // attend on une réponse de l'api
  const error = ref<string | null>(null) // ERREUR  ou pas ?

  async function fetchAll() {
    loading.value = true
    error.value = null
    try {
      const response = await fetchCategoryApi.getAll()
      categories.value = response.data
    } catch (e) {
      error.value = 'Impossible de charger les catégories.'
    } finally {
      loading.value = false // désactive le loader quoi qu'il arrive
    }
  }

  async function create(data: CategoryCreate) {
    try {
      const response = await fetchCategoryApi.create(data)
      categories.value.push(response.data)
    } catch (e) {
      // axios met la réponse Django dans e.response.data
      if (axios.isAxiosError(e) && e.response?.data) {
        // Django renvoie un objet d'erreurs par champ
        // ex: { color: ["category with this color already exists."] }
        const djangoErrors = e.response.data
        // On transforme l'objet en string lisible
        error.value = Object.entries(djangoErrors)
          .map(([field, messages]) => `${field} : ${(messages as string[]).join(', ')}`)
          .join(' | ')
      } else {
        error.value = `Impossible de créer la catégorie.`
      }
    }
  }

  // Partial<> de mettre tous les attributs en optionnel et donc de faire un put ou un patch sans soucis
  async function update(id: number, data: Partial<CategoryCreate>) {
    try {
      const response = await fetchCategoryApi.update(id, data)

      const index = categories.value.findIndex((category) => category.id === id)
      if (index !== -1) {
        categories.value[index] = response.data
      }
    } catch (e) {
      error.value = 'Impossible de modifier la catégorie'
    }
  }

  async function remove(id: number) {
    try {
      await fetchCategoryApi.delete(id)
      //retourne un nouvea tableau sans l'lément supprimé
      categories.value = categories.value.filter((category) => category.id !== id)
    } catch (e) {
      error.value = 'Impossible de supprimer la catégorie'
    }
  }

  function clearError() {
    error.value = null
  }

  // Ce qu'on expose aux composants Vue
  // Tout ce qui n'est pas ici est "privé" au store
  return { categories, loading, error, fetchAll, create, update, remove, clearError }
})

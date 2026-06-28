import { defineStore } from 'pinia'
import { ref } from 'vue'
import axios from 'axios'
import {
  fetchSubcategoryApi,
  type Subcategory,
  type SubcategoryCreate,
} from '@/api/modules/budget/subcategory.ts'

export const useSubcategoryStore = defineStore('subcategoryStore', () => {
  const subcategories = ref<Subcategory[]>([])
  const loading = ref<boolean>(false)
  const error = ref<string | null>(null)
  const isFilterActive = ref(false)

  async function fetchAll() {
    loading.value = true
    error.value = null
    try {
      const response = await fetchSubcategoryApi.getAll()
      subcategories.value = response.data
    } catch (e) {
      console.log(e)
      error.value = 'Impossible de charger les sous catégories'
    } finally {
      loading.value = false
    }
  }

  async function create(data: SubcategoryCreate) {
    try {
      const response = await fetchSubcategoryApi.create(data)
      subcategories.value.push(response.data)
    } catch (e) {
      if (axios.isAxiosError(e) && e.response?.data) {
        const djangoErrors = e.response.data
        error.value = Object.entries(djangoErrors)
          .map(([field, messages]) => `${field} : ${(messages as string[]).join(', ')}`)
          .join(' | ')
      } else {
        error.value = `Impossible de créer la sous catégorie.`
      }
    }
  }

  async function update(id: number, data: Partial<SubcategoryCreate>) {
    try {
      const response = await fetchSubcategoryApi.update(id, data)

      const index = subcategories.value.findIndex((subcategory) => subcategory.id === id)
      if (index !== -1) {
        subcategories.value[index] = response.data
      }
    } catch (e) {
      error.value = 'Impossible de modifier la sous catégorie'
    }
  }

  async function remove(id: number) {
    try {
      await fetchSubcategoryApi.delete(id)
      subcategories.value = subcategories.value.filter((subcategory) => subcategory.id !== id)
    } catch (e) {
      error.value = ' Impossible de supprimer la sous catégorie'
    }
  }

  function clearError() {
    error.value = null
  }

  return { subcategories, loading, error, fetchAll, create, update, remove, clearError }
})

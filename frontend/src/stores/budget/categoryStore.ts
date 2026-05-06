import { defineStore } from 'pinia'
import { ref } from 'vue'
import { categoryApi, type Category } from '@/api/modules/budget'

export const useCategoryStore = defineStore('category', () => {
  const categories = ref<Category[]>([])
  const loading = ref(false)

  async function fetchAll() {
    loading.value = true
    const { data } = await categoryApi.getAll()
    categories.value = data
    loading.value = false
  }

  async function create(payload: Omit<Category, 'id'>) {
    const { data } = await categoryApi.create(payload)
    categories.value.push(data)
  }

  async function remove(id: number) {
    await categoryApi.delete(id)
    categories.value = categories.value.filter((c) => c.id !== id)
  }

  return { categories, loading, fetchAll, create, remove }
})

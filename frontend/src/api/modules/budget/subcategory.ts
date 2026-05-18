import type { Category } from './category.ts'
import api from '@/api'

export interface Subcategory {
  id: number
  name: string
  icon: string
  category: number
  category_detail: Category
}

export type SubcategoryCreate = {
  name: string
  icon: File | null
  category: number
}

export const fetchSubcategoryApi = {
  getAll() {
    return api.get<Subcategory[]>('/budget/subcategory/')
  },

  getById(id: number) {
    return api.get<Subcategory>(`/budget/subcategory/${id}/`)
  },

  create(data: SubcategoryCreate) {
    const formData = new FormData()
    formData.append('name', data.name)
    formData.append('category', String(data.category))

    if (data.icon) {
      formData.append('icon', data.icon)
    }
    return api.post<Subcategory>('/budget/subcategory/', formData)
  },

  update(id: number, data: Partial<SubcategoryCreate>) {
    const formData = new FormData()
    if (data.name) formData.append('name', data.name)
    if (data.icon) formData.append('icon', data.icon)
    if (data.category) formData.append('category', String(data.category))
    return api.patch<Subcategory>(`budget/subcategory/${id}/`, formData)
  },

  delete(id: number) {
    return api.delete(`budget/subcategory/${id}/`)
  },
}

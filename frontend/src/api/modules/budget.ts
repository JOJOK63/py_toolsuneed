import api from '../index'


export interface Category {
  id: number
  name: string
  color: string
  // icon: url | string
  is_active: boolean
  // tes autres champs
}

export const categoryApi = {
  getAll: () => api.get<Category[]>('/budget/category/'),
  getOne: (id: number) => api.get<Category>(`/budget/category/${id}/`),
  create: (data: Omit<Category, 'id'>) => api.post<Category>('/budget/category/', data),
  update: (id: number, data: Partial<Category>) =>
    api.put<Category>(`/budget/category/${id}/`, data),
  delete: (id: number) => api.delete(`/budget/category/${id}/`),
}

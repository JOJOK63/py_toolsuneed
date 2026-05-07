import api from '../index'

export interface Category{
  id:number
  name:string
  color:string
  icon:string
  is_active:boolean
}

// Omit<Category, 'id' | 'is_active'> = "Category mais sans id et sans is_active" pour la creation
// Pour créer/modifier : icon est un vrai fichier ou null
export type CategoryCreate = {
  name: string
  color: string
  icon: File | null
  is_active?: boolean
}

export const categoryApi = {
  getAll() {
    return api.get<Category[]>('/budget/category/')
  },

  getById(id: number) {
    return api.get<Category>(`/budget/category/${id}/`)
  },

  create(data: CategoryCreate) {
    // On construit un FormData à la place d'envoyer du JSON
    const formData = new FormData()
    formData.append('name', data.name)
    formData.append('color', data.color)
    formData.append('is_active', String(data.is_active ?? true))
    // On n'ajoute icon QUE si l'utilisateur a choisi un fichier
    if (data.icon) {
      formData.append('icon', data.icon)
    }
    return api.post<Category>('/budget/category/', formData)
  },

  // PUT /budget/category/1/ → remplacement complet
  update(id: number, data: Partial<CategoryCreate>) {
    const formData = new FormData()
    if (data.name) formData.append('name', data.name)
    if (data.color) formData.append('color', data.color)
    if (data.icon) formData.append('icon', data.icon)
    if (data.is_active !== undefined) formData.append('is_active', String(data.is_active))
    return api.patch<Category>(`/budget/category/${id}/`, formData)
  },

  delete(id: number) {
    return api.delete(`/budget/category/${id}/`)
  },
}

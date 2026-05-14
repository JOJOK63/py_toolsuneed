import type { Category } from './category.ts'

export interface Subcategory {
  id: number
  name: string
  icon: string
  category: number
  category_detail: Category
}

// export type SubcategoryCreate = {
//   name: string
//   icon: File | null
//   category: number
// }

import type { RouteRecordRaw } from 'vue-router'

const budgetRoutes: RouteRecordRaw[] = [
  {
    path: '/budget',
    component: () => import('@/views/budget/BudgetView.vue'),
    children: [
      {
        path: 'categories', // → /budget/categories
        name: 'Categories',
        component: () => import('@/views/budget/Category/CategoryView.vue'),
      },
      {
        path: 'subcategories', // → /budget/subcategories
        name: 'Subcategories',
        component: () => import('@/views/budget/Subcategory/SubcategoryView.vue'),
      },
    ],
  },
]

export default budgetRoutes

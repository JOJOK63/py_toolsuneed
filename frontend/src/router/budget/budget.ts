import type { RouteRecordRaw } from 'vue-router'

const budgetRoutes: RouteRecordRaw[] = [
  {
    path: '/budget',
    component: () => import('@/views/budget/BudgetView.vue'),
    meta: { requiresAuth: true },
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
      {
        path: 'transactions', // → /budget/subcategories
        name: 'Transactions',
        component: () => import('@/views/budget/Transaction/TransactionView.vue'),
      },
    ],
  },
]

export default budgetRoutes

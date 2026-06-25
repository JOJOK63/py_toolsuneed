import type { RouteRecordRaw } from 'vue-router'

const todolistRoutes: RouteRecordRaw[] = [
  {
    path: '/todolist',
    component: () => import('@/views/todolist/TodolistView.vue'),
    meta: { requiresAuth: true },
    children: [
      // {
      //   path: 'todolists', // → /budget/categories
      //   name: 'Todolists',
      //   component: () => import('@/views/todolist/Todo/TodoView.vue'),
      // },
      // {
      //   path: 'subcategories', // → /budget/subcategories
      //   name: 'Subcategories',
      //   component: () => import('@/views/budget/Subcategory/SubcategoryView.vue'),
      // },
    ],
  },
]

export default todolistRoutes

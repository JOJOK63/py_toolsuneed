import { createRouter, createWebHistory } from 'vue-router'
import budgetRoutes from './budget/budget.ts'
import todolistRoutes from './todolist/todolist.ts'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'Home', component: () => import('@/views/HomeView.vue') },
    { path: '/test', name: 'Test', component: () => import('@/views/TestView.vue') },
    ...todolistRoutes,
    ...budgetRoutes,
  ],
})

export default router

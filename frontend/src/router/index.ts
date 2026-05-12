import { createRouter, createWebHistory } from 'vue-router'
import budgetRoutes from './budget/budget.ts'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'Home', component: () => import('@/views/HomeView.vue') },
    ...budgetRoutes,
  ],
})

export default router

import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'Home', component: () => import('@/views/HomeView.vue') },
    { path: '/budget', name: 'Budget', component: () => import('@/views/budget/BudgetView.vue') },
    // demain : { path: '/toolbox', ... }
  ],
})

export default router

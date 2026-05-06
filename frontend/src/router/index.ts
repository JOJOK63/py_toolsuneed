import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import BudgetListView from '@/views/budget/BudgetListView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'Home', component: () => import('@/views/HomeView.vue') },
    { path: '/budget', name: 'Budget', component: () => import('@/views/budget/CategoryListView.vue') },
    // demain : { path: '/toolbox', ... }
  ],
})

export default router

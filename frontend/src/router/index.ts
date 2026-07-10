import { createRouter, createWebHistory } from 'vue-router'
import budgetRoutes from './budget/budget.ts'
import todolistRoutes from './todolist/todolist.ts'
import authRoutes from './auth/auth.ts'
import { useAuthStore } from '@/stores/auth'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: () => import('@/views/HomeView.vue'),
      meta: { requiresAuth: true },
    },
    { path: '/test', name: 'Test', component: () => import('@/views/TestView.vue') },
    { path: '/login', name: 'Login', component: () => import('@/views/auth/LoginView.vue') },
    ...authRoutes,
    ...todolistRoutes,
    ...budgetRoutes,
  ],
})

router.beforeEach((to, from, next) => {
  const authStore = useAuthStore()

  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    next({ name: 'Login' })
  } else if (to.name === 'Login' && authStore.isAuthenticated) {
    next({ name: 'Home' })
  } else {
    next()
  }
})

export default router

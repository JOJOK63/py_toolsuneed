// stores/auth.ts
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { authApi, type LoginCredentials } from '@/api/modules/auth/auth.ts'
import axios from 'axios'

export const useAuthStore = defineStore('authStore', () => {
  const access = ref<string | null>(localStorage.getItem('access'))
  const refresh = ref<string | null>(localStorage.getItem('refresh'))
  const loading = ref(false)
  const error = ref<string | null>(null)

  const isAuthenticated = computed(() => !!access.value)

  async function login(credentials: LoginCredentials) {
    loading.value = true
    error.value = null
    try {
      const response = await authApi.login(credentials)
      access.value = response.data.access
      refresh.value = response.data.refresh
      localStorage.setItem('access', access.value)
      localStorage.setItem('refresh', refresh.value)
      return true
    } catch (e) {
      if (axios.isAxiosError(e) && e.response?.data) {
        error.value = e.response.data.error ?? 'Identifiants invalides.'
      } else {
        error.value = 'Impossible de se connecter.'
      }
      return false
    } finally {
      loading.value = false
    }
  }

  function logout() {
    access.value = null
    refresh.value = null
    localStorage.removeItem('access')
    localStorage.removeItem('refresh')
  }

  function clearError() {
    error.value = null
  }

  return { access, refresh, loading, error, isAuthenticated, login, logout, clearError }
})

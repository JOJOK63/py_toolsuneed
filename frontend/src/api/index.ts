import axios from 'axios'
import camelcaseKeys from 'camelcase-keys'
import snakecaseKeys from 'snakecase-keys'

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
})

// --- INTERCEPTOR DE REQUÊTE : injecte le token + convertit camelCase -> snake_case ---
api.interceptors.request.use((config) => {
  const access = localStorage.getItem('access')
  if (access) {
    config.headers.Authorization = `Bearer ${access}`
  }

  // On ne convertit que les payloads JSON classiques (pas FormData, pas les uploads d'images)
  if (config.data && !(config.data instanceof FormData)) {
    config.data = snakecaseKeys(config.data, { deep: true })
  }

  return config
})

// --- INTERCEPTOR DE RÉPONSE : convertit snake_case -> camelCase + gère le refresh automatique sur 401 ---
let isRefreshing = false
let refreshSubscribers: ((token: string) => void)[] = []

function onRefreshed(token: string) {
  refreshSubscribers.forEach((cb) => cb(token))
  refreshSubscribers = []
}

api.interceptors.response.use(
  (response) => {
    if (response.data) {
      response.data = camelcaseKeys(response.data, { deep: true })
    }
    return response
  },
  async (error) => {
    const originalRequest = error.config

    if (error.response?.status !== 401 || originalRequest._retry) {
      return Promise.reject(error)
    }

    const refreshToken = localStorage.getItem('refresh')
    if (!refreshToken) {
      localStorage.removeItem('access')
      localStorage.removeItem('refresh')
      window.location.href = '/login'
      return Promise.reject(error)
    }

    originalRequest._retry = true

    if (isRefreshing) {
      return new Promise((resolve) => {
        refreshSubscribers.push((token: string) => {
          originalRequest.headers.Authorization = `Bearer ${token}`
          resolve(api(originalRequest))
        })
      })
    }

    isRefreshing = true
    try {
      const { data } = await axios.post(`${import.meta.env.VITE_API_URL}/token/refresh/`, {
        refresh: refreshToken,
      })
      localStorage.setItem('access', data.access)
      isRefreshing = false
      onRefreshed(data.access)

      originalRequest.headers.Authorization = `Bearer ${data.access}`
      return api(originalRequest)
    } catch (refreshError) {
      isRefreshing = false
      localStorage.removeItem('access')
      localStorage.removeItem('refresh')
      window.location.href = '/login'
      return Promise.reject(refreshError)
    }
  },
)

export default api

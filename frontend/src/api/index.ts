import axios from 'axios'

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
})

// --- INTERCEPTOR DE REQUÊTE : injecte le token à chaque appel ---
api.interceptors.request.use((config) => {
  const access = localStorage.getItem('access')
  if (access) {
    config.headers.Authorization = `Bearer ${access}`
  }
  return config
})

// --- INTERCEPTOR DE RÉPONSE : gère le refresh automatique sur 401 ---
let isRefreshing = false
let refreshSubscribers: ((token: string) => void)[] = []

function onRefreshed(token: string) {
  refreshSubscribers.forEach((cb) => cb(token))
  refreshSubscribers = []
}

api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config

    // Si pas 401, ou si on a déjà tenté un refresh pour cette requête → on laisse planter
    if (error.response?.status !== 401 || originalRequest._retry) {
      return Promise.reject(error)
    }

    const refreshToken = localStorage.getItem('refresh')
    if (!refreshToken) {
      // pas de refresh dispo → déconnexion forcée
      localStorage.removeItem('access')
      localStorage.removeItem('refresh')
      window.location.href = '/login'
      return Promise.reject(error)
    }

    originalRequest._retry = true

    if (isRefreshing) {
      // une requête refresh est déjà en cours : on attend qu'elle finisse
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

// api/modules/auth/auth.ts
import api from '../../index.ts'

export interface LoginCredentials {
  username: string
  password: string
}

export interface TokenPair {
  access: string
  refresh: string
}

export const authApi = {
  login(credentials: LoginCredentials) {
    return api.post<TokenPair>('/login/', credentials)
  },

  refresh(refreshToken: string) {
    return api.post<{ access: string }>('/token/refresh/', { refresh: refreshToken })
  },
}

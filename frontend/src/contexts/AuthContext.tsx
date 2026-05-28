import { createContext, useContext, useEffect, useMemo, useState } from 'react'
import type { ReactNode } from 'react'
import { authApi } from '../services/api'
import type { User } from '../types/api'

interface AuthContextValue {
  user: User | null
  isAuthenticated: boolean
  isAdmin: boolean
  login: (email: string, password: string) => Promise<void>
  register: (username: string, email: string, password: string) => Promise<void>
  logout: () => void
}

const AuthContext = createContext<AuthContextValue | undefined>(undefined)

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User | null>(() => {
    const stored = localStorage.getItem('user')
    return stored ? (JSON.parse(stored) as User) : null
  })

  useEffect(() => {
    if (!localStorage.getItem('token')) return
    authApi.me().then(setUser).catch(() => setUser(null))
  }, [])

  const value = useMemo<AuthContextValue>(
    () => ({
      user,
      isAuthenticated: Boolean(user),
      isAdmin: user?.role === 'admin',
      login: async (email, password) => {
        const result = await authApi.login(email, password)
        localStorage.setItem('token', result.access_token)
        localStorage.setItem('user', JSON.stringify(result.user))
        setUser(result.user)
      },
      register: async (username, email, password) => {
        const result = await authApi.register(username, email, password)
        localStorage.setItem('token', result.access_token)
        localStorage.setItem('user', JSON.stringify(result.user))
        setUser(result.user)
      },
      logout: () => {
        localStorage.removeItem('token')
        localStorage.removeItem('user')
        setUser(null)
      },
    }),
    [user],
  )

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>
}

export function useAuth() {
  const value = useContext(AuthContext)
  if (!value) throw new Error('useAuth must be used within AuthProvider')
  return value
}

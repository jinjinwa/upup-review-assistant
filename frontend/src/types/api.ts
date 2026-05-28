export interface ApiResponse<T> {
  code: number
  success: boolean
  message: string
  data: T
}

export interface User {
  id: number
  username: string
  email: string
  role: 'admin' | 'user'
  is_active: boolean
}

export interface AuthResult {
  access_token: string
  token_type: string
  user: User
}

export interface DemoReport {
  id: number
  title: string
  score: number
  summary: string
  created_at: string
}

export interface DataSource {
  id: number
  name: string
  kind: string
  status: string
  is_enabled: boolean
  last_sync_at: string | null
}

export interface IntegrationTask {
  id: number
  data_source_id: number
  status: string
  message: string
  created_at: string
  finished_at: string | null
}

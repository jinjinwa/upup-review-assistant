import type { ApiResponse, AuthResult, DataSource, DemoReport, IntegrationTask, User } from '../types/api'

const API_BASE = import.meta.env.VITE_API_BASE_URL || '/api'

export class ApiError extends Error {
  code: number

  constructor(message: string, code: number) {
    super(message)
    this.code = code
  }
}

function token() {
  return localStorage.getItem('token')
}

async function request<T>(path: string, options: RequestInit = {}): Promise<T> {
  const headers = new Headers(options.headers)
  headers.set('Content-Type', 'application/json')
  const accessToken = token()
  if (accessToken) {
    headers.set('Authorization', `Bearer ${accessToken}`)
  }

  const response = await fetch(`${API_BASE}${path}`, { ...options, headers })
  const payload = (await response.json()) as ApiResponse<T>
  if (!response.ok || !payload.success) {
    if (response.status === 401) {
      localStorage.removeItem('token')
      localStorage.removeItem('user')
    }
    throw new ApiError(payload.message || 'Request failed', payload.code || response.status)
  }
  return payload.data
}

export const authApi = {
  login: (email: string, password: string) =>
    request<AuthResult>('/auth/login', {
      method: 'POST',
      body: JSON.stringify({ email, password }),
    }),
  register: (username: string, email: string, password: string) =>
    request<AuthResult>('/auth/register', {
      method: 'POST',
      body: JSON.stringify({ username, email, password }),
    }),
  me: () => request<User>('/auth/me'),
}

export const demoApi = {
  overview: () => request<{ welcome: string; role: string; modules: string[]; notice: string }>('/demo/overview'),
  createReview: () => request<DemoReport>('/demo/reviews', { method: 'POST' }),
  reports: () => request<{ items: DemoReport[] }>('/demo/reports'),
}

export const scoringApi = {
  evaluate: () =>
    request<{ title: string; score: number; band: string; summary: string }>('/scoring/evaluate', {
      method: 'POST',
      body: JSON.stringify({
        title: '社区版通用评分器',
        dimensions: [
          { name: 'data_completeness', value: 78, weight: 0.35 },
          { name: 'workflow_readiness', value: 84, weight: 0.4 },
          { name: 'demo_volatility', value: 62, weight: 0.25 },
        ],
      }),
    }),
}

export const adminApi = {
  users: () =>
    request<{
      items: Array<User & { report_count: number }>
      implementation_note: string
    }>('/admin/users'),
  dataSources: () => request<{ items: DataSource[] }>('/admin/data-sources'),
  syncDataSource: (id: number) =>
    request<{ task_id: number; status: string }>(`/admin/data-sources/${id}/sync`, { method: 'POST' }),
  tasks: () => request<{ items: IntegrationTask[] }>('/admin/tasks'),
}

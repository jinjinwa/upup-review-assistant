import type { ReactNode } from 'react'
import { Navigate, Route, Routes } from 'react-router-dom'
import MainLayout from './components/MainLayout'
import { useAuth } from './contexts/AuthContext'
import AdminDataGovernance from './pages/AdminDataGovernance'
import AdminUsers from './pages/AdminUsers'
import Dashboard from './pages/Dashboard'
import Login from './pages/Login'
import Profile from './pages/Profile'
import Register from './pages/Register'
import Reports from './pages/Reports'
import Review from './pages/Review'

function Protected({ children }: { children: ReactNode }) {
  const { isAuthenticated } = useAuth()
  return isAuthenticated ? <>{children}</> : <Navigate to="/login" replace />
}

function AdminOnly({ children }: { children: ReactNode }) {
  const { isAdmin } = useAuth()
  return isAdmin ? <>{children}</> : <Navigate to="/app/dashboard" replace />
}

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<Navigate to="/app/dashboard" replace />} />
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />
      <Route
        path="/app"
        element={
          <Protected>
            <MainLayout />
          </Protected>
        }
      >
        <Route path="dashboard" element={<Dashboard />} />
        <Route path="review" element={<Review />} />
        <Route path="reports" element={<Reports />} />
        <Route path="profile" element={<Profile />} />
        <Route path="admin/users" element={<AdminOnly><AdminUsers /></AdminOnly>} />
        <Route path="admin/data" element={<AdminOnly><AdminDataGovernance /></AdminOnly>} />
      </Route>
    </Routes>
  )
}

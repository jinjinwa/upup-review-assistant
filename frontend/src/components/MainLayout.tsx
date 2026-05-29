import { Activity, Database, FileText, Home, LogOut, Shield, UserRound } from 'lucide-react'
import { NavLink, Outlet, useNavigate } from 'react-router-dom'
import { useAuth } from '../contexts/AuthContext'

export default function MainLayout() {
  const { user, isAdmin, logout } = useAuth()
  const navigate = useNavigate()

  const doLogout = () => {
    logout()
    navigate('/login')
  }

  return (
    <div className="app-layout">
      <aside className="sidebar">
        <div className="brand">
          <strong>Stock Quant</strong>
          <span>Community</span>
        </div>
        <nav>
          <NavLink to="/app/dashboard"><Home size={18} /> 看板</NavLink>
          <NavLink to="/app/review"><Activity size={18} /> Demo 复盘</NavLink>
          <NavLink to="/app/reports"><FileText size={18} /> Demo 报告</NavLink>
          <NavLink to="/app/profile"><UserRound size={18} /> 个人中心</NavLink>
          {isAdmin ? (
            <>
              <NavLink to="/app/admin/users"><Shield size={18} /> 用户管理</NavLink>
              <NavLink to="/app/admin/data"><Database size={18} /> 数据治理</NavLink>
            </>
          ) : null}
        </nav>
        <a className="cta" href="https://upup.live/register?invite=INV-0E08A" target="_blank" rel="noreferrer">
          体验部署版
        </a>
      </aside>
      <main>
        <header className="topbar">
          <div>
            <strong>{user?.username}</strong>
            <span>{user?.role === 'admin' ? '管理员' : '普通用户'}</span>
          </div>
          <button className="ghost-button" onClick={doLogout}><LogOut size={16} /> 退出</button>
        </header>
        <Outlet />
      </main>
    </div>
  )
}

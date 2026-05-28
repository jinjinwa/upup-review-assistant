import PageHeader from '../components/PageHeader'
import { Card } from '../components/ui'
import { useAuth } from '../contexts/AuthContext'

export default function Profile() {
  const { user } = useAuth()

  return (
    <div className="page-shell">
      <PageHeader title="个人中心" description="认证状态来自 JWT 和 /api/auth/me。" />
      <Card>
        <h2>{user?.username}</h2>
        <p>{user?.email}</p>
        <p>角色：{user?.role === 'admin' ? '管理员' : '普通用户'}</p>
      </Card>
    </div>
  )
}

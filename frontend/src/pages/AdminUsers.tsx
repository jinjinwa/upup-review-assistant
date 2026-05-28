import { useEffect, useState } from 'react'
import PageHeader from '../components/PageHeader'
import { Card } from '../components/ui'
import { adminApi } from '../services/api'
import type { User } from '../types/api'

type AdminUser = User & { report_count: number }

export default function AdminUsers() {
  const [users, setUsers] = useState<AdminUser[]>([])
  const [note, setNote] = useState('')

  useEffect(() => {
    adminApi.users().then((result) => {
      setUsers(result.items)
      setNote(result.implementation_note)
    })
  }, [])

  return (
    <div className="page-shell">
      <PageHeader title="管理员 · 用户管理" description="公开的是 RBAC 和 N+1 避免方式，不公开商业权限体系。" />
      <Card>
        <p>{note}</p>
        <table>
          <thead>
            <tr><th>用户</th><th>邮箱</th><th>角色</th><th>报告数</th></tr>
          </thead>
          <tbody>
            {users.map((user) => (
              <tr key={user.id}>
                <td>{user.username}</td>
                <td>{user.email}</td>
                <td>{user.role}</td>
                <td>{user.report_count}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </Card>
    </div>
  )
}

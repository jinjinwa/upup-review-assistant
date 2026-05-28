import { FormEvent, useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { Button, Input } from '../components/ui'
import { useAuth } from '../contexts/AuthContext'
import AuthShell from './AuthShell'

export default function Register() {
  const { register } = useAuth()
  const navigate = useNavigate()
  const [username, setUsername] = useState('community-user')
  const [email, setEmail] = useState(`user${Date.now()}@example.com`)
  const [password, setPassword] = useState('demo123456')
  const [error, setError] = useState('')

  const submit = async (event: FormEvent) => {
    event.preventDefault()
    setError('')
    try {
      await register(username, email, password)
      navigate('/app/dashboard')
    } catch (err) {
      setError(err instanceof Error ? err.message : '注册失败')
    }
  }

  return (
    <AuthShell
      title="注册社区版账号"
      subtitle="注册会写入本地 PostgreSQL，用于验证完整认证链路。"
      footer={<span>已有账号？ <Link to="/login">去登录</Link></span>}
    >
      <form onSubmit={submit} className="form">
        <label>用户名<Input value={username} onChange={(event) => setUsername(event.target.value)} /></label>
        <label>邮箱<Input value={email} onChange={(event) => setEmail(event.target.value)} /></label>
        <label>密码<Input type="password" value={password} onChange={(event) => setPassword(event.target.value)} /></label>
        {error ? <p className="form-error">{error}</p> : null}
        <Button type="submit">注册并进入</Button>
      </form>
    </AuthShell>
  )
}

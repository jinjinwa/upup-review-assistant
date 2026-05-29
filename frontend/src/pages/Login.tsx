import { FormEvent, useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { Button, Input } from '../components/ui'
import { useAuth } from '../contexts/AuthContext'
import AuthShell from './AuthShell'

export default function Login() {
  const { login } = useAuth()
  const navigate = useNavigate()
  const [email, setEmail] = useState('admin@example.com')
  const [password, setPassword] = useState('admin123456')
  const [error, setError] = useState('')

  const submit = async (event: FormEvent) => {
    event.preventDefault()
    setError('')
    try {
      await login(email, password)
      navigate('/app/dashboard')
    } catch (err) {
      setError(err instanceof Error ? err.message : '登录失败')
    }
  }

  return (
    <AuthShell
      title="UPUP 社区版骨架"
      subtitle="登录后可体验完整前后端、数据库、任务队列和权限框架。"
      footer={<span>没有账号？ <Link to="/register">注册一个</Link></span>}
    >
      <form onSubmit={submit} className="form">
        <label>邮箱<Input value={email} onChange={(event) => setEmail(event.target.value)} /></label>
        <label>密码<Input type="password" value={password} onChange={(event) => setPassword(event.target.value)} /></label>
        {error ? <p className="form-error">{error}</p> : null}
        <Button type="submit">登录</Button>
      </form>
    </AuthShell>
  )
}

import type { ReactNode } from 'react'

export default function AuthShell({
  title,
  subtitle,
  children,
  footer,
}: {
  title: string
  subtitle: string
  children: ReactNode
  footer: ReactNode
}) {
  return (
    <div className="auth-page">
      <section className="auth-hero">
        <p className="eyebrow">Open-core community edition</p>
        <h1>{title}</h1>
        <p>{subtitle}</p>
        <div className="auth-demo-accounts">
          <strong>默认账号</strong>
          <span>管理员：admin@example.com / admin123456</span>
          <span>普通用户：demo@example.com / demo123456</span>
        </div>
      </section>
      <section className="auth-card">
        {children}
        <div className="auth-footer">{footer}</div>
        <a className="product-link" href="mailto:1419995247@qq.com">
          产品咨询
        </a>
      </section>
    </div>
  )
}

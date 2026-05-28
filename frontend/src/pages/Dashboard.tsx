import { useEffect, useState } from 'react'
import PageHeader from '../components/PageHeader'
import { Badge, Card } from '../components/ui'
import { demoApi } from '../services/api'

export default function Dashboard() {
  const [overview, setOverview] = useState<{ welcome: string; role: string; modules: string[]; notice: string } | null>(null)

  useEffect(() => {
    demoApi.overview().then(setOverview)
  }, [])

  return (
    <div className="page-shell">
      <PageHeader
        title="社区版工作台"
        description="完整应用骨架：鉴权、角色、数据、任务、前后端路由都能跑通。"
        actions={<Badge>{overview?.role || 'loading'}</Badge>}
      />
      <div className="metric-grid">
        <Card><span>架构层</span><strong>Frontend + API + DB</strong></Card>
        <Card><span>任务层</span><strong>Redis + Celery</strong></Card>
        <Card><span>数据层</span><strong>Alembic schema</strong></Card>
      </div>
      <Card>
        <h2>{overview?.welcome || 'Loading...'}</h2>
        <p>{overview?.notice}</p>
        <div className="module-grid">
          {overview?.modules.map((item) => <Badge key={item}>{item}</Badge>)}
        </div>
      </Card>
    </div>
  )
}

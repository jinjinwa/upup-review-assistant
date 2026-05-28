import { useEffect, useState } from 'react'
import PageHeader from '../components/PageHeader'
import { Button, Card, Badge } from '../components/ui'
import { adminApi } from '../services/api'
import type { DataSource, IntegrationTask } from '../types/api'

export default function AdminDataGovernance() {
  const [sources, setSources] = useState<DataSource[]>([])
  const [tasks, setTasks] = useState<IntegrationTask[]>([])

  const load = async () => {
    const [sourceResult, taskResult] = await Promise.all([adminApi.dataSources(), adminApi.tasks()])
    setSources(sourceResult.items)
    setTasks(taskResult.items)
  }

  const sync = async (id: number) => {
    await adminApi.syncDataSource(id)
    setTimeout(load, 1200)
  }

  useEffect(() => {
    load()
  }, [])

  return (
    <div className="page-shell">
      <PageHeader title="管理员 · 数据治理" description="mock 数据源、mock 集成、Celery 任务状态，展示架构壳子。" />
      <div className="two-column">
        <Card>
          <h2>数据源</h2>
          <div className="list">
            {sources.map((source) => (
              <div className="row compact" key={source.id}>
                <div>
                  <strong>{source.name}</strong>
                  <span>{source.kind}</span>
                </div>
                <Badge>{source.status}</Badge>
                <Button onClick={() => sync(source.id)}>同步</Button>
              </div>
            ))}
          </div>
        </Card>
        <Card>
          <h2>集成任务</h2>
          <div className="list">
            {tasks.map((task) => (
              <div className="task" key={task.id}>
                <div className="row compact">
                  <strong>#{task.id}</strong>
                  <Badge>{task.status}</Badge>
                </div>
                <p>{task.message}</p>
              </div>
            ))}
          </div>
        </Card>
      </div>
    </div>
  )
}

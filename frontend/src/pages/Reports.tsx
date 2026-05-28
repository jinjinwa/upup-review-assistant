import { useEffect, useState } from 'react'
import PageHeader from '../components/PageHeader'
import { Card } from '../components/ui'
import { demoApi } from '../services/api'
import type { DemoReport } from '../types/api'

export default function Reports() {
  const [reports, setReports] = useState<DemoReport[]>([])

  useEffect(() => {
    demoApi.reports().then((result) => setReports(result.items))
  }, [])

  return (
    <div className="page-shell">
      <PageHeader title="Demo 报告" description="人工合成报告列表，用于展示数据库读写和用户隔离。" />
      <div className="list">
        {reports.map((report) => (
          <Card key={report.id}>
            <div className="row">
              <div>
                <h2>{report.title}</h2>
                <p>{report.summary}</p>
              </div>
              <div className="score-pill">{report.score}</div>
            </div>
          </Card>
        ))}
      </div>
    </div>
  )
}

import { useState } from 'react'
import PageHeader from '../components/PageHeader'
import { Button, Card } from '../components/ui'
import { demoApi, scoringApi } from '../services/api'
import type { DemoReport } from '../types/api'

export default function Review() {
  const [report, setReport] = useState<DemoReport | null>(null)
  const [score, setScore] = useState<{ score: number; band: string; summary: string } | null>(null)

  const run = async () => {
    const [nextReport, nextScore] = await Promise.all([demoApi.createReview(), scoringApi.evaluate()])
    setReport(nextReport)
    setScore(nextScore)
  }

  return (
    <div className="page-shell">
      <PageHeader
        title="Demo 复盘"
        description="保留业务工作流壳子，核心策略和真实评分因子已经裁剪。"
        actions={<Button onClick={run}>运行 fake 复盘</Button>}
      />
      <div className="two-column">
        <Card>
          <h2>通用评分器</h2>
          <p>这是可公开的 evaluator 框架，只处理调用方传入的 demo dimensions。</p>
          <div className="score-number">{score?.score ?? '--'}</div>
          <span>{score?.band ?? '尚未运行'}</span>
        </Card>
        <Card>
          <h2>Fake Report</h2>
          <p>{report?.summary || '点击按钮后会写入本地数据库并返回一条 fake report。'}</p>
          {report ? <strong>{report.title} · {report.score}</strong> : null}
        </Card>
      </div>
    </div>
  )
}

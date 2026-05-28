"""Synthetic demo data for the public repository."""

SAMPLE_MARKET = [
    {
        "demo_code": "DEMO001",
        "name": "晨星制造",
        "theme": "智能工坊",
        "labels": ["steady", "prototype", "workshop"],
        "demo_activity": 7,
        "demo_volatility": 2,
        "summary": "A synthetic manufacturing scenario with stable demo participation.",
    },
    {
        "demo_code": "DEMO002",
        "name": "海川能源",
        "theme": "绿色动力",
        "labels": ["energy", "transition"],
        "demo_activity": 5,
        "demo_volatility": 3,
        "summary": "An artificial energy transition scenario for local testing.",
    },
    {
        "demo_code": "DEMO003",
        "name": "云岭科技",
        "theme": "云端协作",
        "labels": ["cloud", "collaboration", "demo-lab", "automation"],
        "demo_activity": 8,
        "demo_volatility": 4,
        "summary": "A synthetic technology scenario with a busy demo workflow.",
    },
    {
        "demo_code": "DEMO004",
        "name": "南桥消费",
        "theme": "社区零售",
        "labels": ["retail", "community"],
        "demo_activity": 4,
        "demo_volatility": 1,
        "summary": "A made-up consumer scenario for showing compact summaries.",
    },
    {
        "demo_code": "DEMO005",
        "name": "星河医药",
        "theme": "健康服务",
        "labels": ["health", "service", "research"],
        "demo_activity": 6,
        "demo_volatility": 2,
        "summary": "An artificial healthcare scenario with balanced demo values.",
    },
]


def get_market_snapshot():
    """Return a copy of the synthetic entries used by the demo page."""
    return {
        "source": "synthetic",
        "count": len(SAMPLE_MARKET),
        "items": [dict(item) for item in SAMPLE_MARKET],
    }

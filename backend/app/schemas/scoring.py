from pydantic import BaseModel, Field


class ScoreDimension(BaseModel):
    name: str
    value: int = Field(ge=0, le=100)
    weight: float = Field(ge=0, le=1)


class ScoreRequest(BaseModel):
    title: str = "Community demo score"
    dimensions: list[ScoreDimension]


class ScoreResult(BaseModel):
    title: str
    score: int
    band: str
    summary: str

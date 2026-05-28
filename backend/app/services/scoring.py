from app.schemas.scoring import ScoreRequest, ScoreResult


def evaluate_score(payload: ScoreRequest) -> ScoreResult:
    total_weight = sum(item.weight for item in payload.dimensions)
    if total_weight <= 0:
        score = 0
    else:
        score = round(sum(item.value * item.weight for item in payload.dimensions) / total_weight)

    if score >= 80:
        band = "community-focus"
    elif score >= 60:
        band = "community-watch"
    else:
        band = "community-observe"

    return ScoreResult(
        title=payload.title,
        score=score,
        band=band,
        summary="Generic score produced from caller-supplied demo dimensions only.",
    )

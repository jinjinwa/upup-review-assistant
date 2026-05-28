from fastapi import APIRouter, Depends

from app.core.auth import get_current_user
from app.core.response import success_response
from app.models import User
from app.schemas.scoring import ScoreRequest
from app.services.scoring import evaluate_score

router = APIRouter(prefix="/api/scoring", tags=["scoring"])


@router.post("/evaluate")
def evaluate(payload: ScoreRequest, user: User = Depends(get_current_user)):
    result = evaluate_score(payload)
    return success_response(result.model_dump())

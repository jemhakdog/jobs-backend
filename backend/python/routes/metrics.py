from fastapi import APIRouter, Depends
from utils.logger import get_logger
from utils.security import validate_input

logger = get_logger(__name__)
router = APIRouter()

@router.get("/metrics")
async def get_metrics(_: None = Depends(validate_input)):
    """
    Retrieve application metrics.

    Returns:
        Response: Prometheus metrics in text format.
    """
    return await metrics()

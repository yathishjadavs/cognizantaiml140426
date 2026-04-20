"""
Utility functions for the Banking Project
"""

import uuid
from datetime import datetime
from config.logger import get_logger
from src.exceptions import InvalidAmountError

logger = get_logger(__name__)


def generate_account_id() -> str:
    """
    Generates a unique account ID
    """
    account_id = f"ACC-{uuid.uuid4().hex[:8].upper()}"
    logger.info(f"Generated account ID: {account_id}")
    return account_id


def validate_amount(amount: float) -> None:
    """
    Validates transaction amount
    """
    if amount <= 0:
        logger.error(f"Invalid amount: {amount}")
        raise InvalidAmountError("Amount must be greater than zero")


def current_timestamp() -> str:
    """
    Returns current timestamp as string
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
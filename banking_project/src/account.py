"""
Account model for the Banking Project
"""

from dataclasses import dataclass
from config.logger import get_logger
from src.exceptions import InvalidAmountError

logger = get_logger(__name__)


@dataclass
class Account:
    """
    Represents a bank account
    """
    account_id: str
    holder_name: str
    balance: float = 0.0

    def __post_init__(self):
        if self.balance < 0:
            logger.error("Account created with negative balance")
            raise InvalidAmountError("Initial balance cannot be negative")

        logger.info(
            f"Account created | ID={self.account_id} | "
            f"Holder={self.holder_name} | Balance={self.balance}"
        )

    def get_balance(self) -> float:
        """
        Returns current balance
        """
        logger.info(
            f"Balance checked | ID={self.account_id} | Balance={self.balance}"
        )
        return self.balance

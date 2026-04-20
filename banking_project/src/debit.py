"""
Debit logic for the Banking Project
"""

import uuid

from config.logger import get_logger
from src.account import Account
from src.storage import save_account
from src.utils import validate_amount
from src.transaction import record_transaction
from src.exceptions import (
    BankingError,
    InsufficientBalanceError,
)

logger = get_logger(__name__)


def debit(account: Account, amount: float) -> None:
    """
    Debit (withdraw) money from an account
    """
    try:
        logger.info(
            f"Debit requested | ID={account.account_id} | Amount={amount}"
        )

        validate_amount(amount)

        if account.balance < amount:
            logger.error(
                f"Insufficient balance | ID={account.account_id} | "
                f"Balance={account.balance} | Amount={amount}"
            )
            raise InsufficientBalanceError("Insufficient balance")

        account.balance -= amount
        save_account(account)

        transaction_id = str(uuid.uuid4())

        record_transaction(
            transaction_id=transaction_id,
            account_id=account.account_id,
            transaction_type="DEBIT",
            amount=amount,
        )

        logger.info(
            f"Debit successful | ID={account.account_id} | "
            f"Amount={amount} | New Balance={account.balance}"
        )

    except BankingError:
        raise
    except Exception:
        logger.exception("Unexpected error during debit operation")
        raise
"""
Credit logic for the Banking Project
"""

import uuid

from config.logger import get_logger
from src.account import Account
from src.storage import save_account
from src.utils import validate_amount
from src.transaction import record_transaction
from src.exceptions import BankingError

logger = get_logger(__name__)


def credit(account: Account, amount: float) -> None:
    """
    Credit (add) money to an account
    """
    try:
        logger.info(
            f"Credit requested | ID={account.account_id} | Amount={amount}"
        )

        validate_amount(amount)

        account.balance += amount
        save_account(account)

        transaction_id = str(uuid.uuid4())

        record_transaction(
            transaction_id=transaction_id,
            account_id=account.account_id,
            transaction_type="CREDIT",
            amount=amount,
        )

        logger.info(
            f"Credit successful | ID={account.account_id} | "
            f"Amount={amount} | New Balance={account.balance}"
        )

    except BankingError:
        raise
    except Exception:
        logger.exception("Unexpected error during credit operation")
        raise

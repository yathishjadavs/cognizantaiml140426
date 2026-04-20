"""
Transaction handling for the Banking Project
"""

from dataclasses import dataclass
from typing import List, Dict
import json
from pathlib import Path

from config.logger import get_logger
from src.utils import current_timestamp
from src.exceptions import StorageError

logger = get_logger(__name__)

# Directory and file for transactions
DATA_DIR = Path("data")
TRANSACTION_FILE = DATA_DIR / "transactions.json"


@dataclass
class Transaction:
    transaction_id: str
    account_id: str
    transaction_type: str  # CREDIT or DEBIT
    amount: float
    timestamp: str


def _ensure_data_dir() -> None:
    """Ensure the data directory exists."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)


def _read_transactions() -> List[Dict]:
    """Read all transactions from JSON file."""
    _ensure_data_dir()

    if not TRANSACTION_FILE.exists():
        return []

    try:
        with open(TRANSACTION_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        logger.exception("Failed to read transactions file")
        raise StorageError("Unable to read transaction history") from e


def _write_transactions(data: List[Dict]) -> None:
    """Write transactions to JSON file."""
    _ensure_data_dir()

    try:
        with open(TRANSACTION_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)
    except Exception as e:
        logger.exception("Failed to write transactions file")
        raise StorageError("Unable to save transaction history") from e


def record_transaction(
    transaction_id: str,
    account_id: str,
    transaction_type: str,
    amount: float
) -> None:
    """
    Record a transaction (CREDIT or DEBIT)
    """
    transaction = Transaction(
        transaction_id=transaction_id,
        account_id=account_id,
        transaction_type=transaction_type,
        amount=amount,
        timestamp=current_timestamp()
    )

    transactions = _read_transactions()
    transactions.append(transaction.__dict__)
    _write_transactions(transactions)

    logger.info(
        f"Transaction recorded | "
        f"ID={transaction_id} | "
        f"Account={account_id} | "
        f"Type={transaction_type} | "
        f"Amount={amount}"
    )
    
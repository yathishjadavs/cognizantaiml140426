"""
Storage layer for saving and loading account data
"""

import json
from pathlib import Path
from typing import Dict

from config.logger import get_logger
from src.account import Account
from src.exceptions import StorageError, AccountNotFoundError

logger = get_logger(__name__)

# Directory to store data files
DATA_DIR = Path("data")
ACCOUNTS_FILE = DATA_DIR / "accounts.json"


def _ensure_data_dir() -> None:
    """Ensure data directory exists."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)


def _read_accounts() -> Dict[str, dict]:
    """Read all accounts from JSON file."""
    _ensure_data_dir()

    if not ACCOUNTS_FILE.exists():
        return {}

    try:
        with open(ACCOUNTS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        logger.exception("Failed to read accounts file")
        raise StorageError("Unable to read accounts data") from e


def _write_accounts(data: Dict[str, dict]) -> None:
    """Write all accounts to JSON file."""
    _ensure_data_dir()

    try:
        with open(ACCOUNTS_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        logger.exception("Failed to write accounts file")
        raise StorageError("Unable to save accounts data") from e


def save_account(account: Account) -> None:
    """
    Save or update an account
    """
    data = _read_accounts()

    data[account.account_id] = {
        "account_id": account.account_id,
        "holder_name": account.holder_name,
        "balance": account.balance,
    }

    _write_accounts(data)
    logger.info(f"Account saved | ID={account.account_id}")


def load_account(account_id: str) -> Account:
    """
    Load an account by account_id
    """
    data = _read_accounts()

    if account_id not in data:
        logger.error(f"Account not found | ID={account_id}")
        raise AccountNotFoundError(f"Account {account_id} not found")

    acc = data[account_id]
    logger.info(f"Account loaded | ID={account_id}")

    return Account(
        account_id=acc["account_id"],
        holder_name=acc["holder_name"],
        balance=acc["balance"],
    )

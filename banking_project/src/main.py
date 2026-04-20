"""
CLI entry point for the Banking Project
"""

from config.logger import get_logger
from src.account import Account
from src.utils import generate_account_id
from src.credit import credit
from src.debit import debit
from src.storage import save_account, load_account
from src.exceptions import BankingError

logger = get_logger(__name__)


def create_account() -> Account:
    name = input("Enter account holder name: ").strip()
    initial_balance = float(input("Enter initial balance: "))

    account = Account(
        account_id=generate_account_id(),
        holder_name=name,
        balance=initial_balance,
    )

    save_account(account)
    print("✅ Account created successfully")
    print(f"Account ID: {account.account_id}")

    return account


def load_existing_account() -> Account:
    account_id = input("Enter account ID: ").strip()
    account = load_account(account_id)
    print("✅ Account loaded successfully")
    return account


def show_menu():
    print("\n====== Banking System Menu ======")
    print("1. Create new account")
    print("2. Load existing account")
    print("3. Credit amount")
    print("4. Debit amount")
    print("5. Check balance")
    print("0. Exit")
    print("================================")


def main():
    logger.info("Banking CLI started")
    account = None

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                account = create_account()

            elif choice == "2":
                account = load_existing_account()

            elif choice == "3":
                if not account:
                    print("⚠️ Load or create an account first")
                    continue
                amount = float(input("Enter amount to credit: "))
                credit(account, amount)
                print("✅ Amount credited successfully")

            elif choice == "4":
                if not account:
                    print("⚠️ Load or create an account first")
                    continue
                amount = float(input("Enter amount to debit: "))
                debit(account, amount)
                print("✅ Amount debited successfully")

            elif choice == "5":
                if not account:
                    print("⚠️ Load or create an account first")
                    continue
                print(f"💰 Current Balance: {account.get_balance()}")

            elif choice == "0":
                logger.info("Banking CLI exited")
                print("👋 Exiting Banking System. Goodbye!")
                break

            else:
                print("❌ Invalid choice. Please try again.")

        except BankingError as e:
            print(f"❌ Error: {e}")
            logger.error(e)

        except Exception as e:
            print("❌ Unexpected error occurred")
            logger.exception(e)


if __name__ == "__main__":
    main()
    
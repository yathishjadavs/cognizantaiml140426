"""
Custom exceptions for the Banking Project
"""


class BankingError(Exception):
    """Base class for all banking-related exceptions"""
    pass


class AccountNotFoundError(BankingError):
    """Raised when an account is not found"""
    pass


class InvalidAmountError(BankingError):
    """Raised when amount is invalid (<= 0)"""
    pass


class InsufficientBalanceError(BankingError):
    """Raised when balance is insufficient for debit"""
    pass


class TransactionError(BankingError):
    """Raised when a transaction fails"""
    pass


class StorageError(BankingError):
    """Raised when saving or loading data fails"""
    pass
    
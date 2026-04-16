"""
healthcare_app package

This file marks healthcare_app as a Python package and
exposes core classes for easy importing.
"""

from .patient import Patient
from .doctor import Doctor

__all__ = ["Patient", "Doctor"]

"""Thêm tính năng — code sạch."""
from decimal import Decimal


def total(items: list[Decimal]) -> Decimal:
    return sum(items, Decimal("0"))

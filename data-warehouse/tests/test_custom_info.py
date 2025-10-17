import pytest
from datetime import date
from models import CustomInfo
from pydantic import ValidationError


def test_valid_customer_info():
    """Test that the model validates with correct data."""
    data = {
        "cst_id": 1,
        "cst_key": "C001",
        "cst_firstname": "John",
        "cst_lastname": "Doe",
        "cst_marital_status": "Single",
        "cst_gndr": "M",
        "cst_create_date": "2025-10-17",
    }

    model = CustomInfo(**data)
    assert model.cst_id == 1
    assert model.cst_create_date == date(2025, 10, 17)


def test_invalid_date_format():
    """Test that an invalid date format raises a validation error."""
    data = {
        "cst_id": 2,
        "cst_key": "C002",
        "cst_create_date": "17/10/2025",  # ❌ invalid format
    }

    with pytest.raises(ValidationError):
        CustomInfo(**data)


def test_missing_optional_fields():
    """Test that model initializes even with missing optional fields."""
    model = CustomInfo(cst_id=3)
    assert model.cst_id == 3
    assert model.cst_firstname is None
    assert model.cst_create_date is None


def test_wrong_type():
    """Test that wrong data types raise a validation error."""
    data = {
        "cst_id": "not-an-int",  # ❌ string instead of int
    }

    with pytest.raises(ValidationError):
        CustomInfo(**data)
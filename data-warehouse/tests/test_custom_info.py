import pytest
import csv
from datetime import date
from models import CustomInfo
from pydantic import ValidationError


DATA_FILE = "datasets/source_crm/cust_info.csv"


def test_custom_info_from_csv():
    """Validate first 10 rows from CSV file using CustomInfo model."""
    with open(DATA_FILE, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for i, row in enumerate(reader):
            if i >= 10:
                break

            row["cst_id"] = int(row["cst_id"])
            row["cst_create_date"] = row["cst_create_date"]

            model = CustomInfo(**row)
            assert isinstance(model.cst_id, int)
            assert isinstance(model.cst_create_date, date)


def test_invalid_custom_info_from_csv():
    """Test that invalid data in CSV raises ValidationError."""
    invalid_data = {
        "cst_id": "not-an-int",
        "cst_key": "C999",
        "cst_firstname": "Alice",
        "cst_lastname": "Wonder",
        "cst_marital_status": "Single",
        "cst_gndr": "F",
        "cst_create_date": "2025-10-20",
    }

    with pytest.raises(ValidationError):
        CustomInfo(**invalid_data)


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

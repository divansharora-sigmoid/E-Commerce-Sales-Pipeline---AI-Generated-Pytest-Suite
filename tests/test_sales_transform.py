import pandas as pd
import pytest
from pipeline.sales_transform import clean_sales_data


class TestCleanSalesData:
    """Comprehensive pytest suite for clean_sales_data function."""

    # ========== Positive Tests ==========
    def test_valid_data_preserved(self):
        """Test that valid data rows are preserved."""
        data = {
            "customer_id": [1, 2, 3],
            "sales_amount": [100.0, 200.0, 300.0]
        }
        df = pd.DataFrame(data)
        
        result = clean_sales_data(df)
        
        assert len(result) == 3
        assert list(result["customer_id"]) == [1, 2, 3]
        assert list(result["sales_amount"]) == [100.0, 200.0, 300.0]

    def test_return_type_is_dataframe(self):
        """Test that function returns a pandas DataFrame."""
        data = {"customer_id": [1], "sales_amount": [100]}
        df = pd.DataFrame(data)
        
        result = clean_sales_data(df)
        
        assert isinstance(result, pd.DataFrame)

    # ========== Null Handling Tests ==========
    def test_null_customer_id_dropped(self):
        """Test that rows with null customer_id are dropped."""
        data = {
            "customer_id": [1, None, 3],
            "sales_amount": [100.0, 200.0, 300.0]
        }
        df = pd.DataFrame(data)
        
        result = clean_sales_data(df)
        
        assert len(result) == 2
        assert 1 in result["customer_id"].values
        assert 3 in result["customer_id"].values
        assert None not in result["customer_id"].values

    def test_null_sales_amount_filled_with_zero(self):
        """Test that null sales_amount values are filled with 0."""
        data = {
            "customer_id": [1, 2],
            "sales_amount": [100.0, None]
        }
        df = pd.DataFrame(data)
        
        result = clean_sales_data(df)
        
        assert len(result) == 2
        assert result["sales_amount"].iloc[1] == 0.0
        assert result["sales_amount"].isna().sum() == 0

    def test_both_null_conditions(self):
        """Test handling when both customer_id is null and sales_amount is null."""
        data = {
            "customer_id": [1, None],
            "sales_amount": [100, None]
        }
        df = pd.DataFrame(data)
        
        result = clean_sales_data(df)
        
        assert len(result) == 1
        assert result["customer_id"].iloc[0] == 1
        assert result["sales_amount"].iloc[0] == 100.0

    # ========== Edge Cases ==========
    def test_empty_dataframe(self):
        """Test handling of empty DataFrame."""
        df = pd.DataFrame({"customer_id": [], "sales_amount": []})
        
        result = clean_sales_data(df)
        
        assert len(result) == 0
        assert isinstance(result, pd.DataFrame)

    def test_all_null_customer_ids(self):
        """Test DataFrame where all customer_ids are null."""
        data = {
            "customer_id": [None, None, None],
            "sales_amount": [100.0, 200.0, 300.0]
        }
        df = pd.DataFrame(data)
        
        result = clean_sales_data(df)
        
        assert len(result) == 0

    def test_all_null_sales_amounts(self):
        """Test DataFrame where all sales_amounts are null."""
        data = {
            "customer_id": [1, 2, 3],
            "sales_amount": [None, None, None]
        }
        df = pd.DataFrame(data)
        
        result = clean_sales_data(df)
        
        assert len(result) == 3
        assert all(result["sales_amount"] == 0.0)

    def test_zero_sales_amount_preserved(self):
        """Test that explicit zero sales_amount is preserved."""
        data = {
            "customer_id": [1, 2],
            "sales_amount": [0.0, 100.0]
        }
        df = pd.DataFrame(data)
        
        result = clean_sales_data(df)
        
        assert len(result) == 2
        assert result["sales_amount"].iloc[0] == 0.0

    def test_negative_sales_amount_preserved(self):
        """Test that negative sales_amount (refunds) is preserved."""
        data = {
            "customer_id": [1, 2],
            "sales_amount": [-50.0, 100.0]
        }
        df = pd.DataFrame(data)
        
        result = clean_sales_data(df)
        
        assert len(result) == 2
        assert result["sales_amount"].iloc[0] == -50.0

    def test_large_values(self):
        """Test handling of very large sales amounts."""
        data = {
            "customer_id": [1, 2],
            "sales_amount": [999999999.99, 100.0]
        }
        df = pd.DataFrame(data)
        
        result = clean_sales_data(df)
        
        assert len(result) == 2
        assert result["sales_amount"].iloc[0] == 999999999.99

    def test_string_customer_id(self):
        """Test handling of string customer_id values."""
        data = {
            "customer_id": ["CUST001", "CUST002", None],
            "sales_amount": [100.0, 200.0, 300.0]
        }
        df = pd.DataFrame(data)
        
        result = clean_sales_data(df)
        
        assert len(result) == 2
        assert "CUST001" in result["customer_id"].values

    def test_single_row_valid(self):
        """Test with single valid row."""
        data = {
            "customer_id": [1],
            "sales_amount": [100.0]
        }
        df = pd.DataFrame(data)
        
        result = clean_sales_data(df)
        
        assert len(result) == 1
        assert result["customer_id"].iloc[0] == 1
        assert result["sales_amount"].iloc[0] == 100.0

    def test_single_row_null_customer(self):
        """Test with single row having null customer_id."""
        data = {
            "customer_id": [None],
            "sales_amount": [100.0]
        }
        df = pd.DataFrame(data)
        
        result = clean_sales_data(df)
        
        assert len(result) == 0

    def test_original_dataframe_not_modified(self):
        """Test that the original DataFrame is not modified (immutability)."""
        data = {
            "customer_id": [1, None],
            "sales_amount": [100.0, None]
        }
        df = pd.DataFrame(data)
        original_len = len(df)
        
        result = clean_sales_data(df)
        
        # Original should remain unchanged
        assert len(df) == original_len
        assert df["customer_id"].isna().sum() == 1
        assert df["sales_amount"].isna().sum() == 1

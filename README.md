# E-Commerce Sales Pipeline - AI-Generated Pytest Suite

## Project Overview

This project demonstrates AI-powered unit testing for an e-commerce ETL (Extract, Transform, Load) pipeline. The goal was to generate comprehensive pytest test suites using Claude Code for validating data transformation logic.

## Architecture

```
Shopify API → Python ETL → Snowflake
                ↓
           pytest Suite (AI-Generated)
```

## Project Structure

```
ecommerce-pipeline/
├── pipeline/
│   ├── __init__.py
│   └── sales_transform.py      # ETL transformation logic
├── tests/
│   ├── __init__.py
│   └── test_sales_transform.py # AI-generated pytest suite
├── requirements.txt             # Python dependencies
└── README.md                   # This file
```

## Technologies Used

- **Python 3.11+**
- **pytest** - Testing framework
- **pytest-cov** - Coverage reporting
- **pandas** - Data manipulation
- **Claude Code** - AI test generation

## Transformation Logic

The `clean_sales_data()` function in `@/pipeline/sales_transform.py` performs two key data cleaning operations:

1. **Drops rows with null `customer_id`** - Ensures every transaction has a valid customer
2. **Fills null `sales_amount` with 0** - Handles missing sales data gracefully

## AI-Generated Test Suite

The test suite in `@/tests/test_sales_transform.py` was entirely generated using Claude Code with the following prompt:

> Generate a complete pytest suite for the clean_sales_data function.
> Include: Positive tests, Null handling, Edge cases, Coverage support

### Test Coverage (15 Tests)

| Category | Test Cases |
|----------|------------|
| **Positive Tests** | Valid data preservation, Return type validation |
| **Null Handling** | Null customer_id dropped, Null sales_amount filled, Both conditions |
| **Edge Cases** | Empty DataFrame, All null customer_ids, All null sales_amounts, Zero values, Negative amounts, Large values, String customer_ids, Single row scenarios, DataFrame immutability |

## Running the Tests

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Tests with Coverage

```bash
pytest --cov=. -v
```

### Generate HTML Coverage Report

```bash
pytest --cov=. --cov-report=html
```

Open `htmlcov/index.html` in your browser to view the detailed coverage report.

## Test Results

- **15/15 tests passed**
- **100% code coverage** (103 statements, 0 missed)
- All edge cases covered

## Key Learnings

### 1. AI-Generated Testing
- Claude Code successfully generated comprehensive test cases covering positive, negative, and edge scenarios
- Test suite follows pytest best practices with descriptive test names and docstrings
- Organized using class-based test grouping for maintainability

### 2. pytest Automation
- Parameterized test structure for ETL validation
- Proper use of pandas DataFrame assertions
- Coverage integration for quality metrics

### 3. ETL Validation Patterns
- Null handling strategies for data pipelines
- DataFrame immutability testing
- Type safety and edge case validation

## Sample Test Output

```
======================================== test session starts ========================================
platform darwin -- Python 3.10.13, pytest-9.0.3
rootdir: /Users/as-mac-1266/Desktop/GEN/week2/day5_lab1
collected 15 items

tests/test_sales_transform.py::TestCleanSalesData::test_valid_data_preserved PASSED          [  6%]
tests/test_sales_transform.py::TestCleanSalesData::test_return_type_is_dataframe PASSED       [ 13%]
tests/test_sales_transform.py::TestCleanSalesData::test_null_customer_id_dropped PASSED        [ 20%]
tests/test_sales_transform.py::TestCleanSalesData::test_null_sales_amount_filled_with_zero PASSED [ 26%]
tests/test_sales_transform.py::TestCleanSalesData::test_both_null_conditions PASSED           [ 33%]
tests/test_sales_transform.py::TestCleanSalesData::test_empty_dataframe PASSED                [ 40%]
tests/test_sales_transform.py::TestCleanSalesData::test_all_null_customer_ids PASSED          [ 46%]
tests/test_sales_transform.py::TestCleanSalesData::test_all_null_sales_amounts PASSED         [ 53%]
tests/test_sales_transform.py::TestCleanSalesData::test_zero_sales_amount_preserved PASSED    [ 60%]
tests/test_sales_transform.py::TestCleanSalesData::test_negative_sales_amount_preserved PASSED [ 66%]
tests/test_sales_transform.py::TestCleanSalesData::test_large_values PASSED                  [ 73%]
tests/test_sales_transform.py::TestCleanSalesData::test_string_customer_id PASSED            [ 80%]
tests/test_sales_transform.py::TestCleanSalesData::test_single_row_valid PASSED             [ 86%]
tests/test_sales_transform.py::TestCleanSalesData::test_single_row_null_customer PASSED      [ 93%]
tests/test_sales_transform.py::TestCleanSalesData::test_original_dataframe_not_modified PASSED [100%]

======================================== 15 passed in 0.78s =========================================
```

## Deliverables

- [x] pytest suite with 15 comprehensive tests
- [x] HTML coverage report showing 100% coverage
- [x] Automated validation pipeline
- [x] ETL transformation logic for e-commerce sales data

## Next Steps

This pipeline can be extended with:
- Additional transformations (data type conversion, duplicate removal)
- Integration tests for Shopify API and Snowflake connections
- Performance benchmarks for large datasets
- CI/CD pipeline integration for automated testing

---

**Lab:** AI-Generated pytest Suite for E-Commerce Sales Pipeline  
**Domain:** E-Commerce Analytics  
**Status:** ✅ Complete
# E-Commerce-Sales-Pipeline---AI-Generated-Pytest-Suite

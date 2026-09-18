# E-Commerce Data Platform & Business Analytics

## Project Overview

This project is an end-to-end e-commerce data platform built using Python, Snowflake, SQL, and Power BI.

The project demonstrates how raw retail transaction data can be extracted, cleaned, transformed, loaded into a cloud data warehouse, modeled using a star schema, analyzed using SQL, and visualized through an interactive Power BI dashboard.

## Architecture

Raw Excel Dataset
        ↓
Python ETL
        ↓
Snowflake RAW
        ↓
Snowflake STAGING
        ↓
Snowflake ANALYTICS
        ↓
SQL Analysis
        ↓
Power BI Dashboard

## Technologies Used

- Python
- Pandas
- Snowflake
- SQL
- Power BI
- Excel
- Git / GitHub

## Dataset

Dataset: UCI Online Retail II

The dataset contains online retail transactions including:

- Invoice
- Stock Code
- Product Description
- Quantity
- Invoice Date
- Price
- Customer ID
- Country

The dataset contains both sales and cancellation transactions.

## Data Processing

Python was used to:

1. Load both Excel sheets.
2. Combine the datasets.
3. Remove duplicate records.
4. Remove invalid negative prices.
5. Identify cancellation transactions.
6. Calculate transaction-level revenue.
7. Handle Customer ID as a nullable field.
8. Export the processed dataset to CSV.

### Transformation Results

- Raw records: 1,067,371
- Duplicate records removed: 34,335
- Invalid negative-price records removed: 5
- Final processed records: 1,033,031
- Sales transactions: 1,013,927
- Cancellation transactions: 19,104

## Snowflake Data Warehouse

The Snowflake database contains three layers:

### RAW

Stores the processed transaction data loaded from the CSV file.

### STAGING

Provides a cleaned and standardized layer for analytics.

### ANALYTICS

Contains the dimensional data model used for reporting.

## Data Model

A star schema was created with:

### Fact Table

`FACT_SALES`

Contains transaction-level measures such as:

- Quantity
- Price
- Total Amount
- Transaction Type
- Invoice
- Customer
- Product
- Date

### Dimension Tables

- `DIM_CUSTOMER`
- `DIM_PRODUCT`
- `DIM_DATE`
- `DIM_COUNTRY`

## Business Analysis

SQL was used to calculate:

- Gross Sales
- Cancellation Amount
- Net Sales
- Average Order Value
- Total Orders
- Total Customers
- Repeat Customers
- Repeat Customer Rate
- Monthly Sales
- Country Sales
- Top Products
- Top Customers
- Monthly Cancellation Rate

## Key Results

- Gross Sales: £20.48M
- Cancellation Amount: -£1.46M
- Net Sales: £19.01M
- Orders: 45,331
- Identified Customers: 5,881
- Average Order Value: £451.71
- Repeat Customer Rate: approximately 72%
- UK Gross Sales: approximately £17.41M

## Power BI Dashboard

The Power BI report provides interactive business analysis including:

- Sales KPIs
- Monthly Sales Trends
- Customer Analysis
- Top Customers by Revenue
- Top Products by Revenue
- Top Products by Quantity
- Customer Repeat Rate
- Average Order Value
- Cancellation Analysis
- Country Filtering

## Data Quality

The project also identifies important data quality issues in the source data:

- Missing Customer IDs
- Missing product descriptions
- Duplicate transactions
- Cancellation transactions
- Zero-price transactions
- Operational/non-product stock codes

Instead of silently removing business-relevant cancellations, the project preserves them and classifies transactions using `TransactionType`.

## Project Skills Demonstrated

### Data Engineering

- ETL pipeline development
- Data cleaning
- Data validation
- Snowflake data warehouse
- RAW / STAGING / ANALYTICS architecture
- Star schema
- Fact and dimension modeling
- SQL transformations
- Data quality analysis

### Data Analytics

- Exploratory Data Analysis
- Business KPI development
- SQL analytics
- Customer analysis
- Product analysis
- Revenue analysis
- Power BI dashboards
- Business insights

## Project Outcome

This project demonstrates an end-to-end workflow from raw transactional data to a cloud data warehouse and business intelligence dashboard.
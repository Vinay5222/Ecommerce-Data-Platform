# Data Dictionary

## FACT_SALES

| Column | Description |
|---|---|
| INVOICE | Unique invoice number |
| STOCK_CODE | Product or item code |
| CUSTOMER_ID | Customer identifier |
| COUNTRY | Customer country |
| DATE_KEY | Transaction date |
| QUANTITY | Number of units in the transaction |
| PRICE | Unit price |
| TRANSACTION_TYPE | Sale or Cancellation |
| TOTAL_AMOUNT | Quantity multiplied by price |

## DIM_PRODUCT

| Column | Description |
|---|---|
| STOCK_CODE | Unique product/item code |
| DESCRIPTION | Product description |

## DIM_CUSTOMER

| Column | Description |
|---|---|
| CUSTOMER_ID | Unique identified customer |

## DIM_COUNTRY

| Column | Description |
|---|---|
| COUNTRY | Customer country |

## DIM_DATE

| Column | Description |
|---|---|
| DATE_KEY | Calendar date |
| YEAR | Year of transaction |
| MONTH | Month number |
| MONTH_NAME | Month name |
| QUARTER | Calendar quarter |
| WEEK | Week number |
| DAY | Day of month |
| DAY_NAME | Day name |

## Important Business Definitions

### Gross Sales

Total transaction amount for transactions classified as `Sale`.

### Cancellations

Total transaction amount for transactions classified as `Cancellation`.

Cancellation amounts are negative because the original dataset records returned/cancelled quantities as negative values.

### Net Sales

Gross sales plus cancellation amounts.

### Average Order Value

Gross Sales divided by the number of distinct sales invoices.

### Repeat Customer

A customer with more than one distinct sales invoice.
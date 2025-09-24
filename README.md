# ZainAI Mock Data Generator

This project generates mock datasets for various business scenarios using Python and the Faker library. The generated data is organized into three main categories, each with multiple CSV files, and is useful for analytics, testing, and demonstration purposes.

**Key Features:**
- 15 comprehensive datasets with 10,000 rows each
- Realistic business scenarios across telecommunications, ERP, and financial services
- Multiple use cases from analytics to AI model training

## Structure

- `generate_mock_data.py`: Main script to generate all datasets.
- `datasets/`: Output folder containing all generated CSV files, organized by business scenario:
  - `TurningInformationIntoIntelligence/`: Customer analytics and intelligence datasets
  - `EnterpriseResourcePlanning/`: HR, project management, and internal operations datasets  
  - `TransactionManagement/`: Financial transactions and banking datasets


## Data Categories, Tables, Examples, and Use Cases

### 1. Turning Information into Intelligence

#### Customers.csv
- **Description:** Customer demographic and account information.
- **Rows:** 10,000
- **Example Row:**
   | customer_id | age | gender | city     | plan_type | join_date  | churned | last_month_usage_gb | complaints_count | loyalty_score |
   |-------------|-----|--------|----------|-----------|------------|---------|---------------------|------------------|---------------|
   | C00001      | 34  | F      | Manama   | Prepaid   | 2021-05-12 | 0       | 23.45               | 2                | 0.85          |
- **Use Cases:**
   - Customer segmentation
   - Churn prediction
   - Personalization

#### Calls.csv
- **Description:** Call, SMS, and data session records for customers.
- **Rows:** 10,000
- **Example Row:**
   | call_id | customer_id | call_type | duration_min | date       | cell_tower_id |
   |---------|-------------|-----------|--------------|------------|---------------|
   | uuid-123| C00023      | voice     | 12.50        | 2024-11-03 | T045          |
- **Use Cases:**
   - Usage analytics
   - Fraud detection
   - Network optimization

#### InternetUsage.csv
- **Description:** Internet usage logs by app category.
- **Rows:** 10,000
- **Example Row:**
   | usage_id | customer_id | date       | data_used_gb | app_category | device_type |
   |----------|-------------|------------|--------------|--------------|-------------|
   | uuid-456 | C00045      | 2025-01-15 | 2.34         | Streaming    | Mobile      |
- **Use Cases:**
   - App popularity analysis
   - Data plan recommendations
   - Network planning

#### SupportTickets.csv
- **Description:** Customer support ticket records.
- **Rows:** 10,000
- **Example Row:**
   | ticket_id | customer_id | issue_category | priority | date_opened | status   | resolution_time_hours |
   |-----------|-------------|----------------|----------|-------------|----------|----------------------|
   | uuid-789  | C00012      | Billing        | High     | 2025-03-10  | Open     | 24.5                 |
- **Use Cases:**
   - Support workload analysis
   - Issue trend detection
   - SLA monitoring

#### SocialSentiment.csv
- **Description:** Social media posts mentioning the company, with sentiment and topic.
- **Rows:** 10,000
- **Example Row:**
   | post_id  | customer_id | platform | sentiment | topic           | date       | likes | shares |
   |----------|-------------|----------|-----------|-----------------|------------|-------|--------|
   | uuid-101 | C00001      | Twitter  | Positive  | Customer Service| 2025-06-21 | 150   | 45     |
- **Use Cases:**
   - Brand sentiment analysis
   - Social listening
   - Campaign impact measurement

#### FinancialTransactions.csv
- **Description:** Customer financial transaction records including payments and top-ups.
- **Rows:** 10,000
- **Example Row:**
   | transaction_id | customer_id | amount | method   | date       | status  | fraud_flag |
   |----------------|-------------|--------|----------|------------|---------|------------|
   | uuid-112       | C00001      | 25.50  | Top-up   | 2023-06-15 | Success | 0          |
- **Use Cases:**
   - Revenue analysis
   - Payment behavior patterns
   - Fraud detection

#### NetworkPerformance.csv
- **Description:** Network performance metrics by region.
- **Rows:** 10,000
- **Example Row:**
   | record_id | region  | signal_strength | latency_ms | downtime_minutes | date       | tower_load_percentage |
   |-----------|---------|-----------------|------------|------------------|------------|-----------------------|
   | 1         | Manama  | 4               | 45         | 5                | 2023-08-20 | 75.5                  |
- **Use Cases:**
   - Network optimization
   - Service quality monitoring
   - Infrastructure planning

#### CustomerDemographics.csv
- **Description:** Extended customer demographic information.
- **Rows:** 10,000 (matches customers)
- **Example Row:**
   | customer_id | income_bracket | household_size | nationality | education_level |
   |-------------|----------------|----------------|-------------|-----------------|
   | C00001      | Medium         | 3              | Bahraini    | Bachelor        |
- **Use Cases:**
   - Market segmentation
   - Product targeting
   - Demographic analysis

#### ProductCatalog.csv
- **Description:** Available products and services catalog.
- **Rows:** 10,000
- **Example Row:**
   | product_id | name            | price_bhd | active |
   |------------|-----------------|-----------|--------|
   | 1          | Unlimited Social| 15.50     | 1      |
- **Use Cases:**
   - Product portfolio management
   - Pricing analysis
   - Catalog optimization

### 2. Enterprise Resource Planning (ERP)

#### Employees.csv
- **Description:** Employee information including demographics, department, role, and salary.
- **Rows:** 10,000
- **Example Row:**
   | employee_id | name        | age | gender | department | role     | join_date  | salary_bhd |
   |-------------|-------------|-----|--------|------------|----------|------------|------------|
   | E00001      | John Smith  | 32  | M      | IT         | Engineer | 2020-03-15 | 2500.00    |
- **Use Cases:**
   - HR analytics
   - Salary benchmarking
   - Department analysis
   - Employee retention

#### Projects.csv
- **Description:** Project information with status and assigned managers.
- **Rows:** 10,000
- **Example Row:**
   | project_id | name       | start_date | end_date   | status    | manager_id |
   |------------|------------|------------|------------|-----------|------------|
   | P0001      | Project 1  | 2023-01-15 | 2024-01-15 | Active    | E00001     |
- **Use Cases:**
   - Project portfolio management
   - Resource allocation
   - Timeline analysis
   - Success rate tracking

#### Tasks.csv
- **Description:** Task assignments and completion tracking for employees.
- **Rows:** 10,000
- **Example Row:**
   | task_id | project_id | assignee_id | description           | priority | status      | due_date   |
   |---------|------------|-------------|-----------------------|----------|-------------|------------|
   | T00001  | P0001      | E00001      | Complete system setup | High     | In Progress | 2024-05-15 |
- **Use Cases:**
   - Project management
   - Resource allocation
   - Performance tracking
   - Workload analysis

### 3. Transaction Management

#### Customers.csv (Finance)
- **Description:** Financial services customer information with account details.
- **Rows:** 10,000
- **Example Row:**
   | customer_id | name        | account_type | balance_bhd | join_date  |
   |-------------|-------------|--------------|-------------|------------|
   | CF00001     | Jane Doe    | Savings      | 15000.50    | 2020-06-10 |
- **Use Cases:**
   - Account management
   - Customer segmentation
   - Balance analysis
   - Retention strategies

#### Transactions.csv
- **Description:** Financial transaction records with fraud detection flags.
- **Rows:** 10,000
- **Example Row:**
   | transaction_id | customer_id | transaction_type | amount_bhd | date       | status  | fraud_flag |
   |----------------|-------------|------------------|------------|------------|---------|------------|
   | uuid-trans-1   | CF00001     | Deposit          | 500.00     | 2024-01-15 | Success | 0          |
- **Use Cases:**
   - Transaction monitoring
   - Fraud detection
   - Financial analytics
   - Compliance reporting

## Requirements

- Python 3.7+
- Packages: `pandas`, `faker`, `numpy`

Install dependencies with:

```bash
pip install pandas faker numpy
```

## Usage

Run the script to generate all datasets:

```bash
python generate_mock_data.py
```

The generated CSV files will be saved in the `datasets/` directory, organized by scenario:
- `datasets/TurningInformationIntoIntelligence/` - Customer intelligence datasets (9 files)
- `datasets/EnterpriseResourcePlanning/` - HR and project management datasets (3 files)
- `datasets/TransactionManagement/` - Financial transaction datasets (2 files)

## Customization

- To change the number of rows, modify the `n` parameter values in the function calls within the `main()` function in `generate_mock_data.py`.
- To add new fields or modify data generation logic, update the respective generator functions (e.g., `generate_customers()`, `generate_calls()`, etc.).
- You can adjust the field values, categories, or business logic in the script to fit your specific needs.
- All datasets currently generate 10,000 rows each for consistency across business scenarios.

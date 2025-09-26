# ZainAI Mock Data Generator

This project generates mock datasets for various business scenarios using Python and the Faker library. The generated data is organized into three main categories, each with multiple CSV files, and is useful for analytics, testing, and demonstration purposes.

**Key Features:**
- 14 comprehensive datasets with 10,000 rows each
- Three distinct business domains: Intelligence, Operations, and Customer Experience
- Enhanced product catalog with electronics and technology products
- New purchase tracking system with installment payment support
- Customer engagement analytics and campaign tracking
- Multiple use cases from analytics to AI model training

## What's New in This Version

### 🛍️ **E-Commerce Integration**
- **Enhanced Product Catalog**: Electronics and technology products with brands, warranties, release years, and specifications
- **Purchase Tracking System**: New purchase system supporting both full payments and installment plans
- **Payment Management**: Track remaining balances and payment schedules for installment purchases
- **Product-Customer Analytics**: Link customer purchases to demographics and engagement patterns

### 📊 **Customer Engagement Analytics** 
- **Engagement History Tracking**: Monitor customer interactions across multiple channels (Email, SMS, App, Call)
- **Campaign Performance**: Track customer responses to marketing campaigns with detailed analytics
- **Multi-channel Insights**: Analyze engagement patterns and conversion rates across different communication channels

### 🔧 **Technical Improvements**
- **Consistent Scale**: All datasets now generate exactly 10,000 rows for uniform analysis
- **Right-sized Datasets**: Optimized row counts for realistic business scenarios (200-2000 rows per dataset)
- **Focused Data Models**: Each domain addresses specific business challenges and use cases

### 💳 **Advanced Payment Features**
- **Installment Payment System**: Support for multi-installment purchase tracking with remaining balances
- **Enhanced Transaction Types**: Expanded payment methods including installment and add-on payments
- **Purchase-to-Payment Linking**: Connect customer purchases with financial transaction history

### 🔧 **Technical Improvements**
- **Optimized Data Structure**: Better data relationships and foreign key structures across datasets
- **Realistic Business Logic**: More authentic data distributions and business scenarios
- **Cleaner Organization**: Intuitive folder structure by business domain

## Structure

- `generate_mock_data.py`: Main script to generate all datasets.
- `datasets/`: Output folder containing all generated CSV files, organized by business domain:
  - `TurningInformationIntoIntelligence/`: Customer analytics, product catalog, purchases, and network intelligence (10 datasets)
  - `ReinventingHowWorkGetsDone/`: Employee management, project tracking, and task assignments (3 datasets)
  - `RedefiningEngagementAndExperiences/`: Customer engagement tracking and campaign analytics (1 dataset)


## Data Categories, Tables, Examples, and Use Cases

### 1. Turning Information into Intelligence

#### Customers.csv
- **Description:** Customer demographic and account information with loyalty scoring.
- **Rows:** 10,000
- **Example Row:**
   | customer_id | age | gender | city     | plan_type | join_date  | churned | last_month_usage_gb | complaints_count | loyalty_score |
   |-------------|-----|--------|----------|-----------|------------|---------|---------------------|------------------|---------------|
   | C00001      | 34  | F      | Manama   | Prepaid   | 2021-05-12 | 0       | 23.45               | 2                | 0.85          |
- **Use Cases:**
   - Customer segmentation and churn prediction
   - Loyalty program optimization
   - Personalized service offerings

#### ProductCatalog.csv
- **Description:** Electronics and technology product catalog with comprehensive specifications.
- **Rows:** 10,000
- **Example Row:**
   | product_id | name              | type    | price_bhd | brand  | warranty_years | release_year | active |
   |------------|------------------|---------|-----------|--------|----------------|--------------|--------|
   | 1          | BrandA Phone 1   | Phone   | 899.50    | BrandA | 2              | 2023         | 1      |
- **Use Cases:**
   - Product portfolio management
   - Pricing strategy analysis
   - Inventory optimization
   - Brand performance tracking

#### Purchases.csv
- **Description:** Customer purchase records with installment payment support.
- **Rows:** 10,000
- **Example Row:**
   | purchase_id | customer_id | product_id | payment_type | installments_total | remaining_amount | status    | purchase_date |
   |-------------|-------------|------------|--------------|-------------------|------------------|-----------|---------------|
   | uuid-123    | C00001      | 1          | Installment  | 6                 | 299.83          | Pending   | 2024-03-15    |
- **Use Cases:**
   - Purchase behavior analysis
   - Installment payment tracking
   - Customer lifetime value calculation
   - Payment default prediction

#### FinancialTransactions.csv
- **Description:** Customer financial transactions including installment payments.
- **Rows:** 10,000
- **Example Row:**
   | transaction_id | customer_id | amount_bhd | method              | date       | status  | fraud_flag |
   |----------------|-------------|------------|---------------------|------------|---------|------------|
   | uuid-456       | C00001      | 150.75     | Installment Payment | 2024-06-15 | Success | 0          |
- **Use Cases:**
   - Revenue analysis
   - Payment behavior patterns
   - Fraud detection
   - Cash flow management

#### Calls.csv
- **Description:** Call, SMS, and data session records with network infrastructure tracking.
- **Rows:** 10,000
- **Example Row:**
   | call_id  | customer_id | call_type | duration_min | date       | cell_tower_id |
   |----------|-------------|-----------|--------------|------------|---------------|
   | uuid-789 | C00023      | voice     | 12.50        | 2024-11-03 | T045          |
- **Use Cases:**
   - Usage analytics and network optimization
   - Tower load balancing
   - Customer usage pattern analysis

#### InternetUsage.csv
- **Description:** Internet usage logs by app category and device type.
- **Rows:** 10,000
- **Example Row:**
   | usage_id | customer_id | date       | data_used_gb | app_category | device_type |
   |----------|-------------|------------|--------------|--------------|-------------|
   | uuid-101 | C00045      | 2025-01-15 | 2.34         | Streaming    | Mobile      |
- **Use Cases:**
   - Data plan optimization
   - Multi-device usage analysis
   - App performance insights

#### SupportTickets.csv
- **Description:** Customer support ticket records with resolution time tracking.
- **Rows:** 10,000
- **Example Row:**
   | ticket_id | customer_id | issue_category | priority | date_opened | status   | resolution_time_hours |
   |-----------|-------------|----------------|----------|-------------|----------|----------------------|
   | uuid-112  | C00012      | Billing        | High     | 2025-03-10  | Open     | 24.5                 |
- **Use Cases:**
   - Support workload analysis
   - SLA monitoring
   - Issue trend detection

#### SocialSentiment.csv
- **Description:** Social media posts with engagement metrics.
- **Rows:** 10,000
- **Example Row:**
   | post_id  | customer_id | platform | sentiment | topic           | date       | likes | shares |
   |----------|-------------|----------|-----------|-----------------|------------|-------|--------|
   | uuid-113 | C00001      | Twitter  | Positive  | Customer Service| 2025-06-21 | 150   | 45     |
- **Use Cases:**
   - Brand sentiment analysis
   - Social media engagement tracking
   - Campaign impact measurement

#### NetworkPerformance.csv
- **Description:** Network performance metrics by region with tower load data.
- **Rows:** 10,000
- **Example Row:**
   | record_id | region  | signal_strength | latency_ms | downtime_minutes | date       | tower_load_percentage |
   |-----------|---------|-----------------|------------|------------------|------------|-----------------------|
   | 1         | Manama  | 4               | 45         | 5                | 2023-08-20 | 75.5                  |
- **Use Cases:**
   - Network optimization
   - Infrastructure planning
   - Service quality monitoring

#### CustomerDemographics.csv
- **Description:** Extended customer demographic information with education levels.
- **Rows:** 10,000 (matches customers)
- **Example Row:**
   | customer_id | income_bracket | household_size | nationality | education_level |
   |-------------|----------------|----------------|-------------|-----------------|
   | C00001      | Medium         | 3              | Bahraini    | Bachelor        |
- **Use Cases:**
   - Market segmentation
   - Targeted marketing campaigns
   - Demographic trend analysis

### 2. Reinventing How Work Gets Done

#### Employees.csv
- **Description:** Employee information with department and salary details.
- **Rows:** 10,000
- **Example Row:**
   | employee_id | name        | age | gender | department | role     | join_date  | salary_bhd |
   |-------------|-------------|-----|--------|------------|----------|------------|------------|
   | E00001      | John Smith  | 32  | M      | IT         | Engineer | 2020-03-15 | 2500.00    |
- **Use Cases:**
   - HR analytics and salary benchmarking
   - Department performance analysis
   - Employee retention strategies

#### Projects.csv
- **Description:** Project information with status tracking and manager assignments.
- **Rows:** 10,000
- **Example Row:**
   | project_id | name       | start_date | end_date   | status | manager_id |
   |------------|------------|------------|------------|--------|------------|
   | P0001      | Project 1  | 2023-01-15 | 2024-01-15 | Active | E00001     |
- **Use Cases:**
   - Project portfolio management
   - Resource allocation optimization
   - Timeline and success rate analysis

#### Tasks.csv
- **Description:** Task assignments and completion tracking with priority management.
- **Rows:** 10,000
- **Example Row:**
   | task_id | project_id | assignee_id | description           | priority | status      | due_date   |
   |---------|------------|-------------|-----------------------|----------|-------------|------------|
   | T00001  | P0001      | E00001      | Complete system setup | High     | In Progress | 2024-05-15 |
- **Use Cases:**
   - Project management and tracking
   - Employee workload analysis
   - Performance monitoring

### 3. Redefining Engagement & Experiences

#### EngagementHistory.csv
- **Description:** Customer engagement tracking across multiple channels and campaigns.
- **Rows:** 10,000
- **Example Row:**
   | engagement_id | customer_id | campaign    | channel          | response  | date       |
   |---------------|-------------|-------------|------------------|-----------|------------|
   | uuid-114      | C00001      | Campaign 15 | App Notification | Clicked   | 2024-08-15 |
- **Use Cases:**
   - Campaign performance analysis
   - Multi-channel engagement optimization
   - Customer journey mapping
   - Conversion rate analysis

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

The generated CSV files will be saved in the `datasets/` directory, organized by business domain:
- `datasets/TurningInformationIntoIntelligence/` - Customer intelligence and product analytics (10 files)
- `datasets/ReinventingHowWorkGetsDone/` - Employee and project management (3 files)
- `datasets/RedefiningEngagementAndExperiences/` - Customer engagement tracking (1 file)

## Customization

- To change the number of rows, modify the `n` parameter values in the function calls within the `main()` function in `generate_mock_data.py`.
- To add new fields or modify data generation logic, update the respective generator functions (e.g., `generate_customers()`, `generate_product_catalog()`, `generate_purchases()`, etc.).
- You can adjust the field values, categories, or business logic in the script to fit your specific needs.
- All datasets consistently generate 10,000 rows each for uniform analysis and comparison across business scenarios.

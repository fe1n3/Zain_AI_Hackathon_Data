# ZainAI Mock Data Generator

This project generates mock datasets for various business scenarios using Python and the Faker library. The generated data is organized into three main categories, each with multiple CSV files, and is useful for analytics, testing, and demonstration purposes.

**Key Features:**
- 25 comprehensive datasets with 10,000 rows each
- Realistic business scenarios across telecommunications
- Multiple use cases from analytics to AI model training

## Structure

- `generate_mock_data.py`: Main script to generate all datasets.
- `ZainAI_MockData/`: Output folder containing all generated CSV files, organized by scenario.


## Data Categories, Tables, Examples, and Use Cases

### 1. Turning Information into Intelligence

#### 1a_Customers.csv
- **Description:** Customer demographic and account information.
- **Example Row:**
   | customer_id | age | gender | city     | plan_type | join_date  | churned | last_month_usage_gb | complaints_count |
   |-------------|-----|--------|----------|-----------|------------|---------|---------------------|------------------|
   | C001        | 34  | F      | Manama   | Prepaid   | 2021-05-12 | 0       | 23.45               | 2                |
- **Use Cases:**
   - Customer segmentation
   - Churn prediction
   - Personalization

#### 1b_Calls.csv
- **Description:** Call, SMS, and data session records for customers.
- **Example Row:**
   | call_id | customer_id | call_type | duration_min | date       |
   |---------|-------------|-----------|--------------|------------|
   | CL001   | C023        | voice     | 12.50        | 2024-11-03 |
- **Use Cases:**
   - Usage analytics
   - Fraud detection
   - Network optimization

#### 1c_InternetUsage.csv
- **Description:** Internet usage logs by app category.
- **Example Row:**
   | usage_id | customer_id | date       | data_used_gb | app_category  |
   |----------|-------------|------------|--------------|---------------|
   | U001     | C045        | 2025-01-15 | 2.34         | Streaming     |
- **Use Cases:**
   - App popularity analysis
   - Data plan recommendations
   - Network planning

#### 1d_SupportTickets.csv
- **Description:** Customer support ticket records.
- **Example Row:**
   | ticket_id | customer_id | issue_category | priority | date_opened | status   |
   |-----------|-------------|----------------|----------|-------------|----------|
   | T001      | C012        | Billing        | High     | 2025-03-10  | Open     |
- **Use Cases:**
   - Support workload analysis
   - Issue trend detection
   - SLA monitoring

#### 1e_SocialSentiment.csv
- **Description:** Social media posts mentioning the company, with sentiment and topic.
- **Example Row:**
   | post_id | platform  | sentiment | topic           | date       |
   |---------|-----------|-----------|-----------------|------------|
   | S001    | Twitter   | Positive  | Customer Service| 2025-06-21 |
- **Use Cases:**
   - Brand sentiment analysis
   - Social listening
   - Campaign impact measurement

#### 1f_FinancialTransactions.csv
- **Description:** Customer financial transaction records including payments and top-ups.
- **Example Row:**
   | transaction_id | customer_id | amount | method      | date       | status  |
   |----------------|-------------|--------|-------------|------------|---------|
   | TX00001        | C00001      | 25.50  | Top-up      | 2023-06-15 | Success |
- **Use Cases:**
   - Revenue analysis
   - Payment behavior patterns
   - Fraud detection

#### 1g_NetworkPerformance.csv
- **Description:** Network performance metrics by region.
- **Example Row:**
   | record_id | region  | signal_strength | latency_ms | downtime_minutes | date       |
   |-----------|---------|-----------------|------------|------------------|------------|
   | NP00001   | Manama  | 4               | 45         | 5                | 2023-08-20 |
- **Use Cases:**
   - Network optimization
   - Service quality monitoring
   - Infrastructure planning

#### 1h_CustomerDemographics.csv
- **Description:** Extended customer demographic information.
- **Example Row:**
   | customer_id | income_bracket | household_size | nationality    |
   |-------------|----------------|----------------|----------------|
   | C00001      | Medium         | 3              | Bahraini       |
- **Use Cases:**
   - Market segmentation
   - Product targeting
   - Demographic analysis

#### 1i_ProductCatalog.csv
- **Description:** Available products and services catalog.
- **Example Row:**
   | product_id | name            | price_bhd | category | active |
   |------------|-----------------|-----------|----------|--------|
   | P001       | Unlimited Social| 15.50     | Data     | 1      |
- **Use Cases:**
   - Product portfolio management
   - Pricing analysis
   - Catalog optimization

### 2. Redefining Engagement & Experiences

#### 2a_CustomerProfiles.csv
- **Description:** Customer engagement preferences and recent activity.
- **Example Row:**
   | customer_id | interests         | preferred_channel | last_engagement_date |
   |-------------|------------------|-------------------|---------------------|
   | C001        | Gaming, Sports   | WhatsApp          | 2025-07-15          |
- **Use Cases:**
   - Targeted marketing
   - Channel optimization
   - Engagement scoring

#### 2b_EmployeeProfiles.csv
- **Description:** Employee department, role, and learning preferences.
- **Example Row:**
   | employee_id | department | role     | completed_trainings | preferred_learning_mode |
   |-------------|------------|----------|---------------------|------------------------|
   | E001        | IT         | Analyst  | 3                   | Video                  |
- **Use Cases:**
   - Training needs analysis
   - HR analytics
   - Internal mobility planning

#### 2c_Campaigns.csv
- **Description:** Marketing campaign details and engagement rates.
- **Example Row:**
   | campaign_id | type   | target_audience         | engagement_rate | date_sent  |
   |-------------|--------|------------------------|----------------|------------|
   | CM001       | Email  | C001, C002, C003, ...  | 0.23           | 2025-08-01 |
- **Use Cases:**
   - Campaign performance analysis
   - Audience segmentation
   - A/B testing
     - *A/B testing* is a method of comparing two versions of a campaign, product, or feature to determine which performs better by randomly exposing different groups to each version and measuring outcomes.

#### 2d_MediaAssets.csv
- **Description:** Metadata for media assets used in campaigns.
- **Example Row:**
   | asset_id | type  | topic           | engagement_score |
   |----------|-------|-----------------|------------------|
   | M001     | Image | Customer Service| 0.67             |
- **Use Cases:**
   - Content effectiveness analysis
   - Asset management
   - Creative optimization

#### 2e_FeedbackSurveys.csv
- **Description:** Customer feedback and satisfaction surveys.
- **Example Row:**
   | survey_id | customer_id | score | comment         | date       |
   |-----------|-------------|-------|-----------------|------------|
   | SV0001    | C00001      | 4     | Great service   | 2024-03-15 |
- **Use Cases:**
   - Customer satisfaction tracking
   - Service improvement
   - Sentiment analysis

#### 2f_RewardsRedemptions.csv
- **Description:** Customer loyalty program reward redemptions.
- **Example Row:**
   | redemption_id | customer_id | reward_type    | date       |
   |---------------|-------------|----------------|------------|
   | RW0001        | C00001      | Data Voucher   | 2024-05-20 |
- **Use Cases:**
   - Loyalty program analysis
   - Reward effectiveness
   - Customer retention

#### 2g_EventParticipation.csv
- **Description:** Customer participation in company events.
- **Example Row:**
   | event_id | customer_id | event_name    | attended | date       |
   |----------|-------------|---------------|----------|------------|
   | EV001    | C00001      | Hackathon     | 1        | 2024-06-10 |
- **Use Cases:**
   - Event effectiveness
   - Community engagement
   - Customer relationship building

#### 2h_ContentInteractions.csv
- **Description:** Customer interactions with digital content.
- **Example Row:**
   | interaction_id | customer_id | content_id | type  | date       |
   |----------------|-------------|------------|-------|------------|
   | IN00001        | C00001      | M001       | Click | 2024-07-25 |
- **Use Cases:**
   - Content performance analysis
   - User behavior tracking
   - Personalization algorithms
- **Use Cases:**
   - Targeted marketing
   - Channel optimization
   - Engagement scoring

#### 2b_EmployeeProfiles.csv
- **Description:** Employee department, role, and learning preferences.
- **Example Row:**
   | employee_id | department | role     | completed_trainings | preferred_learning_mode |
   |-------------|------------|----------|---------------------|------------------------|
   | E001        | IT         | Analyst  | 3                   | Video                  |
- **Use Cases:**
   - Training needs analysis
   - HR analytics
   - Internal mobility planning

#### 2c_Campaigns.csv
- **Description:** Marketing campaign details and engagement rates.
- **Example Row:**
   | campaign_id | type   | target_audience         | engagement_rate | date_sent  |
   |-------------|--------|------------------------|----------------|------------|
   | CM001       | Email  | C001, C002, C003, ...  | 0.23           | 2025-08-01 |
- **Use Cases:**
   - Campaign performance analysis
   - Audience segmentation
   - A/B testing

#### 2d_MediaAssets.csv
- **Description:** Metadata for media assets used in campaigns.
- **Example Row:**
   | asset_id | type  | topic           | engagement_score |
   |----------|-------|-----------------|------------------|
   | M001     | Image | Customer Service| 0.67             |
- **Use Cases:**
   - Content effectiveness analysis
   - Asset management
   - Creative optimization

### 3. Reinventing How Work Gets Done

#### 3a_HRRequests.csv
- **Description:** HR-related requests from employees.
- **Example Row:**
   | request_id | employee_id | type      | date_submitted | status   |
   |------------|-------------|-----------|----------------|----------|
   | HR001      | E005        | Leave     | 2025-04-10     | Approved |
- **Use Cases:**
   - HR process automation
   - Request volume analysis
   - Policy compliance

#### 3b_FinanceRequests.csv
- **Description:** Finance-related requests and approvals.
- **Example Row:**
   | request_id | department | type         | amount | status   | date_submitted |
   |------------|------------|--------------|--------|----------|---------------|
   | F001       | Marketing  | Purchase     | 1200.5 | Pending  | 2025-05-12    |
- **Use Cases:**
   - Expense tracking
   - Budget planning
   - Approval workflow analysis

#### 3c_ITTickets.csv
- **Description:** IT support ticket records for employees.
- **Example Row:**
   | ticket_id | employee_id | issue_type   | priority | date_opened | status   |
   |-----------|-------------|-------------|----------|-------------|----------|
   | IT001     | E010        | VPN Setup   | Medium   | 2025-07-01  | Resolved |
- **Use Cases:**
   - IT support analytics
   - Issue trend monitoring
   - Resource allocation

#### 3d_Meetings.csv
- **Description:** Meeting records with participants and transcripts.
- **Example Row:**
   | meeting_id | participants     | transcript                        | date       |
   |------------|------------------|------------------------------------|------------|
   | MT001      | E001, E002       | Discussed project. Action: follow up| 2025-08-20 |
- **Use Cases:**
   - Meeting analytics
   - Action item tracking
   - Collaboration analysis

#### 3e_TaskAssignments.csv
- **Description:** Task assignments and completion tracking for employees.
- **Example Row:**
   | task_id | employee_id | description     | deadline   | status    |
   |---------|-------------|----------------|------------|-----------|
   | TK0001  | E001        | Prepare report | 2024-05-15 | Completed |
- **Use Cases:**
   - Project management
   - Resource allocation
   - Performance tracking

#### 3f_ProcurementRequests.csv
- **Description:** Procurement and vendor requests by departments.
- **Example Row:**
   | request_id | department | vendor  | amount_bhd | status   | date       |
   |------------|------------|---------|------------|----------|------------|
   | PR0001     | IT         | VendorA | 2500.00    | Approved | 2024-03-20 |
- **Use Cases:**
   - Vendor management
   - Budget control
   - Procurement analytics

#### 3g_SystemLogs.csv
- **Description:** System event logs across various platforms.
- **Example Row:**
   | log_id  | timestamp           | system | event  | severity |
   |---------|---------------------|--------|--------|----------|
   | LG00001 | 2024-06-15 14:30:25 | CRM    | Login  | Low      |
- **Use Cases:**
   - System monitoring
   - Security analysis
   - Performance optimization

#### 3h_KnowledgeBase.csv
- **Description:** Knowledge base articles and documentation.
- **Example Row:**
   | article_id | title              | content                    | tags            |
   |------------|--------------------|----------------------------|----------------|
   | KB001      | Network troubleshooting| This is a guide for...    | ["Network"]    |
- **Use Cases:**
   - Knowledge management
   - Self-service support
   - Content organization

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

The generated CSV files will be saved in the `ZainAI_MockData/` directory, organized by scenario.

## Customization

- To change the number of rows, modify the `range` values in `generate_mock_data.py`.
- You can adjust the fields, categories, or logic in the script to fit your needs.

# ZainAI Mock Data Generator

This project generates mock datasets for various business scenarios using Python and the Faker library. The generated data is organized into three main categories, each with multiple CSV files, and is useful for analytics, testing, andThe generated CSV files will be saved in the `datasets/` directory, organized by business domain:
- `datasets/TurningInformationIntoIntelligence/` - Customer intelligence and product analytics (10 files)
- `datasets/ReinventingHowWorkGetsDone/` - Complete operational management (10 files)
- `datasets/RedefiningEngagementAndExperiences/` - Customer experience and marketing analytics (7 files)

**Total: 27 CSV files** covering comprehensive business operations from customer analytics to internal operations and engagement tracking.stration purposes.

**Key Features:**
- 27 comprehensive datasets across three business domains
- Realistic business scenarios covering telecommunications, operations, and customer experience
- Enhanced product catalog with electronics and technology products
- Complete purchase tracking system with installment payment support
- Advanced employee management and project tracking systems
- Comprehensive customer engagement and experience analytics
- Multiple use cases from analytics to AI model training

## Structure

- `generate_mock_data.py`: Main script to generate all datasets.
- `datasets/`: Output folder containing all generated CSV files, organized by business domain:
  - `TurningInformationIntoIntelligence/`: Customer analytics, product catalog, and network intelligence (10 datasets)
  - `ReinventingHowWorkGetsDone/`: Complete operational management including HR, IT, finance, and project management (10 datasets)
  - `RedefiningEngagementAndExperiences/`: Customer experience, marketing campaigns, and engagement analytics (7 datasets)


## Data Categories, Tables, Examples, and Use Cases

### 1. Turning Information into Intelligence (10 Datasets)

#### Customers.csv
- **Description:** Customer demographic and account information with loyalty scoring.
- **Rows:** 10,000
- **Example Row:**
   | customer_id | age | gender | city     | plan_type | churned | loyalty_score |
   |-------------|-----|--------|----------|-----------|---------|---------------|
   | C00001      | 34  | F      | Manama   | Prepaid   | 0       | 0.85          |

#### ProductCatalog.csv  
- **Description:** Electronics and technology product catalog with specifications.
- **Rows:** 10,000
- **Example Row:**
   | product_id | name           | type  | price_bhd | brand  | warranty_years |
   |------------|----------------|-------|-----------|--------|----------------|
   | 1          | BrandA Phone 1 | Phone | 899.50    | BrandA | 2              |

#### Purchases.csv
- **Description:** Customer purchase records with installment payment support.
- **Rows:** 10,000
- **Example Row:**
   | purchase_id | customer_id | product_id | payment_type | installments_total | status  |
   |-------------|-------------|------------|--------------|-------------------|---------|
   | uuid-123    | C00001      | 1          | Installment  | 6                 | Pending |

#### FinancialTransactions.csv
- **Description:** Customer financial transactions including installment payments.
- **Rows:** 10,000
- **Example Row:**
   | transaction_id | customer_id | amount_bhd | method              | status  | fraud_flag |
   |----------------|-------------|------------|---------------------|---------|------------|
   | uuid-456       | C00001      | 150.75     | Installment Payment | Success | 0          |

#### Calls.csv
- **Description:** Call, SMS, and data session records with network tracking.
- **Rows:** 10,000
- **Example Row:**
   | call_id  | customer_id | call_type | duration_min | cell_tower_id |
   |----------|-------------|-----------|--------------|---------------|
   | uuid-789 | C00001      | voice     | 15.5         | T001          |

#### InternetUsage.csv
- **Description:** Internet usage logs by app category and device type.
- **Rows:** 10,000
- **Example Row:**
   | usage_id  | customer_id | data_used_gb | app_category | device_type |
   |-----------|-------------|--------------|--------------|-------------|
   | uuid-101  | C00001      | 2.5          | Social Media | Mobile      |

#### SupportTickets.csv
- **Description:** Customer support ticket records with resolution tracking.
- **Rows:** 10,000
- **Example Row:**
   | ticket_id | customer_id | issue_category | priority | status   | resolution_time_hours |
   |-----------|-------------|----------------|----------|----------|-----------------------|
   | uuid-102  | C00001      | Billing        | Medium   | Resolved | 24.5                  |

#### SocialSentiment.csv
- **Description:** Social media posts with engagement metrics.
- **Rows:** 10,000
- **Example Row:**
   | post_id  | customer_id | platform | sentiment | topic   | likes | shares |
   |----------|-------------|----------|-----------|---------|-------|--------|
   | uuid-103 | C00001      | Twitter  | Positive  | Network | 25    | 5      |

#### NetworkPerformance.csv
- **Description:** Network performance metrics by region with tower load data.
- **Rows:** 10,000
- **Example Row:**
   | record_id | region | signal_strength | latency_ms | tower_load_percentage |
   |-----------|--------|-----------------|------------|-----------------------|
   | 1         | Manama | 4               | 45         | 75.2                  |

#### CustomerDemographics.csv
- **Description:** Extended customer demographic information.
- **Rows:** 10,000 (matches customers)
- **Example Row:**
   | customer_id | income_bracket | household_size | nationality | education_level |
   |-------------|----------------|----------------|-------------|-----------------|
   | C00001      | Medium         | 4              | Bahraini    | Bachelor        |

### 2. Reinventing How Work Gets Done (10 Datasets)

#### Employees.csv
- **Description:** Employee information with department and salary details.
- **Rows:** 10000
- **Example Row:**
   | employee_id | name       | department | role     | salary_bhd |
   |-------------|------------|------------|----------|------------|
   | E00001      | John Smith | IT         | Engineer | 2500.00    |

#### Projects.csv
- **Description:** Project information with status tracking and manager assignments.
- **Rows:** 10000
- **Example Row:**
   | project_id | name       | status | manager_id | start_date | end_date   |
   |------------|------------|--------|------------|------------|------------|
   | P0001      | Project 1  | Active | E00001     | 2023-01-15 | 2024-06-30 |

#### Tasks.csv
- **Description:** Task assignments and completion tracking.
- **Rows:** 10000
- **Example Row:**
   | task_id | project_id | assignee_id | description       | priority | status      |
   |---------|------------|-------------|-------------------|----------|-------------|
   | T00001  | P0001      | E00005      | Implement feature | High     | In Progress |

#### HRRequests.csv
- **Description:** HR-related requests from employees.
- **Rows:** 10000
- **Example Row:**
   | request_id | employee_id | request_type | status   |
   |------------|-------------|--------------|----------|
   | HR00001    | E00005      | Leave        | Approved |

#### FinanceRequests.csv
- **Description:** Finance-related requests and budget approvals.
- **Rows:** 10000
- **Example Row:**
   | request_id | employee_id | request_type | amount_bhd | status  |
   |------------|-------------|--------------|------------|---------|
   | FN00001    | E00010      | Purchase     | 1200.50    | Pending |

#### ITTickets.csv
- **Description:** IT support ticket records for employees.
- **Rows:** 10000
- **Example Row:**
   | ticket_id | employee_id | category | priority | status      |
   |-----------|-------------|----------|----------|-------------|
   | IT00001   | E00015      | Hardware | High     | In Progress |

#### Meetings.csv
- **Description:** Meeting records with participants and action items.
- **Rows:** 10000
- **Example Row:**
   | meeting_id | topic              | participants        | action_items          |
   |------------|--------------------|---------------------|-----------------------|
   | M00001     | Weekly standup     | E00001,E00002,E00003| Review project status |

#### TaskAssignments.csv
- **Description:** Task assignments and completion tracking.
- **Rows:** 10000
- **Example Row:**
   | task_id | employee_id | project_id | priority | status    | due_date   |
   |---------|-------------|------------|----------|-----------|------------|
   | T00001  | E00005      | P0001      | High     | Completed | 2024-03-15 |

#### ProcurementRequests.csv
- **Description:** Procurement and vendor requests by departments.
- **Rows:** 10000
- **Example Row:**
   | request_id | department | item   | quantity | status   |
   |------------|------------|--------|----------|----------|
   | PR00001    | IT         | Laptop | 5        | Approved |

#### SystemLogs.csv
- **Description:** System event logs across various platforms.
- **Rows:** 10000
- **Example Row:**
   | log_id | system | event | severity | timestamp           |
   |--------|--------|-------|----------|---------------------|
   | SL00001| ERP    | Login | Low      | 2024-03-15 09:30:15 |

### 3. Redefining Engagement & Experiences (7 Datasets)

#### CustomerProfiles.csv
- **Description:** Customer engagement preferences and activity tracking.
- **Rows:** 10000
- **Example Row:**
   | customer_id | preferred_channel | loyalty_score | historical_engagement |
   |-------------|------------------|---------------|----------------------|
   | C00001      | SMS              | 0.85          | 75                   |

#### EmployeeProfiles.csv
- **Description:** Employee engagement and training profiles.
- **Rows:** 10000
- **Example Row:**
   | employee_id | name       | role     | training_completed | engagement_score |
   |-------------|------------|----------|-------------------|------------------|
   | E00001      | John Smith | Engineer | 12                | 0.88             |

#### Campaigns.csv
- **Description:** Marketing campaign details across multiple channels.
- **Rows:** 10000
- **Example Row:**
   | campaign_id | name       | channel      | budget_bhd | target_segment |
   |-------------|------------|--------------|------------|----------------|
   | CM0001      | Campaign 1 | Email        | 25000.00   | Youth          |

#### FeedbackSurveys.csv
- **Description:** Customer and employee satisfaction surveys.
- **Rows:** 10000
- **Example Row:**
   | survey_id | subject_id | category | topic        | rating |
   |-----------|------------|----------|--------------|--------|
   | S00001    | C00001     | Customer | Satisfaction | 4      |

#### RewardsRedemptions.csv
- **Description:** Customer loyalty program reward redemptions.
- **Rows:** 10000
- **Example Row:**
   | redemption_id | customer_id | reward_type | points_spent | date       |
   |---------------|-------------|-------------|--------------|------------|
   | R00001        | C00001      | Discount    | 100          | 2024-03-15 |

#### EventParticipation.csv
- **Description:** Customer participation in company events.
- **Rows:** 10000
- **Example Row:**
   | participation_id | customer_id | event_type | attendance |
   |------------------|-------------|------------|------------|
   | EV00001          | C00001      | Workshop   | Attended   |

#### ContentInteractions.csv
- **Description:** Customer interactions with digital content and campaigns.
- **Rows:** 10000
- **Example Row:**
   | interaction_id | customer_id | campaign_id | action | date       |
   |----------------|-------------|-------------|--------|------------|
   | CI00001        | C00001      | CM0001      | Click  | 2024-03-15 |

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
- `datasets/ReinventingHowWorkGetsDone/` - Complete operational management (11 files)
- `datasets/RedefiningEngagementAndExperiences/` - Customer experience and marketing analytics (9 files)

**Total: 27 CSV files** covering comprehensive business operations from customer analytics to internal operations and engagement tracking.

## Customization

- To change the number of rows, modify the `n` parameter values in the function calls within the `main()` function in `generate_mock_data.py`.
- To add new fields or modify data generation logic, update the respective generator functions (e.g., `generate_customers()`, `generate_hr_requests()`, `generate_campaigns()`, etc.).
- You can adjust the field values, categories, or business logic in the script to fit your specific needs.
- Dataset sizes are optimized for different business functions:
  - **Large datasets (10,000 rows)**: Core customer and product data for robust analytics
  - **Medium datasets (500-2,000 rows)**: Operational data like employees, tasks, and content interactions
  - **Small datasets (200-500 rows)**: Specialized data like projects, campaigns, and administrative records
- To enable/disable specific datasets, comment/uncomment the corresponding lines in the `main()` function.

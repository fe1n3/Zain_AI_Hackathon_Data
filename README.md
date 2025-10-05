# ZainAI Mock Data Generator

This project generates mock datasets for various business scenarios using Python and the Faker library. The generated data is organized into three main categories, each with multiple CSV files, and is useful for analytics, testing, and demonstration purposes.

**Key Features:**
- 30 comprehensive datasets across three business domains
- Realistic business scenarios covering telecommunications, operations, and customer experience
- Enhanced product catalog with electronics and technology products
- Complete purchase tracking system with installment payment support
- Advanced employee management and project tracking systems
- Comprehensive customer engagement and experience analytics
- Multiple use cases from analytics to AI model training

## What's New in This Version

### � **Massive Dataset Expansion**
- **30 Total Datasets**: Expanded from 14 to 30 comprehensive business datasets
- **Complete Business Operations**: Full coverage of telecommunications, HR, finance, IT, and customer experience
- **Advanced Engagement Tracking**: Comprehensive customer experience and employee engagement analytics
- **Operational Intelligence**: Complete internal operations tracking from HR to procurement

### �🛍️ **E-Commerce & Financial Integration** 
- **Enhanced Product Catalog**: Electronics and technology products with brands, warranties, release years
- **Purchase Tracking System**: Full payment and installment tracking with remaining balances
- **Financial Transaction Management**: Complete transaction lifecycle from purchases to payments
- **Customer-Product Analytics**: Deep linking between customer behavior and purchase patterns

### 🏢 **Complete Operational Framework**
- **HR Management**: Employee requests, profiles, and administrative tracking
- **IT Operations**: System logs, support tickets, and infrastructure monitoring  
- **Financial Operations**: Budget requests, procurement, and expense management
- **Project Management**: Tasks, meetings, and collaboration tracking
- **Knowledge Management**: Organizational knowledge base and documentation

### 🎯 **Advanced Customer Experience**
- **Multi-channel Campaigns**: Marketing campaigns across email, SMS, social media, and app notifications
- **Customer Engagement**: Detailed interaction tracking and engagement scoring
- **Loyalty Programs**: Rewards redemption and customer retention analytics
- **Event Management**: Workshop, training, and event participation tracking
- **Content Analytics**: Media asset performance and content interaction analysis

### 🔧 **Technical Excellence**
- **Realistic Data Volumes**: Appropriately sized datasets for each business function (200-10,000 rows)
- **Enhanced Data Relationships**: Complex foreign key relationships across all business domains
- **Business Logic Integration**: Authentic business processes and workflows represented in data
- **Scalable Architecture**: Modular design supporting easy expansion and customization

## Structure

- `generate_mock_data.py`: Main script to generate all datasets.
- `datasets/`: Output folder containing all generated CSV files, organized by business domain:
  - `TurningInformationIntoIntelligence/`: Customer analytics, product catalog, and network intelligence (10 datasets)
  - `ReinventingHowWorkGetsDone/`: Complete operational management including HR, IT, finance, and project management (11 datasets)
  - `RedefiningEngagementAndExperiences/`: Customer experience, marketing campaigns, and engagement analytics (9 datasets)


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

#### InternetUsage.csv
- **Description:** Internet usage logs by app category and device type.
- **Rows:** 10,000

#### SupportTickets.csv
- **Description:** Customer support ticket records with resolution tracking.
- **Rows:** 10,000

#### SocialSentiment.csv
- **Description:** Social media posts with engagement metrics.
- **Rows:** 10,000

#### NetworkPerformance.csv
- **Description:** Network performance metrics by region with tower load data.
- **Rows:** 10,000

#### CustomerDemographics.csv
- **Description:** Extended customer demographic information.
- **Rows:** 10,000 (matches customers)

### 2. Reinventing How Work Gets Done (11 Datasets)

#### Employees.csv
- **Description:** Employee information with department and salary details.
- **Rows:** 500
- **Example Row:**
   | employee_id | name       | department | role     | salary_bhd |
   |-------------|------------|------------|----------|------------|
   | E00001      | John Smith | IT         | Engineer | 2500.00    |

#### Projects.csv
- **Description:** Project information with status tracking and manager assignments.
- **Rows:** 200

#### Tasks.csv
- **Description:** Task assignments and completion tracking.
- **Rows:** 1,000

#### HRRequests.csv
- **Description:** HR-related requests from employees.
- **Rows:** 500
- **Example Row:**
   | request_id | employee_id | request_type | status   |
   |------------|-------------|--------------|----------|
   | HR00001    | E00005      | Leave        | Approved |

#### FinanceRequests.csv
- **Description:** Finance-related requests and budget approvals.
- **Rows:** 500
- **Example Row:**
   | request_id | employee_id | request_type | amount_bhd | status  |
   |------------|-------------|--------------|------------|---------|
   | FN00001    | E00010      | Purchase     | 1200.50    | Pending |

#### ITTickets.csv
- **Description:** IT support ticket records for employees.
- **Rows:** 500

#### Meetings.csv
- **Description:** Meeting records with participants and action items.
- **Rows:** 500

#### TaskAssignments.csv
- **Description:** Task assignments and completion tracking.
- **Rows:** 1,000

#### ProcurementRequests.csv
- **Description:** Procurement and vendor requests by departments.
- **Rows:** 500

#### SystemLogs.csv
- **Description:** System event logs across various platforms.
- **Rows:** 1,000

#### KnowledgeBase.csv
- **Description:** Knowledge base articles and documentation.
- **Rows:** 500

### 3. Redefining Engagement & Experiences (9 Datasets)

#### CustomerProfiles.csv
- **Description:** Customer engagement preferences and activity tracking.
- **Rows:** 5,000
- **Example Row:**
   | customer_id | preferred_channel | loyalty_score | historical_engagement |
   |-------------|------------------|---------------|----------------------|
   | C00001      | SMS              | 0.85          | 75                   |

#### EmployeeProfiles.csv
- **Description:** Employee engagement and training profiles.
- **Rows:** 500

#### Campaigns.csv
- **Description:** Marketing campaign details across multiple channels.
- **Rows:** 200
- **Example Row:**
   | campaign_id | name       | channel      | budget_bhd | target_segment |
   |-------------|------------|--------------|------------|----------------|
   | CM0001      | Campaign 1 | Email        | 25000.00   | Youth          |

#### MediaAssets.csv
- **Description:** Media assets used in campaigns with engagement scores.
- **Rows:** 500

#### FeedbackSurveys.csv
- **Description:** Customer and employee satisfaction surveys.
- **Rows:** 1,000

#### RewardsRedemptions.csv
- **Description:** Customer loyalty program reward redemptions.
- **Rows:** 1,000

#### EventParticipation.csv
- **Description:** Customer participation in company events.
- **Rows:** 1,000

#### ContentInteractions.csv
- **Description:** Customer interactions with digital content and campaigns.
- **Rows:** 2,000

#### EngagementHistory.csv (Note: Currently commented out in code)
- **Description:** Historical customer engagement tracking across channels.
- **Status:** Available but not currently generated

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

**Total: 30 CSV files** covering comprehensive business operations from customer analytics to internal operations and engagement tracking.

## Customization

- To change the number of rows, modify the `n` parameter values in the function calls within the `main()` function in `generate_mock_data.py`.
- To add new fields or modify data generation logic, update the respective generator functions (e.g., `generate_customers()`, `generate_hr_requests()`, `generate_campaigns()`, etc.).
- You can adjust the field values, categories, or business logic in the script to fit your specific needs.
- Dataset sizes are optimized for different business functions:
  - **Large datasets (10,000 rows)**: Core customer and product data for robust analytics
  - **Medium datasets (500-2,000 rows)**: Operational data like employees, tasks, and content interactions
  - **Small datasets (200-500 rows)**: Specialized data like projects, campaigns, and administrative records
- To enable/disable specific datasets, comment/uncomment the corresponding lines in the `main()` function.

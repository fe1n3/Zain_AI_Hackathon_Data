import os
import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()
Faker.seed(42)
random.seed(42)

# -----------------------------
# Utility functions
# -----------------------------
def ensure_folder(path: str):
    os.makedirs(path, exist_ok=True)

def save_csv(df, path: str):
    df.to_csv(path, index=False)
    print(f"✅ Saved {path}")

def random_date(start, end):
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds()))
    )

start_date = datetime(2020, 1, 1)
end_date = datetime(2025, 9, 30)

# -----------------------------
# Challenge 1: Turning Information into Intelligence
# -----------------------------
def generate_customers(n=1000):
    cities = ["Manama", "Muharraq", "Riffa", "Isa Town"]
    plan_types = ["Prepaid", "Postpaid"]
    data = []
    for i in range(1, n+1):
        churn = random.choice([0, 1])
        data.append({
            "customer_id": f"C{i:05d}",
            "age": random.randint(18, 65),
            "gender": random.choice(["M", "F"]),
            "city": random.choice(cities),
            "plan_type": random.choice(plan_types),
            "join_date": fake.date_between(start_date='-5y', end_date='today'),
            "churned": churn,
            "last_month_usage_gb": round(random.uniform(0, 50), 2),
            "complaints_count": random.randint(0, 5),
            "loyalty_score": round(random.uniform(0, 1), 2)
        })
    return pd.DataFrame(data)

def generate_product_catalog(n=50):
    product_types = ["Phone", "TV", "Laptop", "Watch", "Headphones", "Tablet"]
    brands = ["BrandA", "BrandB", "BrandC", "BrandD"]
    data = []
    for i in range(1, n+1):
        data.append({
            "product_id": i,
            "name": f"{random.choice(brands)} {random.choice(product_types)} {i}",
            "type": random.choice(product_types),
            "price_bhd": round(random.uniform(50, 3000), 2),
            "brand": random.choice(brands),
            "warranty_years": random.randint(1, 3),
            "release_year": random.randint(2018, 2025),
            "active": random.choice([0, 1])
        })
    return pd.DataFrame(data)

def generate_purchases(customers, products, n=5000):
    payment_types = ["Full", "Installment"]
    data = []
    for _ in range(n):
        cust = random.choice(customers)
        prod = random.choice(products)
        payment_type = random.choice(payment_types)
        installments = random.randint(2, 12) if payment_type == "Installment" else 1
        status = random.choice(["Pending", "Completed", "Failed"])
        remaining = round(prod["price_bhd"] - (prod["price_bhd"]/installments)*(installments-1),2) if payment_type=="Installment" else 0
        data.append({
            "purchase_id": fake.uuid4(),
            "customer_id": cust["customer_id"],
            "product_id": prod["product_id"],
            "payment_type": payment_type,
            "installments_total": installments,
            "remaining_amount": remaining,
            "status": status,
            "purchase_date": fake.date_between(start_date='-2y', end_date='today')
        })
    return pd.DataFrame(data)

def generate_financial_transactions(customers, n=5000):
    methods = ["Top-up", "Bill Payment", "Installment Payment", "Add-on"]
    data = []
    for _ in range(n):
        cust = random.choice(customers)
        data.append({
            "transaction_id": fake.uuid4(),
            "customer_id": cust["customer_id"],
            "amount_bhd": round(random.uniform(1, 2000), 2),
            "method": random.choice(methods),
            "date": fake.date_between(start_date='-2y', end_date='today'),
            "status": random.choice(["Success", "Failed", "Pending"]),
            "fraud_flag": random.choice([0, 1])
        })
    return pd.DataFrame(data)

def generate_calls(customers, n=5000):
    call_types = ["voice", "SMS", "data"]
    data = []
    for _ in range(n):
        cust = random.choice(customers)
        data.append({
            "call_id": fake.uuid4(),
            "customer_id": cust["customer_id"],
            "call_type": random.choice(call_types),
            "duration_min": round(random.uniform(0.5, 60), 2),
            "date": fake.date_between(start_date='-1y', end_date='today'),
            "cell_tower_id": f"T{random.randint(1,200):03d}"
        })
    return pd.DataFrame(data)

def generate_internet_usage(customers, n=5000):
    app_categories = ["Social Media", "Streaming", "Gaming", "Work", "Education"]
    devices = ["Mobile", "Tablet", "Laptop"]
    data = []
    for _ in range(n):
        cust = random.choice(customers)
        data.append({
            "usage_id": fake.uuid4(),
            "customer_id": cust["customer_id"],
            "date": fake.date_between(start_date='-1y', end_date='today'),
            "data_used_gb": round(random.uniform(0.1, 10), 2),
            "app_category": random.choice(app_categories),
            "device_type": random.choice(devices)
        })
    return pd.DataFrame(data)

def generate_support_tickets(customers, n=1000):
    issue_categories = ["Billing", "Network", "Service", "Technical"]
    priorities = ["Low", "Medium", "High"]
    data = []
    for _ in range(n):
        cust = random.choice(customers)
        data.append({
            "ticket_id": fake.uuid4(),
            "customer_id": cust["customer_id"],
            "issue_category": random.choice(issue_categories),
            "priority": random.choice(priorities),
            "date_opened": fake.date_between(start_date='-6mo', end_date='today'),
            "status": random.choice(["Open", "Resolved", "Pending"]),
            "resolution_time_hours": round(random.uniform(1, 72), 1)
        })
    return pd.DataFrame(data)

def generate_social_sentiment(customers, n=500):
    platforms = ["Twitter", "Instagram", "Facebook"]
    sentiments = ["Positive", "Neutral", "Negative"]
    topics = ["Network", "Offer", "Customer Service", "Event"]
    data = []
    for _ in range(n):
        cust = random.choice(customers)
        data.append({
            "post_id": fake.uuid4(),
            "customer_id": cust["customer_id"],
            "platform": random.choice(platforms),
            "sentiment": random.choice(sentiments),
            "topic": random.choice(topics),
            "date": fake.date_between(start_date='-1y', end_date='today'),
            "likes": random.randint(0, 500),
            "shares": random.randint(0, 200)
        })
    return pd.DataFrame(data)

def generate_network_performance(n=1000):
    regions = ["Manama", "Muharraq", "Riffa", "Isa Town"]
    data = []
    for i in range(n):
        data.append({
            "record_id": i+1,
            "region": random.choice(regions),
            "signal_strength": random.randint(1, 5),
            "latency_ms": random.randint(10, 200),
            "downtime_minutes": random.randint(0, 60),
            "date": random_date(start_date, end_date).date(),
            "tower_load_percentage": round(random.uniform(0, 100), 2)
        })
    return pd.DataFrame(data)

def generate_customer_demographics(customers):
    nationalities = ["Bahraini", "Expats-GCC", "Expats-Asia", "Expats-Other"]
    education_levels = ["High School", "Bachelor", "Master", "PhD"]
    data = []
    for cust in customers:
        data.append({
            "customer_id": cust["customer_id"],
            "income_bracket": random.choice(["Low", "Medium", "High"]),
            "household_size": random.randint(1, 7),
            "nationality": random.choice(nationalities),
            "education_level": random.choice(education_levels)
        })
    return pd.DataFrame(data)

# -----------------------------
# Challenge 2: Reinventing How Work Gets Done
# -----------------------------
def generate_employees(n=500):
    roles = ["Manager", "Engineer", "Sales", "HR", "Finance", "Support"]
    departments = ["IT", "Sales", "HR", "Finance", "Operations"]
    data = []
    for i in range(1, n+1):
        data.append({
            "employee_id": f"E{i:05d}",
            "name": fake.name(),
            "age": random.randint(22, 60),
            "gender": random.choice(["M", "F"]),
            "department": random.choice(departments),
            "role": random.choice(roles),
            "join_date": fake.date_between(start_date='-10y', end_date='today'),
            "salary_bhd": round(random.uniform(800, 8000), 2)
        })
    return pd.DataFrame(data)

def generate_projects(employees, n=200):
    project_status = ["Planning", "Active", "Completed", "On Hold"]
    data = []
    for i in range(1, n+1):
        manager = random.choice(employees)["employee_id"]
        data.append({
            "project_id": f"P{i:04d}",
            "name": f"Project {i}",
            "start_date": fake.date_between(start_date='-5y', end_date='today'),
            "end_date": fake.date_between(start_date='-1y', end_date='today'),
            "status": random.choice(project_status),
            "manager_id": manager
        })
    return pd.DataFrame(data)

def generate_tasks(projects, employees, n=1000):
    priorities = ["Low", "Medium", "High"]
    statuses = ["Open", "In Progress", "Completed", "Blocked"]
    data = []
    for i in range(1, n+1):
        project = random.choice(projects)["project_id"]
        assignee = random.choice(employees)["employee_id"]
        data.append({
            "task_id": f"T{i:05d}",
            "project_id": project,
            "assignee_id": assignee,
            "description": fake.sentence(),
            "priority": random.choice(priorities),
            "status": random.choice(statuses),
            "due_date": fake.date_between(start_date='-1y', end_date='today')
        })
    return pd.DataFrame(data)


def generate_customer_profiles(n=5000):
    cities = ["Manama", "Muharraq", "Riffa", "Isa Town"]
    data = []
    for i in range(1, n+1):
        data.append({
            "customer_id": f"C{i:05d}",
            "name": fake.name(),
            "age": random.randint(18, 65),
            "gender": random.choice(["M", "F"]),
            "city": random.choice(cities),
            "preferred_channel": random.choice(["SMS", "Email", "App", "Call"]),
            "loyalty_score": round(random.uniform(0, 1), 2),
            "historical_engagement": random.randint(0, 100)
        })
    return pd.DataFrame(data)

def generate_employee_profiles(n=500):
    roles = ["Manager", "Engineer", "Sales", "HR", "Finance", "Support"]
    departments = ["IT", "Sales", "HR", "Finance", "Operations"]
    data = []
    for i in range(1, n+1):
        data.append({
            "employee_id": f"E{i:05d}",
            "name": fake.name(),
            "age": random.randint(22, 60),
            "gender": random.choice(["M", "F"]),
            "role": random.choice(roles),
            "department": random.choice(departments),
            "training_completed": random.randint(0, 20),
            "engagement_score": round(random.uniform(0, 1), 2)
        })
    return pd.DataFrame(data)

def generate_campaigns(n=200):
    channels = ["Email", "SMS", "Social Media", "App Push", "Website"]
    data = []
    for i in range(1, n+1):
        data.append({
            "campaign_id": f"CM{i:04d}",
            "name": f"Campaign {i}",
            "start_date": fake.date_between(start_date='-2y', end_date='today'),
            "end_date": fake.date_between(start_date='-1y', end_date='today'),
            "channel": random.choice(channels),
            "budget_bhd": round(random.uniform(1000, 50000), 2),
            "target_segment": random.choice(["Youth", "Families", "Professionals", "Students"])
        })
    return pd.DataFrame(data)

def generate_feedback_surveys(n=1000):
    categories = ["Customer", "Employee"]
    topics = ["Satisfaction", "Net Promoter Score", "Experience", "Support"]
    ratings = [1, 2, 3, 4, 5]
    data = []
    for i in range(1, n+1):
        data.append({
            "survey_id": f"S{i:05d}",
            "subject_id": f"C{random.randint(1,5000):05d}" if random.random() > 0.5 else f"E{random.randint(1,500):05d}",
            "category": random.choice(categories),
            "topic": random.choice(topics),
            "rating": random.choice(ratings),
            "date": fake.date_between(start_date='-2y', end_date='today')
        })
    return pd.DataFrame(data)

def generate_rewards_redemptions(n=1000):
    rewards = ["Discount", "Voucher", "Free Data", "Gift Item"]
    data = []
    for i in range(1, n+1):
        data.append({
            "redemption_id": f"R{i:05d}",
            "customer_id": f"C{random.randint(1,5000):05d}",
            "reward_type": random.choice(rewards),
            "points_spent": random.randint(10, 500),
            "date": fake.date_between(start_date='-2y', end_date='today')
        })
    return pd.DataFrame(data)

def generate_event_participation(n=1000):
    events = ["Workshop", "Hackathon", "Webinar", "Training Session"]
    data = []
    for i in range(1, n+1):
        data.append({
            "participation_id": f"EV{i:05d}",
            "customer_id": f"C{random.randint(1,5000):05d}",
            "event_type": random.choice(events),
            "event_date": fake.date_between(start_date='-2y', end_date='today'),
            "attendance": random.choice(["Attended", "Registered", "No-show"])
        })
    return pd.DataFrame(data)

def generate_content_interactions(n=2000):
    actions = ["View", "Click", "Like", "Share"]
    data = []
    for i in range(1, n+1):
        data.append({
            "interaction_id": f"CI{i:05d}",
            "customer_id": f"C{random.randint(1,5000):05d}",
            "campaign_id": f"CM{random.randint(1,200):04d}",
            "action": random.choice(actions),
            "date": fake.date_between(start_date='-2y', end_date='today')
        })
    return pd.DataFrame(data)


# -----------------------------
# Challenge 3: Reinventing How Work Gets Done
# -----------------------------
def generate_hr_requests(n=500):
    request_types = ["Leave", "Onboarding", "Policy Update", "Other"]
    statuses = ["Pending", "Approved", "Rejected"]
    data = []
    for i in range(1, n+1):
        data.append({
            "request_id": f"HR{i:05d}",
            "employee_id": f"E{random.randint(1,500):05d}",
            "request_type": random.choice(request_types),
            "date_submitted": fake.date_between(start_date='-2y', end_date='today'),
            "status": random.choice(statuses)
        })
    return pd.DataFrame(data)

def generate_finance_requests(n=500):
    request_types = ["Purchase", "Expense Claim", "Budget Approval"]
    statuses = ["Pending", "Approved", "Rejected"]
    data = []
    for i in range(1, n+1):
        data.append({
            "request_id": f"FN{i:05d}",
            "employee_id": f"E{random.randint(1,500):05d}",
            "request_type": random.choice(request_types),
            "amount_bhd": round(random.uniform(100, 10000), 2),
            "date_submitted": fake.date_between(start_date='-2y', end_date='today'),
            "status": random.choice(statuses)
        })
    return pd.DataFrame(data)

def generate_it_tickets(n=500):
    categories = ["Hardware", "Software", "Network", "Other"]
    priorities = ["Low", "Medium", "High"]
    statuses = ["Open", "In Progress", "Closed"]
    data = []
    for i in range(1, n+1):
        data.append({
            "ticket_id": f"IT{i:05d}",
            "employee_id": f"E{random.randint(1,500):05d}",
            "category": random.choice(categories),
            "priority": random.choice(priorities),
            "status": random.choice(statuses),
            "date_reported": fake.date_between(start_date='-2y', end_date='today')
        })
    return pd.DataFrame(data)

def generate_meetings(n=500):
    data = []
    for i in range(1, n+1):
        participants = [f"E{random.randint(1,500):05d}" for _ in range(random.randint(2,6))]
        data.append({
            "meeting_id": f"M{i:05d}",
            "topic": fake.sentence(nb_words=5),
            "date": fake.date_between(start_date='-2y', end_date='today'),
            "participants": ",".join(participants),
            "action_items": fake.sentence(nb_words=10)
        })
    return pd.DataFrame(data)

def generate_task_assignments(n=1000):
    statuses = ["Open", "In Progress", "Completed", "Blocked"]
    priorities = ["Low", "Medium", "High"]
    data = []
    for i in range(1, n+1):
        data.append({
            "task_id": f"T{i:05d}",
            "employee_id": f"E{random.randint(1,500):05d}",
            "project_id": f"P{random.randint(1,200):04d}",
            "description": fake.sentence(),
            "priority": random.choice(priorities),
            "status": random.choice(statuses),
            "due_date": fake.date_between(start_date='-1y', end_date='today')
        })
    return pd.DataFrame(data)

def generate_procurement_requests(n=500):
    items = ["Laptop", "Phone", "Software License", "Furniture"]
    statuses = ["Pending", "Approved", "Rejected"]
    data = []
    for i in range(1, n+1):
        data.append({
            "request_id": f"PR{i:05d}",
            "department": random.choice(["IT", "HR", "Finance", "Operations"]),
            "item": random.choice(items),
            "quantity": random.randint(1, 50),
            "date_submitted": fake.date_between(start_date='-2y', end_date='today'),
            "status": random.choice(statuses)
        })
    return pd.DataFrame(data)

def generate_system_logs(n=1000):
    events = ["Login", "Logout", "Error", "Update", "Access"]
    severities = ["Low", "Medium", "High", "Critical"]
    data = []
    for i in range(1, n+1):
        data.append({
            "log_id": f"SL{i:05d}",
            "system": random.choice(["ERP", "CRM", "Network", "InternalApp"]),
            "event": random.choice(events),
            "severity": random.choice(severities),
            "timestamp": fake.date_time_between(start_date='-2y', end_date='now')
        })
    return pd.DataFrame(data)

# -----------------------------know
# Main runner
# -----------------------------
def main():
    base_dir = "datasets"
    ensure_folder(base_dir)

    # ----- Challenge 1: Turning Information into Intelligence -----
    c1_dir = os.path.join(base_dir, "TurningInformationIntoIntelligence")
    ensure_folder(c1_dir)

    customers_df = generate_customers(10000)
    save_csv(customers_df, os.path.join(c1_dir, "Customers.csv"))

    product_df = generate_product_catalog(10000)
    save_csv(product_df, os.path.join(c1_dir, "ProductCatalog.csv"))

    purchases_df = generate_purchases(customers_df.to_dict(orient="records"), product_df.to_dict(orient="records"), 10000)
    save_csv(purchases_df, os.path.join(c1_dir, "Purchases.csv"))

    transactions_df = generate_financial_transactions(customers_df.to_dict(orient="records"), 10000)
    save_csv(transactions_df, os.path.join(c1_dir, "FinancialTransactions.csv"))

    calls_df = generate_calls(customers_df.to_dict(orient="records"), 10000)
    save_csv(calls_df, os.path.join(c1_dir, "Calls.csv"))

    internet_df = generate_internet_usage(customers_df.to_dict(orient="records"), 10000)
    save_csv(internet_df, os.path.join(c1_dir, "InternetUsage.csv"))

    tickets_df = generate_support_tickets(customers_df.to_dict(orient="records"), 10000)
    save_csv(tickets_df, os.path.join(c1_dir, "SupportTickets.csv"))

    sentiment_df = generate_social_sentiment(customers_df.to_dict(orient="records"), 10000)
    save_csv(sentiment_df, os.path.join(c1_dir, "SocialSentiment.csv"))

    network_df = generate_network_performance(10000)
    save_csv(network_df, os.path.join(c1_dir, "NetworkPerformance.csv"))

    demographics_df = generate_customer_demographics(customers_df.to_dict(orient="records"))
    save_csv(demographics_df, os.path.join(c1_dir, "CustomerDemographics.csv"))

    # ----- Challenge 2: Reinventing How Work Gets Done -----
    c2_dir = os.path.join(base_dir, "ReinventingHowWorkGetsDone")
    ensure_folder(c2_dir)

    employees_df = generate_employees(10000)
    save_csv(employees_df, os.path.join(c2_dir, "Employees.csv"))

    projects_df = generate_projects(employees_df.to_dict(orient="records"), 10000)
    save_csv(projects_df, os.path.join(c2_dir, "Projects.csv"))

    tasks_df = generate_tasks(projects_df.to_dict(orient="records"), employees_df.to_dict(orient="records"), 10000)
    save_csv(tasks_df, os.path.join(c2_dir, "Tasks.csv"))

    save_csv(generate_hr_requests(10000), os.path.join(c2_dir, "HRRequests.csv"))
    save_csv(generate_finance_requests(10000), os.path.join(c2_dir, "FinanceRequests.csv"))
    save_csv(generate_it_tickets(10000), os.path.join(c2_dir, "ITTickets.csv"))
    save_csv(generate_meetings(10000), os.path.join(c2_dir, "Meetings.csv"))
    save_csv(generate_task_assignments(10000), os.path.join(c2_dir, "TaskAssignments.csv"))
    save_csv(generate_procurement_requests(10000), os.path.join(c2_dir, "ProcurementRequests.csv"))
    save_csv(generate_system_logs(10000), os.path.join(c2_dir, "SystemLogs.csv"))

    # ----- Challenge 3: Redefining Engagement & Experiences -----
    c3_dir = os.path.join(base_dir, "RedefiningEngagementAndExperiences")
    ensure_folder(c3_dir)

    save_csv(generate_customer_profiles(10000), os.path.join(c3_dir, "CustomerProfiles.csv"))
    save_csv(generate_employee_profiles(10000), os.path.join(c3_dir, "EmployeeProfiles.csv"))
    save_csv(generate_campaigns(10000), os.path.join(c3_dir, "Campaigns.csv"))
    save_csv(generate_feedback_surveys(10000), os.path.join(c3_dir, "FeedbackSurveys.csv"))
    save_csv(generate_rewards_redemptions(10000), os.path.join(c3_dir, "RewardsRedemptions.csv"))
    save_csv(generate_event_participation(10000), os.path.join(c3_dir, "EventParticipation.csv"))
    save_csv(generate_content_interactions(10000), os.path.join(c3_dir, "ContentInteractions.csv"))


if __name__ == "__main__":
    main()

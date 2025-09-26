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

# -----------------------------
# Challenge 3: Redefining Engagement & Experiences
# -----------------------------
def generate_engagement_history(customers, n=5000):
    channels = ["Email", "SMS", "App Notification", "Call"]
    responses = ["Clicked", "Opened", "Ignored", "Converted"]
    data = []
    for _ in range(n):
        cust = random.choice(customers)
        data.append({
            "engagement_id": fake.uuid4(),
            "customer_id": cust["customer_id"],
            "campaign": f"Campaign {random.randint(1,50)}",
            "channel": random.choice(channels),
            "response": random.choice(responses),
            "date": fake.date_between(start_date='-1y', end_date='today')
        })
    return pd.DataFrame(data)

# -----------------------------
# Main runner
# -----------------------------
def main():
    base_dir = "datasets"
    ensure_folder(base_dir)

    # ----- Challenge 1 -----
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

    # ----- Challenge 2 -----
    c2_dir = os.path.join(base_dir, "ReinventingHowWorkGetsDone")
    ensure_folder(c2_dir)

    employees_df = generate_employees(10000)
    save_csv(employees_df, os.path.join(c2_dir, "Employees.csv"))

    projects_df = generate_projects(employees_df.to_dict(orient="records"), 10000)
    save_csv(projects_df, os.path.join(c2_dir, "Projects.csv"))

    tasks_df = generate_tasks(projects_df.to_dict(orient="records"), employees_df.to_dict(orient="records"), 10000)
    save_csv(tasks_df, os.path.join(c2_dir, "Tasks.csv"))

    # ----- Challenge 3 -----
    c3_dir = os.path.join(base_dir, "RedefiningEngagementAndExperiences")
    ensure_folder(c3_dir)

    engagement_df = generate_engagement_history(customers_df.to_dict(orient="records"), 10000)
    save_csv(engagement_df, os.path.join(c3_dir, "EngagementHistory.csv"))

if __name__ == "__main__":
    main()

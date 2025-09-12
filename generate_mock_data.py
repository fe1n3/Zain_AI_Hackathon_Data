import os
import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta
import numpy as np

fake = Faker()
Faker.seed(42)
random.seed(42)

# Base folder
base_folder = "ZainAI_MockData"
os.makedirs(base_folder, exist_ok=True)

def random_date(start, end):
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())),
    )

start_date = datetime(2020, 1, 1)
end_date = datetime(2025, 9, 30)


# ---------------------------
# 1️⃣ Turning Information into Intelligence
# ---------------------------
folder1 = os.path.join(base_folder, "Turning_Information_into_Intelligence")
os.makedirs(folder1, exist_ok=True)

# a. Customers.csv
customers = []
cities = ["Manama", "Muharraq", "Riffa", "Isa Town"]
plan_types = ["Prepaid", "Postpaid"]
for i in range(10000):
    customers.append({
        "customer_id": f"C{i+1:03d}",
        "age": random.randint(18, 65),
        "gender": random.choice(["M", "F"]),
        "city": random.choice(cities),
        "plan_type": random.choice(plan_types),
        "join_date": fake.date_between(start_date='-5y', end_date='today'),
        "churned": random.choice([0, 1]),
        "last_month_usage_gb": round(random.uniform(0, 50), 2),
        "complaints_count": random.randint(0, 5)
    })
pd.DataFrame(customers).to_csv(os.path.join(folder1, "1a_Customers.csv"), index=False)

# b. Calls.csv
calls = []
call_types = ["voice", "SMS", "data"]
for i in range(10000):
    calls.append({
        "call_id": f"CL{i+1:03d}",
        "customer_id": f"C{random.randint(1, 100):03d}",
        "call_type": random.choice(call_types),
        "duration_min": round(random.uniform(0.5, 60), 2),
        "date": fake.date_between(start_date='-1y', end_date='today')
    })
pd.DataFrame(calls).to_csv(os.path.join(folder1, "1b_Calls.csv"), index=False)

# c. InternetUsage.csv
internet_usage = []
app_categories = ["Social Media", "Streaming", "Gaming", "Work", "Education"]
for i in range(10000):
    internet_usage.append({
        "usage_id": f"U{i+1:03d}",
        "customer_id": f"C{random.randint(1, 100):03d}",
        "date": fake.date_between(start_date='-1y', end_date='today'),
        "data_used_gb": round(random.uniform(0.1, 10), 2),
        "app_category": random.choice(app_categories)
    })
pd.DataFrame(internet_usage).to_csv(os.path.join(folder1, "1c_InternetUsage.csv"), index=False)

# d. SupportTickets.csv
issue_categories = ["Billing", "Network", "Service", "Technical"]
priorities = ["Low", "Medium", "High"]
support_tickets = []
for i in range(10000):
    support_tickets.append({
        "ticket_id": f"T{i+1:03d}",
        "customer_id": f"C{random.randint(1, 100):03d}",
        "issue_category": random.choice(issue_categories),
        "priority": random.choice(priorities),
        "date_opened": fake.date_between(start_date='-6mo', end_date='today'),
        "status": random.choice(["Open", "Resolved", "Pending"])
    })
pd.DataFrame(support_tickets).to_csv(os.path.join(folder1, "1d_SupportTickets.csv"), index=False)

# e. SocialSentiment.csv
platforms = ["Twitter", "Instagram", "Facebook"]
sentiments = ["Positive", "Neutral", "Negative"]
topics = ["Network", "Offer", "Customer Service", "Event"]
social_sentiment = []
for i in range(10000):
    social_sentiment.append({
        "post_id": f"S{i+1:03d}",
        "platform": random.choice(platforms),
        "sentiment": random.choice(sentiments),
        "topic": random.choice(topics),
        "date": fake.date_between(start_date='-1y', end_date='today')
    })
pd.DataFrame(social_sentiment).to_csv(os.path.join(folder1, "1e_SocialSentiment.csv"), index=False)

# f. FinancialTransactions.csv
transactions = []
for i in range(10000):
    transactions.append({
        "transaction_id": f"TX{i+1:05}",
        "customer_id": f"C{random.randint(1, 500):05}",
        "amount": round(random.uniform(1, 200), 2),
        "method": random.choice(["Top-up", "Bill Payment", "Roaming", "Add-on"]),
        "date": random_date(start_date, end_date).date(),
        "status": random.choice(["Success", "Failed", "Pending"])
    })
pd.DataFrame(transactions).to_csv(os.path.join(folder1, "1f_FinancialTransactions.csv"), index=False)

# g. NetworkPerformance.csv
network = []
for i in range(10000):
    network.append({
        "record_id": f"NP{i+1:05}",
        "region": random.choice(["Manama", "Muharraq", "Riffa", "Isa Town"]),
        "signal_strength": random.randint(1, 5),
        "latency_ms": random.randint(10, 200),
        "downtime_minutes": random.randint(0, 60),
        "date": random_date(start_date, end_date).date()
    })
pd.DataFrame(network).to_csv(os.path.join(folder1, "1g_NetworkPerformance.csv"), index=False)

# h. CustomerDemographics.csv
demographics = []
for i in range(10000):
    demographics.append({
        "customer_id": f"C{i+1:05}",
        "income_bracket": random.choice(["Low", "Medium", "High"]),
        "household_size": random.randint(1, 7),
        "nationality": random.choice(["Bahraini", "Expats-GCC", "Expats-Asia", "Expats-Other"])
    })
pd.DataFrame(demographics).to_csv(os.path.join(folder1, "1h_CustomerDemographics.csv"), index=False)

# i. ProductCatalog.csv
products = []
for i in range(10000):
    products.append({
        "product_id": f"P{i+1:03}",
        "name": random.choice(["Unlimited Social", "Roaming Pack", "Family Bundle", "Student Offer"]),
        "price_bhd": round(random.uniform(1, 30), 2),
        "category": random.choice(["Data", "Voice", "Combo"]),
        "active": random.choice([0, 1])
    })
pd.DataFrame(products).to_csv(os.path.join(folder1, "1i_ProductCatalog.csv"), index=False)


# ---------------------------
# 2️⃣ Redefining Engagement & Experiences
# ---------------------------
folder2 = os.path.join(base_folder, "Redefining_Engagement_and_Experiences")
os.makedirs(folder2, exist_ok=True)

# a. CustomerProfiles.csv
interests_list = ["Gaming", "Streaming", "Finance", "Sports", "News", "Travel"]
channels = ["Email", "WhatsApp", "SMS", "App Notification"]
customer_profiles = []
for i in range(10000):
    customer_profiles.append({
        "customer_id": f"C{i+1:03d}",
        "interests": ", ".join(random.sample(interests_list, 2)),
        "preferred_channel": random.choice(channels),
        "last_engagement_date": fake.date_between(start_date='-3mo', end_date='today')
    })
pd.DataFrame(customer_profiles).to_csv(os.path.join(folder2, "2a_CustomerProfiles.csv"), index=False)

# b. EmployeeProfiles.csv
departments = ["Marketing", "IT", "HR", "Finance", "Operations"]
roles = ["Manager", "Analyst", "Executive", "Intern"]
learning_modes = ["Video", "Text", "Interactive"]
employee_profiles = []
for i in range(10000):
    employee_profiles.append({
        "employee_id": f"E{i+1:03d}",
        "department": random.choice(departments),
        "role": random.choice(roles),
        "completed_trainings": random.randint(0, 10),
        "preferred_learning_mode": random.choice(learning_modes)
    })
pd.DataFrame(employee_profiles).to_csv(os.path.join(folder2, "2b_EmployeeProfiles.csv"), index=False)

# c. Campaigns.csv
campaign_types = ["Email", "SMS", "Push Notification"]
campaigns = []
for i in range(10000):
    campaigns.append({
        "campaign_id": f"CM{i+1:03d}",
        "type": random.choice(campaign_types),
        "target_audience": ", ".join([f"C{random.randint(1,100):03d}" for _ in range(5)]),
        "engagement_rate": round(random.uniform(0.05, 0.7), 2),
        "date_sent": fake.date_between(start_date='-3mo', end_date='today')
    })
pd.DataFrame(campaigns).to_csv(os.path.join(folder2, "2c_Campaigns.csv"), index=False)

# d. MediaAssets.csv
asset_types = ["Image", "Video", "Audio"]
media_assets = []
for i in range(10000):
    media_assets.append({
        "asset_id": f"M{i+1:03d}",
        "type": random.choice(asset_types),
        "topic": random.choice(topics),
        "engagement_score": round(random.uniform(0, 1), 2)
    })
pd.DataFrame(media_assets).to_csv(os.path.join(folder2, "2d_MediaAssets.csv"), index=False)

# e. FeedbackSurveys.csv
surveys = []
for i in range(10000):
    surveys.append({
        "survey_id": f"SV{i+1:04}",
        "customer_id": f"C{random.randint(1, 500):05}",
        "score": random.randint(1, 5),
        "comment": random.choice(["Great service", "Network issue", "Too expensive", "Happy with Zain"]),
        "date": random_date(start_date, end_date).date()
    })
pd.DataFrame(surveys).to_csv(os.path.join(folder2, "2e_FeedbackSurveys.csv"), index=False)

# f. RewardsRedemptions.csv
rewards = []
for i in range(10000):
    rewards.append({
        "redemption_id": f"RW{i+1:04}",
        "customer_id": f"C{random.randint(1, 500):05}",
        "reward_type": random.choice(["Data Voucher", "Discount Coupon", "Event Ticket"]),
        "date": random_date(start_date, end_date).date()
    })
pd.DataFrame(rewards).to_csv(os.path.join(folder2, "2f_RewardsRedemptions.csv"), index=False)

# g. EventParticipation.csv
events = []
for i in range(10000):
    events.append({
        "event_id": f"EV{i+1:03}",
        "customer_id": f"C{random.randint(1, 500):05}",
        "event_name": random.choice(["Hackathon", "Football Tournament", "Music Festival", "Workshop"]),
        "attended": random.choice([0, 1]),
        "date": random_date(start_date, end_date).date()
    })
pd.DataFrame(events).to_csv(os.path.join(folder2, "2g_EventParticipation.csv"), index=False)

# h. ContentInteractions.csv
interactions = []
for i in range(10000):
    interactions.append({
        "interaction_id": f"IN{i+1:05}",
        "customer_id": f"C{random.randint(1, 500):05}",
        "content_id": f"M{random.randint(1, 200):03}",
        "type": random.choice(["Click", "View", "Like", "Share"]),
        "date": random_date(start_date, end_date).date()
    })
pd.DataFrame(interactions).to_csv(os.path.join(folder2, "2h_ContentInteractions.csv"), index=False)

# ---------------------------
# 3️⃣ Reinventing How Work Gets Done
# ---------------------------
folder3 = os.path.join(base_folder, "Reinventing_How_Work_Gets_Done")
os.makedirs(folder3, exist_ok=True)

# a. HRRequests.csv
hr_request_types = ["Leave", "Onboarding", "Promotion"]
hr_requests = []
for i in range(10000):
    hr_requests.append({
        "request_id": f"HR{i+1:03d}",
        "employee_id": f"E{random.randint(1,20):03d}",
        "type": random.choice(hr_request_types),
        "date_submitted": fake.date_between(start_date='-6mo', end_date='today'),
        "status": random.choice(["Pending", "Approved", "Rejected"])
    })
pd.DataFrame(hr_requests).to_csv(os.path.join(folder3, "3a_HRRequests.csv"), index=False)

# b. FinanceRequests.csv
finance_request_types = ["Purchase", "Invoice", "Reimbursement", "Software License"]
finance_requests = []
for i in range(10000):
    finance_requests.append({
        "request_id": f"F{i+1:03d}",
        "department": random.choice(departments),
        "type": random.choice(finance_request_types),
        "amount": round(random.uniform(50, 5000), 2),
        "status": random.choice(["Pending", "Approved", "Rejected"]),
        "date_submitted": fake.date_between(start_date='-6mo', end_date='today')
    })
pd.DataFrame(finance_requests).to_csv(os.path.join(folder3, "3b_FinanceRequests.csv"), index=False)

# c. ITTickets.csv
issue_types = ["Laptop Issue", "VPN Setup", "Email Issue", "Software Bug"]
priorities = ["Low", "Medium", "High"]
it_tickets = []
for i in range(10000):
    it_tickets.append({
        "ticket_id": f"IT{i+1:03d}",
        "employee_id": f"E{random.randint(1,20):03d}",
        "issue_type": random.choice(issue_types),
        "priority": random.choice(priorities),
        "date_opened": fake.date_between(start_date='-6mo', end_date='today'),
        "status": random.choice(["Open", "Resolved", "Pending"])
    })
pd.DataFrame(it_tickets).to_csv(os.path.join(folder3, "3c_ITTickets.csv"), index=False)

# d. Meetings.csv
meetings = []
for i in range(10000):
    participants = ", ".join([f"E{random.randint(1,20):03d}" for _ in range(random.randint(1,3))])
    meetings.append({
        "meeting_id": f"MT{i+1:03d}",
        "participants": participants,
        "transcript": fake.sentence(nb_words=10) + " Action: " + fake.sentence(nb_words=5),
        "date": fake.date_between(start_date='-6mo', end_date='today')
    })
pd.DataFrame(meetings).to_csv(os.path.join(folder3, "3d_Meetings.csv"), index=False)

# e. TaskAssignments.csv
tasks = []
for i in range(10000):
    tasks.append({
        "task_id": f"TK{i+1:04}",
        "employee_id": f"E{random.randint(1, 200):03}",
        "description": random.choice(["Prepare report", "Check network logs", "Review contracts", "Test system"]),
        "deadline": random_date(start_date, end_date).date(),
        "status": random.choice(["Pending", "Completed", "Overdue"])
    })
pd.DataFrame(tasks).to_csv(os.path.join(folder3, "3e_TaskAssignments.csv"), index=False)

# f. ProcurementRequests.csv
procurement = []
for i in range(10000):
    procurement.append({
        "request_id": f"PR{i+1:04}",
        "department": random.choice(["IT", "HR", "Finance", "Marketing"]),
        "vendor": random.choice(["VendorA", "VendorB", "VendorC"]),
        "amount_bhd": round(random.uniform(100, 5000), 2),
        "status": random.choice(["Pending", "Approved", "Rejected"]),
        "date": random_date(start_date, end_date).date()
    })
pd.DataFrame(procurement).to_csv(os.path.join(folder3, "3f_ProcurementRequests.csv"), index=False)

# g. SystemLogs.csv
logs = []
for i in range(10000):
    logs.append({
        "log_id": f"LG{i+1:05}",
        "timestamp": random_date(start_date, end_date),
        "system": random.choice(["HRMS", "Billing", "CRM", "Network"]),
        "event": random.choice(["Login", "Error", "Update", "Timeout"]),
        "severity": random.choice(["Low", "Medium", "High", "Critical"])
    })
pd.DataFrame(logs).to_csv(os.path.join(folder3, "3g_SystemLogs.csv"), index=False)

# h. KnowledgeBase.csv
kb = []
topics = ["Billing issue", "SIM replacement", "Network troubleshooting", "HR policy", "IT access"]
for i in range(10000):
    kb.append({
        "article_id": f"KB{i+1:03}",
        "title": random.choice(topics),
        "content": f"This is a guide for {random.choice(topics)}",
        "tags": random.choice(topics).split()
    })
pd.DataFrame(kb).to_csv(os.path.join(folder3, "3h_KnowledgeBase.csv"), index=False)

print(f"Mock datasets created in folder: {base_folder}")

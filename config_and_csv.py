import os
import csv

# ===== Configuration =====
LEADS_CSV = 'leads.csv'
FOLLOW_UP_DELAY = 20  # seconds for testing
MAX_FOLLOWUPS = 1

# ===== CSV Handling =====
def init_csv():
    if not os.path.exists(LEADS_CSV):
        with open(LEADS_CSV, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['lead_id', 'name', 'age', 'country', 'interest', 'status'])

def save_to_csv(lead_id, name, age, country, interest, status):
    with open(LEADS_CSV, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([lead_id, name, age, country, interest, status])

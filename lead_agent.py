import threading
from datetime import datetime
from config_and_csv import save_to_csv

input_lock = threading.Lock()

class LeadSession:
    def __init__(self, lead_id, name):
        self.lead_id = lead_id
        self.name = name
        self.age = None
        self.country = None
        self.interest = None
        self.status = 'pending'
        self.last_interaction_time = datetime.now()
        self.followup_count = 0

    def update_interaction_time(self):
        self.last_interaction_time = datetime.now()

def get_input_threadsafe(prompt):
    with input_lock:
        return input(prompt + '\n> ').strip()

def start_conversation(lead_id, name, lead_sessions):
    session = LeadSession(lead_id, name)
    lead_sessions[lead_id] = session

    print(f"[Agent -> {name}]: Hey {name}, thank you for filling out the form. I'd like to gather some information from you. Is that okay?")
    consent = get_input_threadsafe(f"[You ({name})]")
    session.update_interaction_time()

    if consent.lower() not in ['yes', 'y', 'okay', 'sure']:
        session.status = 'no_response'
        save_to_csv(session.lead_id, session.name, '', '', '', session.status)
        print(f"[Agent -> {name}]: Alright, no problem. Have a great day!")
        return

    session.age = get_input_threadsafe(f"[Agent to {name}]: What is your age?")
    session.update_interaction_time()

    session.country = get_input_threadsafe(f"[Agent to {name}]: Which country are you from?")
    session.update_interaction_time()

    session.interest = get_input_threadsafe(f"[Agent to {name}]: What product or service are you interested in?")
    session.update_interaction_time()

    session.status = 'secured'
    save_to_csv(session.lead_id, session.name, session.age, session.country, session.interest, session.status)
    print(f"[Agent -> {name}]: Thank you! We've recorded your information.")

import threading
import time
from datetime import datetime
from config_and_csv import init_csv, save_to_csv, FOLLOW_UP_DELAY, MAX_FOLLOWUPS
from lead_agent import start_conversation, LeadSession

lead_sessions = {}

def follow_up_monitor():
    while True:
        now = datetime.now()
        for session in list(lead_sessions.values()):
            if session.status != 'pending':
                continue
            elapsed = (now - session.last_interaction_time).total_seconds()
            if elapsed > FOLLOW_UP_DELAY:
                if session.followup_count >= MAX_FOLLOWUPS:
                    session.status = 'no_response'
                    save_to_csv(session.lead_id, session.name, '', '', '', session.status)
                    print(f"[Agent -> {session.name}]: No response received. Ending session.")
                    continue
                print(f"[Agent -> {session.name}]: Just checking in to see if you're still interested. Let me know when you're ready to continue.")
                session.followup_count += 1
                session.update_interaction_time()
        time.sleep(1)

if __name__ == '__main__':
    init_csv()
    threading.Thread(target=follow_up_monitor, daemon=True).start()

    leads = [('001', 'Alice'), ('002', 'Bob'), ('003', 'Charlie')]
    for lead_id, name in leads:
        threading.Thread(target=start_conversation, args=(lead_id, name, lead_sessions)).start()
        time.sleep(7.5)



---

```markdown
# 🤖 Conversational Sales Agent using Google ADK (Python)

This project demonstrates a conversational sales agent built using **Python** and simulating the behavior of Google's **Agent Development Kit (ADK)**. It supports concurrent conversations with multiple leads, collects important information, sends follow-ups, and saves the data into a CSV file.

---

## ✅ Features

- Automatically starts a conversation when a lead fills out a form
- Collects:
  - Age
  - Country
  - Product or service of interest
- Handles multiple conversations concurrently using `threading`
- Sends a **follow-up** if the lead is unresponsive
- Saves lead data to `leads.csv`
- Simulates 24-hour timeout with **1.5 seconds** for demonstration

---

## 🗂️ File Structure

```

project/
├── main.py              # Entry point to run the agent and simulation
├── lead\_agent.py        # Logic for the conversational agent
├── config\_and\_csv.py    # CSV writing logic and configuration
├── leads.csv            # Stores all collected lead data
└── README.md            # Documentation

````

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/conversational-sales-agent.git
cd conversational-sales-agent
````

### 2. (Optional) Create a virtual environment and activate it

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Run the simulation

```bash
python main.py
```

---

## 🧪 How It Works

* The simulation starts automatically.

* Each lead is assigned a unique `lead_id`.

* The agent sends:

  > "Hey \[Lead Name], thank you for filling out the form. I'd like to gather some information from you. Is that okay?"

* If the lead says "yes", it asks:

  1. What is your age?
  2. Which country are you from?
  3. What product or service are you interested in?

* If no response within 1.5 seconds, it sends a follow-up:

  > "Just checking in to see if you're still interested. Let me know when you're ready to continue."

* Responses are saved in `leads.csv`.

---

## 📁 Sample Output (`leads.csv`)

| lead\_id | name    | age | country  | interest           | status  |
| -------- | ------- | --- | -------- | ------------------ | ------- |
| 1        | Alice   | 20  | US       | Mobile Development | secured |
| 2        | Bob     | 30  | UAE      | AI Development     | secured |
| 3        | Charlie | 40  | UK       | Data Analyst       | secured |

> Status can be `secured`, `no_response`, or `pending`

---

## 📹 Demo Video

🎥 \[Insert your demo video link here – YouTube / Google Drive]

* Shows concurrent lead interactions
* Follow-up for unresponsive users
* Data saved to CSV
* Code explained briefly

---

## 🧾 Design Highlights

* **Multi-threading** used to handle each lead independently
* Context is preserved using per-thread logic
* CSV file handles persistence with headers:

  * `lead_id`, `name`, `age`, `country`, `interest`, `status`
* Timeout simulated with `time.sleep(1.5)` instead of 24 hours

---

## 🧪 Test Scenarios

| Scenario                      | Expected Result                            |
| ----------------------------- | ------------------------------------------ |
| User replies "yes"            | Agent collects and stores data             |
| User replies "no"             | Agent ends conversation with `no_response` |
| User doesn't reply in time    | Follow-up message is sent                  |
| User doesn’t reply even after | Session ends, `no_response` status saved   |
| Multiple leads simultaneously | Each handled independently                 |

---

## 📋 Requirements

Only standard Python libraries are used:

* `threading`
* `csv`
* `time`

No external installations needed.

---

## 🧑‍💻 Author

**Your Name**
GitHub: \[[https://github.com/your-username](https://github.com/your-username)]
Email: \[[your-email@example.com](mailto:your-email@example.com)]

---

## 📄 License

This project is shared for educational purposes under the [MIT License](LICENSE).

```

---

Would you like me to generate:
- The actual `requirements.txt` (even though it’s optional)?
- A zipped final submission folder?

Let me know, and I’ll prepare it for you.
```

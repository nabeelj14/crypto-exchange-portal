Crypto Exchange Portal
A secure, full-stack decentralized cryptocurrency exchange portal built with Python, Django, and SQLite. Featuring a modern dark Web3 theme, role-based dashboards, live market valuation tracking, and an automated transaction verification ledger.

✨ Features
Role-Based Dashboards: Distinct portals tailored for Admins, Agents, and regular Users with granular permission controls.

Modern Web3 Dark Theme: Sleek, high-performance UI tailored with a dark financial-terminal aesthetic for optimal asset tracking.

Live Market Valuations: Real-time data tables displaying asset pricing, market caps, and volumetric fluctuations.

Automated Transaction Ledgers: Secure tracking and logging system for deposits, withdrawals, and crypto conversions.

Robust Backend Security: Form-encoded validation, secure authentication workflows, and session management powered by Django's native security framework.

🛠️ Tech Stack
Backend: Python, Django

Database: SQLite (Development)

Frontend: HTML5, CSS3, JavaScript, Bootstrap / Custom CSS

Version Control: Git & GitHub

🚀 Getting Started Locally
Follow these steps to set up and run the project on your local machine:

1. Clone the Repository
Bash
git clone https://github.com/nabeelj14/crypto-exchange-portal.git
cd crypto-exchange-portal
2. Create and Activate a Virtual Environment
Bash
python -m venv env
# On Windows:
env\Scripts\activate
# On macOS/Linux:
source env/bin/activate
3. Install Dependencies
Bash
pip install -r requirements.txt
4. Apply Database Migrations
Bash
python manage.py makemigrations
python manage.py migrate
5. Create a Superuser (For Admin Access)
Bash
python manage.py createsuperuser
6. Run the Development Server
Bash
python manage.py runserver
Open your browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

📂 Project Structure
Plaintext
crypto_project/
│
├── core/                # Core configurations, settings, and main URLs
├── cryptoplat/          # Main application module (views, models, templates)
├── db.sqlite3           # Local development database
├── manage.py            # Django project management utility
└── requirements.txt     # Project dependencies

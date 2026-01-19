🧑‍💼 Job Portal Web Application (Flask + SQLite)

A simple Job Portal Web Application built using Python (Flask) and SQLite, where employers can post jobs and users can view available job listings.
This project demonstrates backend development, database handling, and basic frontend integration.

🚀 Features

📋 View all available job listings

➕ Post new jobs with title, company, location, and description

🗄️ SQLite database for persistent data storage

🧩 Clean Flask project structure

🔄 Auto-create database and tables on first run

🛠️ Tech Stack

Backend: Python, Flask

Database: SQLite

Frontend: HTML (Jinja2 templates)

Tools: VS Code, GitHub

📂 Project Structure
job-portal/
│
├── app.py               # Main Flask application
├── database.db          # SQLite database
├── requirements.txt     # Python dependencies
│
├── templates/
│   ├── index.html       # Job listing page
│   └── post_job.html    # Job posting form
│
└── README.md

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/job-portal-flask.git
cd job-portal-flask

2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate # macOS/Linux

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Application
python app.py

🌐 Usage

Open browser and go to:
http://127.0.0.1:5000/

View job listings on the homepage

Click Post Job to add a new job

🗃️ Database Details

Database: database.db

Table: jobs

Column	Type
id	Integer (Primary Key)
title	Text
company	Text
location	Text
description	Text

The database and table are automatically created when the app runs for the first time.

🎯 Learning Outcomes

Flask routing and templates

Handling HTML forms in Flask

SQLite database operations

Backend project structure

CRUD fundamentals

📌 Future Enhancements

🔍 Search & filter jobs

👤 User authentication

📝 Edit & delete job posts

🎨 Enhanced UI using CSS/Bootstrap

☁️ Deployment on Render / Vercel

📄 Resume Description (Short)

Built a Job Portal Web Application using Python Flask and SQLite, enabling job posting and listing functionality with database integration and dynamic HTML rendering.

🤝 Contributing

Pull requests are welcome.
For major changes, please open an issue first.

📜 License

This project is open-source and free to use for learning and portfolio purposes.

If you want, I can also:

✅ Add badges (Python, Flask, SQLite)

✅ Customize README for ATS-friendly resume

✅ Write GitHub project description

✅ Improve frontend UI (HTML + CSS)

Just tell me 👍

post_job.html
File
style.css
File
add this to create readme file

Perfect 👍
Below is an UPDATED, COMPLETE README.md that includes your new frontend files (post_job.html and style.css) and explains the UI enhancement clearly.
You can directly copy–paste this into README.md and upload to GitHub.

🧑‍💼 Job Portal Web Application (Flask + SQLite)

A Job Portal Web Application built using Python (Flask), SQLite, HTML, and CSS.
This application allows employers to post jobs and users to view job listings through a clean, responsive, and professional UI.

🚀 Features

📋 View all job listings on the homepage

➕ Post new jobs using a dedicated form

🗄️ SQLite database for persistent storage

🎨 Modern and professional UI using CSS

🧩 Jinja2 templating with Flask

🔄 Auto database & table creation

🛠️ Tech Stack

Backend: Python, Flask

Database: SQLite

Frontend: HTML5, CSS3

Template Engine: Jinja2

Tools: VS Code, GitHub

📂 Project Structure
job-portal/
│
├── app.py                  # Main Flask application
├── database.db             # SQLite database
├── requirements.txt        # Project dependencies
│
├── templates/
│   ├── index.html          # Homepage (job listings)
│   └── post_job.html       # Job posting form
│
├── static/
│   └── style.css           # Application styling
│
└── README.md

🎨 Frontend Overview
🔹 post_job.html

Job posting form with fields:

Job Title

Company

Location

Description

Uses Flask POST method to submit data

Linked with style.css for clean UI

🔹 style.css

Professional color palette (LinkedIn-style blue)

Responsive grid-based job cards

Styled navbar, footer, buttons, and forms

Clean spacing and shadows for modern look

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/job-portal-flask.git
cd job-portal-flask

2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Application
python app.py

🌐 Usage

Open browser and visit:
http://127.0.0.1:5000/

View job listings on the homepage

Click Post Job to add a new job

Submitted jobs appear instantly on the homepage

🗃️ Database Schema

Database: database.db
Table: jobs

Column	Type
id	INTEGER (Primary Key)
title	TEXT
company	TEXT
location	TEXT
description	TEXT

✔️ Database and table are created automatically on first run.

🎯 Learning Outcomes

Flask routing & request handling

HTML form handling with Flask

SQLite CRUD operations

Frontend–Backend integration

Professional project structuring

📌 Future Enhancements

🔍 Search and filter jobs

👤 User authentication (Login/Register)

✏️ Edit & delete job posts

🎨 Bootstrap / Tailwind UI

☁️ Deploy on Render / Vercel

📄 Resume Description

Job Portal Web Application

Developed a full-stack job portal using Python Flask and SQLite with a modern HTML/CSS frontend, enabling job posting and real-time job listing display.

🤝 Contributing

Contributions are welcome.
Feel free to fork the repository and submit a pull request.

📜 License

This project is open-source and free to use for learning and portfolio purposes.

If you want next:

✅ GitHub badges

✅ Deployed version steps

✅ ATS-optimized resume bullets

✅ LinkedIn project description

Just tell me 👌

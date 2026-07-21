📦 Data Engineering – Python Foundations

Overview

This repository documents my structured progression into Data Engineering using Python.

It covers foundational programming concepts and applies them to practical data workflows including:
	•	File I/O
	•	CSV parsing
	•	Data validation
	•	Cleaning pipelines
	•	Function-based modular design
	•	Output reporting and structured exports

The goal of this repository is to build strong fundamentals before moving into production-grade data engineering projects.

⸻

🛠 Skills Covered

Core Python
	•	Variables & data types
	•	Lists & dictionaries
	•	Loops & conditionals
	•	Nested logic
	•	String cleaning & formatting
	•	File handling (.txt, .csv)
	•	Error handling basics

Data Engineering Foundations
	•	Raw file ingestion
	•	Data validation rules
	•	Row-level cleaning
	•	Structured output generation
	•	Clean vs invalid record separation
	•	Reason-based validation reporting
	•	Function-based pipeline architecture

⸻

🔄 Example Pipeline: Day 11 – Function-Based Validation System

This project processes a raw CSV file of user records and:
	1.	Reads input using csv.DictReader
	2.	Validates:
	•	Missing names
	•	Missing emails
	•	Invalid email format
	3.	Separates:
	•	✅ Clean users
	•	❌ Invalid users (with reason)
	4.	Exports:
	•	clean_users_day11.csv
	•	invalid_users_day11.txt
	5.	Prints a processing summary
  Example Output
  Summary
Total processed: 10
Clean users: 4
Invalid users: 6
📁 Project Structure
data-engineering-python-foundations/
│
├── exercises/          # Practice scripts and pipelines
├── logs/               # Daily learning logs
├── outputs/            # Generated CSV and TXT output files
├── .gitignore
├── LICENSE
└── README.md
▶️ How to Run

From the project root:
python3 exercises/day_11_pipeline_functions.py
Ensure your raw CSV file is located in the correct path referenced in the script.

⸻

📈 Learning Progression

This repository represents:
	•	Structured daily learning
	•	Incremental pipeline improvement
	•	Transition from scripting → modular functions
	•	Clean Git workflow with version control

Next phase:
	•	SQL integration
	•	Larger datasets
	•	ETL-style multi-stage pipelines
	•	Real-world data projects

⸻

 Author

Elispher Itimu
Junior Data Engineering (Python + SQL)

# Personal Expense Tracker (Python CLI App)

A beginner-friendly command-line tool to track personal expenses locally using Python.

## What I Learned
- How to build a real command-line interface (CLI) using Python
- How to use classes to model data (`Expense` class)
- How to store and retrieve data using JSON
- How to handle user input and validate it
- How to work with file I/O (input and output) and error handling
- How to structure a multi-file Python project
- How to use Git and GitHub for version control and sharing

## Features
- Add an expense with amount, category, and an optional note
- View all previous expenses with dates
- Expenses are saved locally in `data.json`
- Simple and readable command-line interface

## Project Structure
expense-tracker/

├── main.py # Main CLI logic and menu

├── expense.py # Expense class and object-to-dictionary converter

├── data.json # Stored expense data

└── README.md # Project description and instructions

## How to Run This Project

> You only need Python 3 installed!

### Run locally

1. [Download the ZIP](https://github.com/sreejagangapuram/expense-tracker/archive/refs/heads/main.zip) and unzip it  
2. Open a terminal in the project folder  
3. Run the app:

```bash
python main.py
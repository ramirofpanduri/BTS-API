# Flask REST API for Books to Scrape

This is a REST API built with Flask to manage books and categories stored in a MySQL database. It provides endpoints to query books by ID, list books by category, and retrieve all categories. The database connection settings and other configuration are loaded from environment variables via a `.env` file.

---

## Technologies Used

- Python  
- Flask (REST API)  
- mysql-connector-python (MySQL driver)  
- python-dotenv (for environment variables)  

---

## Installation

It is recommended to create a virtual environment before installing dependencies.

```bash
# Clone the repository
git clone https://github.com/ramirofpanduri/book-api.git
cd book-api

# Install dependencies using Pipenv
pipenv install

# Activate the virtual environment
pipenv shell


## Environment Variables Setup

Create a `.env` file in the project root directory with your database credentials and other settings:

```env
DB_HOST=localhost
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_NAME=your_db_name
DEBUG=True

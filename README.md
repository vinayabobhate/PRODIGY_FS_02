# PRODIGY_FS_02
Flask Employee Management System: A web app built with Flask for managing employee records. It includes admin login, and functionalities to add, view, update and delete employee data. It uses MySQL for database management, offering a straightforward solution for employee data management.

## Features

- **Admin Login**: Admin authentication with hardcoded credentials.
- **Add Employee**: Form to add new employees with validation for email and phone number.
- **Display Employees**: View the list of all employees.
- **Edit Employee**: Modify existing employee records.
- **Delete Employee**: Remove employee records from the database.

## Requirements

- Python 3.x
- Flask
- MySQL Connector

## Setup

### Prerequisites

- Make sure you have MySQL installed and running.
- Create a MySQL database named `employee` and a table `empdata` with the required schema.
- 
### Database Setup

1. Log in to MySQL as the root user:

    ```bash
    mysql -u root -p
    ```

2. Create the 'employee' database:

    ```sql
    CREATE DATABASE employee;
    ```

3. Switch to the 'employee' database:

    ```sql
    USE employee;
    ```

4. Create the 'empdata' table:

    ```sql
    CREATE TABLE empdata (
        Id INT PRIMARY KEY,
        Name VARCHAR(255),
        Email_Id VARCHAR(255),
        Phone_no VARCHAR(15),
        Address VARCHAR(255),
        Post VARCHAR(255),
        Salary FLOAT
    );
    ```

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/vinayabobhate/PRODIGY_FS_02.git
    cd PRODIGY_FS_02
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Configure the database connection in `app.py`:
   - Update `host`, `user`, `password`, and `database` in the MySQL connector setup to match your MySQL credentials.

4. Run the Flask application:

    ```bash
    python app.py
    ```

5. Open your browser and navigate to `http://127.0.0.1:5000/`.

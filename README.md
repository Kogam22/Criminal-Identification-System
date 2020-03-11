# Criminal Face Identification

## Requirements

- Python 3.6, MySQL
- MySQL - Download for windows: http://mysql.localhost.net.ar/downloads/mysql/5.1.html#downloads
- Set username and password
- Create database `criminaldb`
    ```sql
    create database criminaldb;
    ```
- Update the database username and password in the `.env` file.
- Launch powershell, create new virtual environment and activate it
    ```bash 
    python -m venv env
    source env\Scripts\activate.ps1
    ```
- Install the requirements
    ```bash
    pip install -r requirements.txt
    ```
- Run the program
    ```bash
    python home.py
    ```


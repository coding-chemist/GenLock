# GenLock: Password Management System
GenLock is a robust, user-friendly password management system designed to help users generate secure passwords, evaluate their strength, and manage them efficiently. It includes a modern Streamlit-based frontend for an intuitive UI and a Flask-powered backend for handling API operations.

## Table of Contents
- Features
- Tech Stack
- Setup Instructions
- Project Structure
- Usage
- API Endpoints
- Contributing
- License

## Features
### Password Generator
- Generate strong passwords with custom lengths and optional special characters.
- Visualize password strength with a color-coded progress bar.

### Password Security Check
- Analyze password strength and identify weaknesses.
- Supports evaluation based on length, character diversity, and sequence patterns.

### Password Storage
- View and manage a list of generated passwords.
- Passwords are securely stored in an Excel file (passwords.xlsx).

### Rate Limiting
- Built-in rate limiting for API endpoints to prevent abuse.

### Modern UI
- Clean, responsive interface built using Streamlit for easy navigation.

## Tech Stack

- **Backend:** ![Flask](https://img.shields.io/badge/Flask-2.2.3-blue?logo=flask) ![Flask-Limiter](https://img.shields.io/badge/Flask--Limiter-3.8.0-lightgrey?logo=flask)
- **Frontend:** ![Streamlit](https://img.shields.io/badge/Streamlit-1.40.2-red?logo=streamlit)
- **Storage:** ![OpenPyXL](https://img.shields.io/badge/OpenPyXL-3.1.5-lightblue?logo=openpyxl)
- **Utilities:** ![Requests](https://img.shields.io/badge/Requests-2.32.3-blue?logo=requests) ![Logging](https://img.shields.io/badge/Logging-Standard-lightgrey?logo=python)


## Setup Instructions
### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation
Clone the Repository

```bash
git clone https://github.com/your-repo/genlock.git
cd genlock
```
Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Initialize the Excel File The passwords.xlsx file will be automatically created when the app is first run. If needed, you can reinitialize it manually:

```bash
python -c "from app.excel_manager import initialize_excel; initialize_excel()"
```

Run the Backend Server

```bash
python main.py
```
Run the Frontend Open a new terminal and run:

```bash
streamlit run frontend/app.py
```

## Project Structure
```bash
GenLock/
├── app/
│   ├── __init__.py             # Flask app factory
│   ├── routes.py               # API routes
│   ├── password_utils.py       # Password generation and validation logic
│   ├── excel_manager.py        # Excel file management for storing passwords
├── frontend/
│   ├── app.py                  # Streamlit-based frontend
│   ├── utils.py                # Utility functions for frontend
├── main.py                     # Entry point for the Flask backend
├── requirements.txt            # Python dependencies
├── passwords.xlsx              # (Generated) Password storage
└── README.md                   # Project documentation
```

## Usage
### Generate Password
- Navigate to the Generate Password tab in the UI.
- Customize the password length and toggle special character inclusion.
- Click Generate Password to get a strong password.

### Check Password Security
- Go to the Check Password Security tab.
- Input a password to evaluate and click Check Security.
- View its strength rating and potential weaknesses.

### Stored Passwords
- Access the Stored Passwords tab to view all generated passwords.
- Manage stored passwords (deletion functionality to be added as needed).

### API Endpoints

| Method | Endpoint               | Description                       |
|--------|------------------------|-----------------------------------|
| POST   | /generate-password     | Generates a secure password.      |
| POST   | /check-security        | Evaluates password strength.      |
| GET    | /passwords             | Retrieves all stored passwords.   |
| DELETE | /password/<int:id>     | Deletes a password by its ID.     |

**Example Request (Generate Password):**

```bash
POST /generate-password
{
    "length": 16,
    "include_special": true
}
```
**Example Response:**

```json
{
    "password": "aG$6!J3kL",
    "security_level": "Strong"
}
```

## Contributing
Welcome your contributions to GenLock! If you would like to contribute, please fork the repository, create a new branch, and submit a pull request with your changes..

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- **Flask**: A lightweight WSGI web application framework for Python. [Flask](https://flask.palletsprojects.com/).
- **Streamlit**: An open-source app framework for Machine Learning and Data Science projects. [Streamlit](https://streamlit.io/).
- **OpenPyXL**: A Python library to read/write Excel 2010 xlsx/xlsm/xltx/xltm files. [OpenPyXL](https://openpyxl.readthedocs.io/en/stable/).
- **Requests**: A simple HTTP library for Python. [Requests](https://requests.readthedocs.io/en/latest/).
- **Flask-Limiter**: Rate limiting for Flask applications. [Flask-Limiter](https://flask-limiter.readthedocs.io/en/stable/).
- **Python Software Foundation**: For maintaining Python and supporting the development of Python-based tools and libraries.
- **Logo**: The logo image used in this project is sourced from [Les Olson IT](https://lesolson.com/wp-content/uploads/2019/08/Asset-1strong-password.png).



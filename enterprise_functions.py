import os
import json
import requests
from datetime import datetime as pydatetime, timedelta, timezone
from typing import Optional, Callable, Any, Set
from dotenv import load_dotenv

load_dotenv()

def get_leave_balance(employee_email: str) -> str:
    """
    Retrieves the current leave balance for an employee from the company's HR system.
    
    :param employee_email: employee email address.
    :return: A JSON string with leave balance information or an "error" key.
    """
    print(f"Fetching leave balance for employee: {employee_email}")
    
    # TODO: Implement actual HR system API integration
    # This would typically involve calling an HR API endpoint with authentication
    
    # For demonstration purposes, return mock leave balance data
    mock_leave_data = {
        "annual_leave": {
            "balance": 15.5,
            "accrued": 20.0,
            "taken": 4.5,
            "pending": 2.0
        },
        "sick_leave": {
            "balance": 8.0,
            "accrued": 10.0,
            "taken": 2.0,
            "pending": 0.0
        },
        "personal_leave": {
            "balance": 3.0,
            "accrued": 3.0,
            "taken": 0.0,
            "pending": 0.0
        }
    }
    
    return json.dumps({
        "employee_email": employee_email or "current_user",
        "leave_balance": mock_leave_data
    })


def submit_leave_request(start_date: str, end_date: str, leave_type: str, employee_email: str = None, reason: str = "") -> str:
    """
    Creates a leave request in the company's HR system.
    
    :param start_date: Start date of the leave request in YYYY-MM-DD format.
    :param end_date: End date of the leave request in YYYY-MM-DD format.
    :param leave_type: Type of leave request (must be one of: "annual", "sick", "personal").
    :param employee_email: Optional email of the employee requesting leave. If not provided, uses the current user's email.
    :param reason: Optional reason for the leave request.
    :return: A JSON string with either a "message" about successful submission or an "error" key.
    """
    
    # TODO: Implement actual HR system API integration
    # This would typically involve calling an API endpoint
    print("Submitting leave request to HR system...")
    print(f"Employee Email: {employee_email or 'current user'}")
    print(f"Start Date: {start_date}")
    print(f"End Date: {end_date}")
    print(f"Leave Type: {leave_type}")
    print(f"Reason: {reason}")

    request_id = "1234"

    # For now, just return a success message
    return json.dumps({
        "message": f"Leave request {request_id} submitted successfully",
        "status": "Pending"
    })


def get_employee_info(employee_email: str) -> str:
    """
    Retrieves employee information from the company's HR system.
    Returns details such as the employee's manager name and email, and office location.
    
    :param employee_email: employee email address.
    :return: A JSON string with employee information or an "error" key.
    """
    print(f"Fetching employee information for: {employee_email}")
    
    # TODO: Implement actual HR system API integration
    # This would typically involve calling an HR API endpoint with authentication
    
    # For demonstration purposes, return mock employee data
    mock_employee_data = {
        "first_name": "Jason",
        "last_name": "Leong",
        "email": employee_email or "jason.leong@microsoftdemo.com",
        "start_date": "2022-01-01",
        "manager": {
            "name": "Thivy Ruthra",
            "email": "thivyruthra@microsoftdemo.com",
        },
        "office_location": "Melbourne",
    }
    
    return json.dumps({
        "employee": mock_employee_data,
        "as_of_date": pydatetime.now(timezone.utc).strftime("%Y-%m-%d")
    })


def send_email(recipient: str, subject: str, body: str) -> str:
    """
    Sends an email.
    Always confirm the details with the user before sending the email.
    
    :param recipient: The email address to send the email to.
    :param subject: The subject line of the email.
    :param body: The content within the email body.
    :return: A JSON string with either a "message" or an "error" key.
    """

    # Check the recipient email address = thivyruthra@microsoftdemo.com
    if recipient != "thivyruthra@microsoftdemo.com":
        return json.dumps({
            "error": "email address not found"
        })
    
    return json.dumps({
        "message": f"Email sent to {recipient}."
    })
    

# make functions callable a callable set from enterprise-streaming-agent.ipynb
enterprise_fns: Set[Callable[..., Any]] = {
    get_leave_balance,
    submit_leave_request,
    get_employee_info,
    send_email
}
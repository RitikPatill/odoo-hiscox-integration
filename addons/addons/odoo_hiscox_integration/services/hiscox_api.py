import requests
from .logger import log_error

# Replace this with your actual Beeceptor endpoint (or any mock/real API URL)
API_BASE_URL = "https://hiscoxapi.free.beeceptor.com"

def submit_to_hiscox(case_record):
    """
    Sends the case data to the mock Hiscox API via a POST request.
    Returns the JSON response if successful, otherwise None.
    """
    try:
        # Construct the endpoint and payload
        url = f"{API_BASE_URL}/v1/applications"  # If your Beeceptor rule is /v1/applications
        data = {
            "name": case_record.name,
            "email": case_record.email,
            "phone": case_record.phone,
        }

        # Perform the POST request
        response = requests.post(url, json=data)
        response.raise_for_status()  # Raises an error if status != 2xx

        # Return the parsed JSON, e.g. {"id":123, "status":"submitted"}
        return response.json()

    except Exception as e:
        log_error(f"Failed to submit to Hiscox: {str(e)}")
        return None

def check_status_from_hiscox(case_id):
    """
    Fetches the updated status from the mock Hiscox API via a GET request.
    Returns the 'status' field if successful, otherwise None.
    """
    try:
        # Construct the endpoint for retrieving status
        url = f"{API_BASE_URL}/v1/applications/{case_id}/status"
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        # e.g. {"status": "approved"}
        return data.get("status")

    except Exception as e:
        log_error(f"Failed to check status from Hiscox: {str(e)}")
        return None

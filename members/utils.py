import requests
from django.conf import settings

def send_sms(phone_number, message):
    endpoint = "https://api.mnotify.com/api/sms/quick"
    apiKey = settings.MNOTIFY_API_KEY
    data = {
        "key": apiKey,
        "sender": 'NewspringAG',
        "recipient[]": phone_number,
        "message": message,
        "is_schedule": False,
        "schedule_date": ''
    }
    url = endpoint + '?key=' + apiKey
    try:
        response = requests.post(url, data, proxies={"http":None, "https":None})
        response.raise_for_status()
        
        return response.json()
    
    except requests.exceptions.RequestException as e:
        print(f"Error sending SMS: {e}")
        return None

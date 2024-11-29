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

    response = requests.post(url, data)
    return response.json()

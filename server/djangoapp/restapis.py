# Uncomment the imports below before you add the function code
# import requests
import os

import requests
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv("backend_url", default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    "sentiment_analyzer_url", default="http://localhost:5050/"
)


def get_request(endpoint, **kwargs):
    # Add code for get requests to back end
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params += f"{key}={value}&"

    request_url = f"{backend_url}{endpoint}?{params}"
    print(f"GET FROM {request_url}")

    try:
        response = requests.get(request_url)
        return response.json()
    except:
        print("Network exception occurred")


def analyze_review_sentiments(text):
    request_url = f"{sentiment_analyzer_url}analyze/{text}"
    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")


def post_review(data_dict):
    # Add code for posting review
    request_url = f"{backend_url}/insert_review"
    try:
        response = requests.post(request_url, json= data_dict)
        print(response.json())
        return response.json()
    except:
        print("Network exception occurred")

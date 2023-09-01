#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header ofthe response.
"""
from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    value = {'email': argv[2]}

    response = requests.post(url, data=value)
    print(response.text)

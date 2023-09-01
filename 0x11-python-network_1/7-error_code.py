#!/usr/bin/python3
"""A script that
- takes in a URL
- sends a request to the URL
- displays the body of the response.
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]

    response = requests.get(url)
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    print(response.text)

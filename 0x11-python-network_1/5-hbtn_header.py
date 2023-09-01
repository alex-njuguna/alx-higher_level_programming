#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]

    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))

#!/usr/bin/python3
"""A script that:
- takes in a URL
- sends a POST request to the passed URL
- takes email as a parameter
- displays the body of the response
"""
from sys import argv
from urllib import parse, request


if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}
    data = parse.urlencode(value).encode("ascii")

    req = request.Request(url, data)
    with request.urlopen(req) as response:
        print(response.read().decode("utf-8"))

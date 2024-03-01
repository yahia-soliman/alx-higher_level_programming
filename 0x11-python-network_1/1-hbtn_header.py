#!/usr/bin/python3
"""Fetch alx /status to know how it feels"""
import urllib.request
import sys


with urllib.request.urlopen(sys.argv[1]) as res:
    print(res.headers.get('X-Request-Id'))

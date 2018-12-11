#!/usr/bin/env python

import requests
from pip._vendor.distlib.compat import raw_input


def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass


target_url = raw_input("Enter URL:")

with open("/root/Downloads/subdomains.list", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = word + "." + target_url
        response = request(test_url)
        if response:
            print("[+] Discovered subdomain --> " + test_url)

# Test Case
# Company: ExpressVPN
# Author: Antonio Marto
# Date: 2018-11-01
# Run at Commnad line: pytest -v --capture=no test_case_ExpressVPN.py

import pytest
import requests

URL = "https://www.expressvpn.com/"


def test_case_eVPN(url=URL):
    
    response = requests.get(url)

    if response.status_code == 404:
        print ("HTTP %s" %response.reason)
        assert 0
    else:
        print "My test case continue... and eventually pass"
        assert response.status_code == 200
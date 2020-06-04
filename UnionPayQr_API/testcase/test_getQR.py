#!/usr/bin/python
# -*- coding:utf-8 -*-

import pytest
import requests
import os
from common.purchase1 import Purchase1
from common.read_yaml import readyml

a = os.path.join(os.path.dirname(os.path.realpath(__file__)), "testdate.yaml")
test_data = readyml(a)
print(test_data['test_date2'])



@pytest.mark.parametrize("test_input,expect", test_data['test_date2'])
def test_getQR(test_input,expect):

    url = "http://59.151.73.234:8088/appser/qrcodeCreate.json"
    now = Purchase1(test_input)
    header = {
        "Content-Type": "application/json",
        "ORGID": "HK0016",
        "SIGN": "0623036230"
    }

    body =  {
        "orderId": now,
        "merId": "200428000000028",
        "storeNo": "100009",
        "merName": "zhoushaoliang",
        "txnAmt": "100",
        "merCatCode": "5311",
        "currencyCode": test_input,
        "countryCode": "CN"
     }


    r = requests.post(url=url, headers=header, json=body)
    print(r.json())
    assert r.json()['message'] == expect['message']
    assert r.json()['code'] == expect['code']











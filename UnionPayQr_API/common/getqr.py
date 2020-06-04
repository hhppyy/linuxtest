#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
from common.purchase1 import Purchase1
import time

def getQR(currencyCode, countryCode):
    url = "http://59.151.73.234:8088/appser/qrcodeCreate.json"
    now = Purchase1(currencyCode)
    header = {
        "Content-Type": "application/json",
        "ORGID": "HK0016",
        "SIGN": "0623036230"
    }

    body = {
        "orderId": now,
        "merId": "200428000000028",
        "storeNo": "100009",
        "merName": "zhoushaoliang",
        "txnAmt": "100",
        "merCatCode": "5311",
        "currencyCode": currencyCode,
        "countryCode": countryCode
    }
    time.sleep(2)
    r = requests.post(url=url, headers=header, json=body)
    print(r.json())
    return r.json()["data"]

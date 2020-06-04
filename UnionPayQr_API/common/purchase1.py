#!/usr/bin/python
# -*- coding:utf-8 -*-
import pytest
import requests
import time


def Purchase1(currencyCode):
    now = time.strftime("%Y%m%d%H%M%S")
    url = "http://59.151.73.234:8088/appser/qrcPurchase.json"

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
        "merAbbr": "zsl",
        "merCatCode": "5311",
        "backUrl": "http://59.151.73.234:8088/appser/qrcNotify.json",
        "currencyCode": currencyCode,
        "orderDesc": "测试交易"
    }
    time.sleep(2)
    r = requests.post(url=url, headers=header, json=body)
    print(r.json())
    return now

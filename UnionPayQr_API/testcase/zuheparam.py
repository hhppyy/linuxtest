#!/usr/bin/python3
# -*- coding:utf-8 -*-
import pytest
import os
from common.read_yaml import readyml

a = os.path.join(os.path.dirname(os.path.realpath(__file__)), "testdate.yaml")
test_data = readyml(a)
print(test_data['test_date6'][0])
print(test_data['test_date4'][0])

k = 1
@pytest.mark.parametrize("x", test_data['test_date6'][0])
@pytest.mark.parametrize("y", test_data['test_date4'][0])
def test_zuhecanshu(x, y,):
    print(x, y)

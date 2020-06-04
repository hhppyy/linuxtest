# #!/usr/bin/python
# # -*- coding:utf-8 -*-
# import pytest
# from selenium import webdriver
# import time
# import os
# from common.getqr import getQR
# from common.read_yaml import readyml
#
# a = os.path.join(os.path.dirname(os.path.realpath(__file__)), "testdate.yaml")
# test_data = readyml(a)
# print(test_data['test_date5'])
#
#
# @pytest.mark.parametrize("test_input,expect", test_data['test_date5'])
# def test_unipay(test_input, expect):
#     sgin = getQR(test_input)
#     driver = webdriver.Firefox()
#     driver.maximize_window()
#     time.sleep(5)
#     url = "https://qrctest.unionpayintl.com/cqrt/ossAll/paOverSeaReceUnit"
#     driver.get(url)
#     driver.implicitly_wait(3)
#     driver.find_element_by_xpath(".//*[text()='1、主扫消费']").click()
#     time.sleep(3)
#     # driver.find_element_by_xpath(".//*[@name='mpqrcPayload']").clear()
#     # time.sleep(3)
#     driver.find_element_by_xpath(".//*[@name='mpqrcPayload']").send_keys(sgin)
#     time.sleep(5)
#
#     driver.find_element_by_xpath(".//*[text()='mpqrcPayload']").click()
#
#     time.sleep(10)
#     driver.find_element_by_xpath(".//*[text()='发送']").click()
#     time.sleep(10)
#     t = driver.find_element_by_xpath(".//*[@id='mpeRespId']/tbody/tr[1]/td[2]/span").text
#     time.sleep(3)
#     assert t == expect['message']
#     driver.quit()

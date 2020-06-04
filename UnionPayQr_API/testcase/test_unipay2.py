# #!/usr/bin/python3
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
#
#
# @pytest.mark.parametrize("currencyCode", test_data['test_date4'][0])
# @pytest.mark.parametrize("countryCode", test_data['test_date6'][0])
# def test_unipay(currencyCode, countryCode):
#     sgin = getQR(currencyCode, countryCode)
#     print(currencyCode, countryCode)
#     # sgin = "0002010102111531423808400004999220042800000002852045311530390154031005802US5925zhoushaoliang            6002US6241011420200529113821051920200529092800000046304331D"
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
#     driver.find_element_by_xpath(".//*[text()='mpqrcPayload']").click()
#     time.sleep(5)
#     driver.find_element_by_xpath(".//*[text()='发送']").click()
#     time.sleep(5)
#     t = driver.find_element_by_css_selector("td>span").text
#     # time.sleep(3)
#     print(t)
#     assert t == "success"
#     driver.quit()

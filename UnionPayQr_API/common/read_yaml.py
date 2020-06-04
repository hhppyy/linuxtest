#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import yaml

def readyml(yamlPath):
    '''读取yaml文件内容
    参数path: 相对路径，起始路径：项目的根目录
    realPath: 文件的真实路径,绝对路径地址 '''
    if not os.path.isfile(yamlPath):
        raise FileNotFoundError("文件路径不存在，请检查路径是否正确：%s" % yamlPath)
    # open方法打开直接读出来
    f = open(yamlPath, 'r', encoding='utf-8')
    cfg = f.read()
    d = yaml.load(cfg, Loader=yaml.FullLoader)   # 用load方法转字典
    print("读取的测试文件数据：%s"%d)
    return d
if __name__ == '__main__':
    # a = os.path.join(os.path.dirname(os.path.realpath(__file__)),"testdate.yaml")
    # print(a)
    test_data = readyml("E:\\UnionPayQr_API\\testcase\\testdate.yaml")
    print(test_data['test_date'])
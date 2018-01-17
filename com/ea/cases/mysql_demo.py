#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@author:user 
@file: mysql_demo.py 
@time: 2017/11/24 
"""
import os
import sys
import pymysql
import random


# print(__file__)
# print(sys.argv[0])
# print(os.path.splitext(os.path.basename(__file__))[0])
# print(os.path.basename(sys.argv[0]))
# screenshot_path = os.path.join((os.path.dirname(os.path.dirname(os.path.realpath(__file__)))),
#                                'screenshot\\test_zhongduandai_ziying')
# # file = screenshot_path + "\\*.png"
# # print(file)
# files = os.listdir(screenshot_path)
# print(files)
# for file in files:
#     os.remove(screenshot_path + "\\" + file)
# os.remove(file)


def get_zhuanyuan_acount():
    # SQL 查询语句
    name_sql = "select * from act_org_role_user where role_name like '%平台金融专员%';"
    try:
        # # 打开数据库连接
        db = pymysql.connect(host="172.29.12.197", port=3307, user="o2oadmin", passwd="o2oadmin@we741", db="o2oworkflow", charset='utf8')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        while True:
            # 执行SQL语句
            cursor.execute(name_sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            random_number = random.randint(0, len(results))
            row = results[random_number]
            print(row)
            name = row[6]
            acount_sql = "select * from o2o_employee where employee_namecn = '" + name + "'"
            print(acount_sql)
            cursor.execute(acount_sql)
            result = cursor.fetchone()
            employee_account = result[3]
            is_dimission = result[10]
            print(result)
            print(is_dimission)
            if not is_dimission:
                break
        return employee_account
    except Exception as e:
        raise e
    finally:
        # 关闭数据库连接
        db.close()


def get_approver_acount(name):
    try:
        # # 打开数据库连接
        db = pymysql.connect(host="172.29.12.197", port=3307, user="o2oadmin", passwd="o2oadmin@we741",
                             db="o2oworkflow",
                             charset='utf8')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        acount_sql = "select * from o2o_employee where employee_namecn = '" + name + "'"
        print(acount_sql)
        cursor.execute(acount_sql)
        result = cursor.fetchone()
        employee_account = result[3]
        return employee_account
    except Exception as e:
        raise e
    finally:
        # 关闭数据库连接
        db.close()


def test_test():
    from selenium import webdriver
    chromeoptions = webdriver.ChromeOptions()
    chromeoptions.add_argument("--start-maximized")
    # 实例化一个Chrome浏览器
    driver = webdriver.Chrome(chrome_options=chromeoptions)
    driver.get("http://service.380demo.eascs.com/o2ozx/detail?id=mdqg087cu96jc")
    user = driver.find_element_by_css_selector("input[name='user']")
    user.clear()
    user.send_keys("jun.lu")
    driver.find_element_by_css_selector("input[type='submit']").click()
    import time
    time.sleep(2)
    js = "$('div[data-url$=\"processType=CREDIT_INQUIRY\"]').removeAttr('style')"
    driver.execute_script(js)
    time.sleep(1)
    js = "var q=document.documentElement.scrollTop=1000000"
    driver.execute_script(js)
    time.sleep(1)
    el = driver.find_element_by_xpath("//span[text()='审核中']/../following-sibling::td[1]")
    title_value = el.value_of_css_property("title")
    print(el.value_of_css_property("width"))
    print(el.get_attribute("title"))
    print(type(title_value))
    print("title_value is : " + title_value)


if __name__ == '__main__':
    # print(get_zhuanyuan_acount())
    test_test()

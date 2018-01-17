#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@author:user 
@file: tools.py 
@time: 2017/11/08 
"""

import platform
import os
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import configparser
from com.ea.common.logger import logger
import datetime
from xlutils.copy import copy
import xlrd
import pymysql
import random
from com.ea.resource import globalparameter as gl

platatt = platform.system()
conf = configparser.ConfigParser()
config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'resource')
conf.read(config_path + "/config.ini")


def getdriver():
    if platatt == 'Darwin':
        # chromeoptions = webdriver.ChromeOptions()
        # chromeoptions.add_argument("--kiosk")
        # 实例化一个Chrome浏览器
        driver = webdriver.Chrome()
        driver.set_window_size(1180, 1000)
    elif platatt == "Windows":
        chromeoptions = webdriver.ChromeOptions()
        chromeoptions.add_argument("--start-maximized")
        # 实例化一个Chrome浏览器
        driver = webdriver.Chrome(chrome_options=chromeoptions)
    else:
        logger.info("This platform is not Mac and Windows!! Please check!!")
        raise Exception
    # 隐式设置等待时间为3秒
    driver.implicitly_wait(3)
    # 显示设置等待时间为20秒，每0.5秒循环一次
    wait = WebDriverWait(driver, 10, 0.5)
    return driver, wait


def get_chrome_driver():
    try:
        if platatt == 'Darwin':
            # chromeoptions = webdriver.ChromeOptions()
            # chromeoptions.add_argument("--kiosk")
            # 实例化一个Chrome浏览器
            driver = webdriver.Chrome()
            driver.set_window_size(1180, 1000)
        elif platatt == "Windows":
            chromeoptions = webdriver.ChromeOptions()
            chromeoptions.add_argument("--start-maximized")
            # 实例化一个Chrome浏览器
            driver = webdriver.Chrome(chrome_options=chromeoptions)
        else:
            logger.info("This platform is not Mac and Windows!! Please check!!")
            raise Exception
        # 隐式设置等待时间为3秒
        driver.implicitly_wait(10)
        # 显示设置等待时间为20秒，每0.5秒循环一次
        return driver
    except Exception as e:
        raise e


def login(driver, wait, username="jun.lu"):
    url = conf.get("login", "url")
    # username = conf.get("login", "username")
    # 打开wequant主页
    driver.get(url)
    # 输入用户名
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='user']")))
    user = driver.find_element_by_css_selector("input[name='user']")
    user.clear()
    user.send_keys(username)
    # 点击登录界面上的登录按钮
    driver.find_element_by_css_selector("input[type='submit']").click()
    wait.until(EC.invisibility_of_element_located((By.XPATH, "//a[text()='客户管理'")))
    print("登录成功")


def page_down(driver):
    # 拉动滚动条到最后
    js = "var q=document.documentElement.scrollTop=1000000"
    driver.execute_script(js)


def get_current_time():
    shottime = str(datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d-%H-%M-%S'))
    return shottime


def get_screenshot(driver, screenshot_path, casename):
    shottime = get_current_time()
    if not os.path.exists(screenshot_path):
        os.makedirs(screenshot_path)
    picname = screenshot_path + "\\" + shottime + casename + ".png"
    driver.get_screenshot_as_file(picname)
    print("运行失败,请查看图片:" + picname)


def create_huankuanjihua(fullname):
    u"""修改还款计划表中的名字"""
    filename = config_path + '\\hk_plan.xls'
    rb = xlrd.open_workbook(filename)
    w = copy(rb)
    w.get_sheet(0).write(1, 3, fullname)
    w.save(filename)


def del_pics(screenshot_path):
    u"""删除用例的截图目录下所有的截图文件"""
    # files = os.listdir(screenshot_path)
    # print(files)
    # for file in files:
    #     os.remove(screenshot_path + "\\" + file)
    import glob
    ext = os.path.join(screenshot_path, "*.png")
    files = glob.glob(ext)
    for file in files:
        os.remove(file)


def get_random_zhuanyuan_acount():
    try:
        # # 打开数据库连接
        db = pymysql.connect(host=gl.db_host, port=gl.db_port, user=gl.db_workflow_user, passwd=gl.db_workflow_passwd, db=gl.db_db, charset='utf8')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 查询语句
        name_sql = "select * from act_org_role_user where role_name like '%平台金融专员%';"
        while True:
            # 执行SQL语句
            cursor.execute(name_sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            random_number = random.randint(0, len(results))
            row = results[random_number]
            name = row[6]
            acount_sql = "select * from o2o_employee where employee_namecn = '" + name + "'"
            cursor.execute(acount_sql)
            result = cursor.fetchone()
            employee_account = result[3]
            is_dimission = result[10]
            if not is_dimission:
                break
        print("信贷专员账号是: " + employee_account)
        return employee_account
    except Exception as e:
        raise e
    finally:
        # 关闭数据库连接
        db.close()


def get_acount_by_cnname(name):
    try:
        # # 打开数据库连接
        db = pymysql.connect(host=gl.db_host, port=gl.db_port, user=gl.db_workflow_user, passwd=gl.db_workflow_passwd, db=gl.db_db, charset='utf8')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        acount_sql = "select * from o2o_employee where employee_namecn = '" + name + "'"
        cursor.execute(acount_sql)
        result = cursor.fetchone()
        employee_account = result[3]
        print("当前审批人账号是: " + employee_account)
        return employee_account
    except Exception as e:
        raise e
    finally:
        # 关闭数据库连接
        db.close()


def get_approver_acount_by_yewuno(yewuno, process_type):
    try:
        # # 打开数据库连接
        db = pymysql.connect(host=gl.db_host, port=gl.db_port, user=gl.db_workflow_user, passwd=gl.db_workflow_passwd, db=gl.db_db, charset='utf8')
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # -- 根据业务ID查询当前节点审批人 - - a.process_status = 2 为处理中(过滤掉其他已经结束的流程), -- b.node_status = 1 为审核中(过滤掉其他审核通过或者待审核的节点)

        acount_sql = "select em.employee_account from o2o_employee em,(select  c.auditor_name   from wf_process_task_main a, wf_process_task_node   b, wf_task_node_auditors  c  where  a.task_id = b.task_id and b.task_node_id = c.task_node_id  and b.node_status = 1 and a.process_status = 2 and a.process_name like '%" + process_type + "%' and a.refer_code = '" + yewuno + "') bb where em.employee_namecn=bb.auditor_name"
        print(acount_sql)
        cursor.execute(acount_sql)
        result = cursor.fetchone()
        print(cursor.rowcount)
        employee_account = None
        if cursor.rowcount:
            employee_name = result[0]
            employee_account = employee_name.split(" ", 1)[0].split("-")[-1]
        print("当前审批人账号是: " + str(employee_account))
        return employee_account
    except Exception as e:
        raise e
    finally:
        # 关闭数据库连接
        db.close()


# get_acount_by_cnname("程玲")
if __name__ == '__main__':
    get_approver_acount_by_yewuno("D200-BK-1801-00006", "内部审批")
    # pass

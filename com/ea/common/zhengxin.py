#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@author:user 
@file: zhengxin.py 
@time: 2017/11/21 
"""
from com.ea.common import tools
from com.ea.common.cardnumber import IdCardNumber
from com.ea.common.cardname import cardname
from selenium.webdriver.common.action_chains import ActionChains
import sys, os, time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
from com.ea.common import menu


def zhengxin_apply(self, driver, wait, cardNo, first_name, second_name, english_name, fullname, phoneNo,
                   screenshot_path, pic_name, casename, platform, bank):
    u'''申请征信'''
    print("开始创建征信")
    print("身份证号码: " + cardNo)
    print("姓名: " + fullname)
    try:
        menu.go_to_personnel_zhengxin_query(driver)
        # 点击申请征信
        # tools.get_screenshot(driver, screenshot_path)
        driver.find_element_by_xpath("//a[text()='申请征信']").click()
        # 输入身份证
        # tools.get_screenshot(driver, screenshot_path)
        driver.find_element_by_id("idCard").send_keys(cardNo)
        # 点击下一步按钮
        # tools.get_screenshot(driver, screenshot_path)
        driver.find_element_by_xpath("//input[@value='下一步']").click()
        # 输入姓
        # tools.get_screenshot(driver, screenshot_path)
        driver.find_element_by_name("customerFamilyName").send_keys(first_name)
        # 输入名
        driver.find_element_by_name("customerGivenName").send_keys(second_name)
        # 输入拼音名
        driver.find_element_by_name("customerNamePinyin").send_keys(english_name)
        # 选择证件到期日
        driver.find_element_by_id("licenseExpirationDate").click()
        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
        driver.find_element_by_xpath("//td[text()='15']").click()
        driver.switch_to.default_content()
        # 输入手机号
        driver.find_element_by_id("mobileNumber").send_keys(phoneNo)
        # tools.get_screenshot(driver, screenshot_path)

        # 点击申请征信按钮
        driver.find_element_by_xpath("//input[@value='申请征信']").click()
        # 点击确认按钮
        # tools.get_screenshot(driver, screenshot_path)
        wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='确认']")))
        driver.find_element_by_xpath("//button[text()='确认']").click()
        # tools.get_screenshot(driver, screenshot_path)

        # 选择客户类型
        select = Select(driver.find_element_by_name("zxType"))
        select.select_by_visible_text("借款人")
        # 输入信贷经理
        driver.find_element_by_name("operatorName").send_keys("李")
        driver.find_element_by_id("suggest_row1").click()
        # 输入经办平台
        driver.find_element_by_name("ltdName").send_keys(platform)
        time.sleep(1)
        driver.find_element_by_css_selector("input[name='ltdName']+div>div>span").click()
        # 选择征信银行
        select = Select(driver.find_element_by_id("bankType"))
        select.select_by_visible_text(bank)
        # tools.get_screenshot(driver, screenshot_path)
        # 点击保存按钮
        driver.find_element_by_css_selector("input[value='保 存']").click()
        time.sleep(2)
        # tools.get_screenshot(driver, screenshot_path)
        # 拖动页面到最下面
        target = driver.find_element_by_xpath("//td[text()='经办平台：']")
        driver.execute_script("arguments[0].scrollIntoView();", target)
        time.sleep(2)
        # tools.get_screenshot(driver, screenshot_path)
        driver.find_element_by_xpath("//td[text()='客户身份证复印件：']/following-sibling::td[1]/div/div/div/input").send_keys(
            pic_name)
        time.sleep(1)
        driver.find_element_by_xpath(
            "//td[text()='客户手持授权书及身份证照片：']/following-sibling::td[1]/div/div/div/input").send_keys(pic_name)
        time.sleep(1)
        driver.find_element_by_xpath("//td[text()='客户征信授权书：']/following-sibling::td[1]/div/div/div/input").send_keys(
            pic_name)
        time.sleep(1)
        driver.find_element_by_xpath(
            "//td[text()='客户第三方数据查询授权书：']/following-sibling::td[1]/div/div/div/input").send_keys(pic_name)
        time.sleep(1)
        driver.find_element_by_xpath(
            "//td[text()='手持第三方征信授权书与身份证：']/following-sibling::td[1]/div/div/div/input").send_keys(pic_name)
        time.sleep(1)
        driver.find_element_by_xpath(
            "//td[text()='手持第三方征信授权书与身份证：']/following-sibling::td[1]/div/div/div/input").send_keys(pic_name)
        # tools.get_screenshot(driver, screenshot_path)
        # 点击保存按钮
        time.sleep(2)
        # wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value='保 存']")))
        driver.find_element_by_css_selector("input[value='保 存']").click()
        # 点击启动流程按钮
        time.sleep(1)
        # tools.get_screenshot(driver, screenshot_path)
        wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='启动流程']")))
        driver.find_element_by_xpath("//a[text()='启动流程']").click()
        time.sleep(2)
        # tools.get_screenshot(driver, screenshot_path)
        # 获取单号
        wait.until(EC.presence_of_element_located((By.XPATH, "//td[text()='" + fullname + "']/../td/a")))
        # global zhengxingdanhao
        zhengxingdanhao = driver.find_element_by_xpath("//td[text()='" + fullname + "']/../td/a").text
        result = driver.find_element_by_xpath(
            "//td[text()='" + fullname + "']/following-sibling::td[6]").text
        self.assertEqual(result, "审核中")
        print("产生的征信账号: " + zhengxingdanhao)
        print("创建征信结束")
        return zhengxingdanhao
    except Exception as e:
        shottime = tools.get_current_time()
        picname = screenshot_path + "\\" + shottime + casename + ".png"
        driver.get_screenshot_as_file(picname)
        print("运行失败,请查看图片:" + picname)
        raise e


def zhengxin_approve(self, driver, wait, zhengxingdanhao, screenshot_path, pic_name, casename):
    u'''审批征信'''
    # casename = sys._getframe().f_code.co_name
    # zhengxingdanhao = "O2OZX-1711-00031"
    print("审批征信开始")
    print("审批时的征信账号是:" + zhengxingdanhao)
    try:
        # 进入待办查询页面
        menu.go_to_wait_todo_query(driver)
        # tools.get_screenshot(driver, screenshot_path)
        # 输入征信单号查询
        driver.find_element_by_css_selector("input[name='referCode']").send_keys(zhengxingdanhao)
        driver.find_element_by_css_selector("input[name='queryAll']").click()
        self.assertTrue(driver.find_element_by_css_selector("input[name='queryAll']").is_selected())
        driver.find_element_by_css_selector("input[value='搜索']").click()
        wait.until(EC.visibility_of_all_elements_located(
            (By.XPATH, "//td[text()='" + zhengxingdanhao + "']/preceding-sibling::td[1]")))
        # 点击审批流程中第一条记录
        driver.find_element_by_xpath("//td[text()='" + zhengxingdanhao + "']/preceding-sibling::td[1]").click()
        time.sleep(1)
        # tools.get_screenshot(driver, screenshot_path)
        # 拖动页面到最下面
        target = driver.find_element_by_xpath("//th[text()='开始时间']")
        driver.execute_script("arguments[0].scrollIntoView();", target)
        # 输入审批意见
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//td[text()='审核意见:']/following-sibling::td[1]/textarea")))
        driver.find_element_by_xpath("//td[text()='审核意见:']/following-sibling::td[1]/textarea").send_keys(
            "OK")
        # tools.get_screenshot(driver, screenshot_path)
        # 点击通过按钮并确认
        driver.find_element_by_css_selector("input[value='通 过']").click()
        # tools.get_screenshot(driver, screenshot_path)
        driver.find_element_by_xpath("//button[text()='确认']").click()

        # 第二次审批
        time.sleep(3)
        wait.until(
            EC.element_to_be_clickable((By.XPATH, "//td[text()='" + zhengxingdanhao + "']/preceding-sibling::td[1]")))
        # 点击审批流程中第一条记录
        # tools.get_screenshot(driver, screenshot_path)
        driver.find_element_by_xpath("//td[text()='" + zhengxingdanhao + "']/preceding-sibling::td[1]").click()
        time.sleep(1)
        # tools.get_screenshot(driver, screenshot_path)
        # 拖动页面到最下面
        target = driver.find_element_by_xpath("//th[text()='开始时间']")
        driver.execute_script("arguments[0].scrollIntoView();", target)
        # tools.get_screenshot(driver, screenshot_path)
        # 上传附件
        els = driver.find_elements_by_css_selector("input[name='file']")
        els[0].send_keys(pic_name)
        # 选择证件到期日
        driver.find_element_by_name("zxDate").click()
        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
        driver.find_element_by_xpath("//td[text()='15']").click()
        driver.switch_to.default_content()
        # 点击保存按钮
        driver.find_element_by_css_selector("input[value='保存']").click()
        driver.find_element_by_xpath("//button[text()='确认']").click()
        # 输入审批意见
        driver.find_element_by_xpath(
            "//td[text()='审核意见:']/following-sibling::td[1]/textarea").send_keys(
            "OK")
        # 点击通过按钮并确认
        # tools.get_screenshot(driver, screenshot_path)
        driver.find_element_by_css_selector("input[value='通 过']").click()
        # tools.get_screenshot(driver, screenshot_path)
        driver.find_element_by_xpath("//button[text()='确认']").click()
        time.sleep(3)
        # 切换到个人征信查询页面
        menu.go_to_personnel_zhengxin_query(driver)
        time.sleep(1)
        # tools.get_screenshot(driver, screenshot_path)
        result = driver.find_element_by_xpath(
            "//a[text()='" + zhengxingdanhao + "']/../following-sibling::td[7]").text
        self.assertEqual(result, "流程结束")
        print("审批征信结束")

    except Exception as e:
        shottime = tools.get_current_time()
        picname = screenshot_path + "\\" + shottime + casename + ".png"
        driver.get_screenshot_as_file(picname)
        print("运行失败,请查看图片:" + picname)
        raise e

#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@author:user 
@file: loan_clear_page.py 
@time: 2017/12/29 
"""
from selenium.webdriver.common.by import By
from com.ea.common.base_page import BasePage
import time


class LoanClearPage(BasePage):
    u"""发起贷款结清流程"""
    loan_clear_button_loc = (By.XPATH, "//a[text()='发起贷款结清']")
    payman_loc = (By.NAME, "payName")
    paydate_loc = (By.NAME, "payDate")
    saveandstart_button_loc = (By.CSS_SELECTOR, "input[value='保存并启动流程']")

    def click_loan_no(self, loanno):
        u"""点击贷款单号"""
        click_loanno_loc = (By.XPATH, "//a[text()='" + loanno + "']")
        self.find_element(*click_loanno_loc).click()

    def get_result(self, loanno):
        u"""获取结果状态"""
        result_loc = (By.XPATH, "//a[text()='" + loanno + "']/../following-sibling::td[5]")
        return self.find_element(*result_loc).text

    def click_loan_clear_button(self):
        u"""点击发起贷款结清按钮"""
        self.find_element(*self.loan_clear_button_loc).click()

    def scroll_to_payman(self):
        u"""拖动页面到付款人位置"""
        self.script(*self.payman_loc)

    def input_payname(self, payname):
        u"""输入付款人名字"""
        self.send_keys(self.payman_loc, payname)

    def input_pay_date(self, pay_date):
        u"""输入付款日期"""
        self.input_date_time(self.paydate_loc, pay_date)

    def click_saveandstart(self):
        u"""点击保存并启动流程按钮"""
        self.find_element(*self.saveandstart_button_loc).click()

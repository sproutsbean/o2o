#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@author:user 
@file: charge_page.py 
@time: 2017/12/21 
"""

from selenium.webdriver.common.by import By
from com.ea.common.base_page import BasePage


class ChargePage(BasePage):
    start_flow_button_loc = (By.XPATH, "//a[text()='启动流程']")

    def get_result(self, loanno):
        u"""获取结果状态"""
        result_loc = (By.XPATH, "//a[text()='" + loanno + "']/../following-sibling::td[8]")
        return self.find_element(*result_loc).text

    def click_loan_no(self, loanno):
        u"""点击收费流程页面的贷款单号"""
        loanno_loc = (By.XPATH, "//a[text()='" + loanno + "']")
        self.find_element(*loanno_loc).click()

    def click_start_flow(self):
        u"""点击启动流程按钮"""
        self.find_element(*self.start_flow_button_loc).click()

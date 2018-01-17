#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@author:user 
@file: interview_page.py 
@time: 2017/12/22 
"""

from selenium.webdriver.common.by import By
from com.ea.common.base_page import BasePage
import time


class InterviewPage(BasePage):
    edit_intervie_info_loc = (By.XPATH, "//a[text()='编辑面签资料']")
    select_jiekuanhetong_loc = (By.NAME, "contractFlag")
    save_button_loc = (By.CSS_SELECTOR, "input[value='保存']")
    confirm_button_loc = (By.XPATH, "//button[text()='确认']")
    put_file_loc = (By.CSS_SELECTOR, "input[name='file']")
    close_loc = (By.CSS_SELECTOR, "div.action-dialog-model-close")
    interview_submit_loc = (By.XPATH, "//a[text()='面签申报']")

    def get_result(self, loanno):
        u"""获取结果状态"""
        result_loc = (By.XPATH, "//a[text()='" + loanno + "']/../following-sibling::td[10]")
        return self.find_element(*result_loc).text

    def click_loan_no(self, loanno):
        u"""点击面签提报页面的贷款单号"""
        loan_no_loc = (By.XPATH, "//a[text()='" + loanno + "']")
        self.find_element(*loan_no_loc).click()

    def click_edit_interview_button(self):
        u"""点击编辑面签资料按钮"""
        self.find_element(*self.edit_intervie_info_loc).click()

    def select_jiekuanhetong(self, jiekuanhetong_flag):
        u"""选择借款合同是否齐备"""
        self.select_widget(jiekuanhetong_flag, *self.select_jiekuanhetong_loc)

    def click_save_button(self):
        u"""点击保存按钮"""
        self.find_element(*self.save_button_loc).click()
        time.sleep(1)

    def click_confirm_button(self):
        u"""点击确认按钮"""
        self.find_element(*self.confirm_button_loc).click()
        time.sleep(1)

    def input_file(self, file_path):
        u"""上传面签资料"""
        self.find_element(*self.put_file_loc).send_keys(file_path)

    def click_close_button(self):
        u"""点击关闭按钮"""
        self.find_element(*self.close_loc).click()

    def click_interview_submit(self):
        u"""点击面签申报按钮"""
        self.find_element(*self.interview_submit_loc).click()

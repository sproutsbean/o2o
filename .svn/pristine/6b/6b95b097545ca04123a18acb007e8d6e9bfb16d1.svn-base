#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@author:user 
@file: login_page.py 
@time: 2017/12/05 
"""

from selenium.webdriver.common.by import By
from com.ea.common.base_page import BasePage

"""
登录页面元素管理
"""


class LoginPage(BasePage):
    user_loc = (By.CSS_SELECTOR, "input[name='user']")
    submit_loc = (By.CSS_SELECTOR, "input[type='submit']")

    def open(self, url, title):
        u"""打开页面"""
        self._open(url, title)

    def input_username(self, user):
        u"""输入用户名"""
        self.send_keys(self.user_loc, user)

    def click_login(self):
        u"""点击登录按钮"""
        self.find_element(*self.submit_loc).click()

#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@author:user 
@file: menu_check_page.py 
@time: 2018/01/04 
"""
from selenium.webdriver.common.by import By
from com.ea.common.base_page import BasePage
import time


class MenuPage(BasePage):
    search_button_loc = (By.CSS_SELECTOR, "input[value='搜索']")
    query_button_loc = (By.ID, "goods_search")
    next_button_loc = (By.CSS_SELECTOR, "input[value='下一步']")
    css_query_button_loc = (By.CSS_SELECTOR, "input[value='查询']")
    jiangliyuebaodaochu_loc = (By.CSS_SELECTOR, "input[value='奖励月报导出']")
    daochu_button_loc = (By.CSS_SELECTOR, "input[value='导出']")
    xpath_daochu_button_loc = (By.XPATH, "//a[text()='导出']")
    ribaodaochu_loc = (By.CSS_SELECTOR, "input[value='日报导出']")
    yuebaodaochu_loc = (By.CSS_SELECTOR, "input[value='月报导出']")
    xinzeng_button_loc = (By.XPATH, "//a[text()='新增']")
    tianjiarenyuan_button_loc = (By.XPATH, "//a[text()='添加人员']")
    save_button_loc = (By.XPATH, "//a[text()='保存']")
    xpath_save_button_loc = (By.XPATH, "//a[text()='保 存']")
    yewuid_loc = (By.XPATH, "//span[text()='业务ID']")
    shenqingxuqiu_loc = (By.CSS_SELECTOR, "input[value='申请需求']")
    yewuzhiyin_loc = (By.XPATH, "//h3[text()='江西银行办理流程及附件']")
    yingxiaoguanli_loc = (By.XPATH, "//h3[text()='商超贷']")
    peixunguanli_loc = (By.XPATH, "//h3[text()='17届校招生金融专项培训']")
    fengxianguanli_loc = (By.XPATH, "//h3[text()='业务通知']")
    renliguanli_loc = (By.XPATH, "//a[text()='380金服平台内部需求推荐表.xls']")
    caiwuguanli_loc = (By.XPATH, "//a[text()='深圳市怡亚通供应链股份有限公司开票信息2017.1.20.pdf']")
    itguanli_loc = (By.XPATH, "//h3[text()='操作文档']")

    def have_search_button(self):
        els = self.find_elements(*self.search_button_loc)
        if len(els):
            return True
        else:
            return False

    def have_query_button(self):
        els = self.find_elements(*self.query_button_loc)
        if len(els):
            return True
        else:
            return False

    def have_css_query_button(self):
        els = self.find_elements(*self.css_query_button_loc)
        if len(els):
            return True
        else:
            return False

    def have_next_button(self):
        els = self.find_elements(*self.next_button_loc)
        if len(els):
            return True
        else:
            return False

    def have_jiangliyuebaodaochu_button(self):
        els = self.find_elements(*self.jiangliyuebaodaochu_loc)
        if len(els):
            return True
        else:
            return False

    def have_daochu_button(self):
        els = self.find_elements(*self.daochu_button_loc)
        if len(els):
            return True
        else:
            return False

    def have_xpath_daochu_button(self):
        els = self.find_elements(*self.xpath_daochu_button_loc)
        if len(els):
            return True
        else:
            return False

    def have_ribaodaochu_button(self):
        els = self.find_elements(*self.ribaodaochu_loc)
        if len(els):
            return True
        else:
            return False

    def have_yuebaodaochu_button(self):
        els = self.find_elements(*self.yuebaodaochu_loc)
        if len(els):
            return True
        else:
            return False

    def have_xinzeng_button(self):
        els = self.find_elements(*self.xinzeng_button_loc)
        if len(els):
            return True
        else:
            return False

    def have_tianjiarenyuan_button(self):
        els = self.find_elements(*self.tianjiarenyuan_button_loc)
        if len(els):
            return True
        else:
            return False

    def have_save_button(self):
        els = self.find_elements(*self.save_button_loc)
        if len(els):
            return True
        else:
            return False

    def have_xpath_save_button(self):
        els = self.find_elements(*self.xpath_save_button_loc)
        if len(els):
            return True
        else:
            return False

    def have_yewuid(self):
        els = self.find_elements(*self.yewuid_loc)
        if len(els):
            return True
        else:
            return False

    def have_shenqingxuqiu_button(self):
        els = self.find_elements(*self.shenqingxuqiu_loc)
        if len(els):
            return True
        else:
            return False

    def have_yewuzhiyin(self):
        els = self.find_elements(*self.yewuzhiyin_loc)
        if len(els):
            return True
        else:
            return False

    def have_yingxiaoguanli(self):
        els = self.find_elements(*self.yingxiaoguanli_loc)
        if len(els):
            return True
        else:
            return False

    def have_peixunguanli(self):
        els = self.find_elements(*self.peixunguanli_loc)
        if len(els):
            return True
        else:
            return False

    def have_fengxianguanli(self):
        els = self.find_elements(*self.fengxianguanli_loc)
        if len(els):
            return True
        else:
            return False

    def have_renliguanli(self):
        els = self.find_elements(*self.renliguanli_loc)
        if len(els):
            return True
        else:
            return False

    def have_caiwuguanli(self):
        els = self.find_elements(*self.caiwuguanli_loc)
        if len(els):
            return True
        else:
            return False

    def have_itguanli(self):
        els = self.find_elements(*self.itguanli_loc)
        if len(els):
            return True
        else:
            return False

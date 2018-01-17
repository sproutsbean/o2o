#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@author:user 
@file: newzhengxin.py 
@time: 2017/12/11 
"""
from com.ea.pages.zhengxin_page import *
from com.ea.common import menu
from com.ea.resource import globalparameter as gl
import time


class NewZhengxin(object):
    def __init__(self, driver, cardno, fullname, first_name, second_name, english_name, phoneno):
        self.driver = driver
        self.pic_path = gl.test_pic_path
        self.cardNo = cardno
        self.fullname = fullname
        self.first_name = first_name
        self.second_name = second_name
        self.english_name = english_name
        self.phoneNo = phoneno
        self.zhengxindanhao = ""
        self.url = gl.url
        self.title = gl.title

    def zhengxin_apply(self, applyer_account="jun.lu"):
        customer_type = "借款人"
        if applyer_account == "xianhui.ling":
            platform = "粤东"
            manager = "周晶"
        elif applyer_account == "feng.yun":
            platform = "粤西"
            manager = "陈敏芬"
        elif applyer_account == "wenhui.zhang":
            platform = "山东"
            manager = "张树贵"
        elif applyer_account == "ling.cheng":
            platform = "重庆"
            manager = "孙姣"
        else:
            platform = "深圳"
            manager = "周晶"
        bank = "江西银行"
        card_date = "2028-11-11"
        expect_result = "审核中"
        print("开始创建征信")
        print("提单人是: " + applyer_account)
        print("身份证号码: " + self.cardNo)
        print("姓名: " + self.fullname)
        # 实例化征信页面
        customer_info_page = CustomerInfoPage(self.driver)
        # 切换到个人征信查询页面
        menu.go_to_personnel_zhengxin_query(self.driver)
        # 点击征信申请按钮
        customer_info_page.click_zhengxin_apply()
        # 输入身份证
        customer_info_page.input_idcard(self.cardNo)
        # 点击下一步按钮
        customer_info_page.click_next_button()
        # 输入姓
        customer_info_page.input_first_name(self.first_name)
        # 输入名
        customer_info_page.input_last_name(self.second_name)
        # 输入名字拼音
        customer_info_page.input_english_name(self.english_name)
        # 输入手机号码
        customer_info_page.input_phoneno(self.phoneNo)
        # 选择证件到期日期
        customer_info_page.input_cardno_date(card_date)
        # 点击申请征信按钮
        customer_info_page.commit_zhengxin_apply()
        # 点击确定按钮
        customer_info_page.click_confirm_commit()

        # 实例化征信基本信息页面
        zhengxin_base_page = ZhengxinBasePage(self.driver)
        # 选择客户类型
        zhengxin_base_page.select_customer_type(customer_type)
        # 输入信贷经理
        zhengxin_base_page.input_credit_manager(manager)
        # 输入经办平台
        zhengxin_base_page.input_platform(platform)
        # 选择征信银行
        zhengxin_base_page.select_banck(bank)
        # 点击保存按钮
        zhengxin_base_page.click_save_btton()
        time.sleep(2)
        # 拖动页面到最下面
        zhengxin_base_page.page_down()
        # 上传客户身份证复印件
        zhengxin_base_page.put_idcard_pic(self.pic_path)
        time.sleep(1)
        # 上传客户手持授权书及身份证照片
        zhengxin_base_page.put_handle_idcard_pic(self.pic_path)
        time.sleep(1)
        # 上传客户征信授权书
        zhengxin_base_page.put_zhengxin_pic(self.pic_path)
        time.sleep(1)
        # 上传客户第三方数据查询授权书
        zhengxin_base_page.put_third_pic(self.pic_path)
        time.sleep(1)
        # 上传手持第三方征信授权书与身份证
        zhengxin_base_page.put_handle_third_pic(self.pic_path)
        time.sleep(1)
        # 点击保存按钮
        zhengxin_base_page.click_save_btton()
        time.sleep(2)
        # 启动征信流程
        zhengxin_base_page.start_zhengxin()
        time.sleep(2)
        # 获取征信单号
        self.zhengxindanhao = zhengxin_base_page.get_zhengxindanhao(self.fullname)
        actual_result = zhengxin_base_page.get_result(self.fullname)
        assert actual_result == expect_result
        print("产生的征信账号: " + self.zhengxindanhao)
        print("创建征信结束")
        return self.zhengxindanhao

    def zhengxin_approve(self):
        approveview = "OK"
        process_type = "新征信查询"
        card_date = "2028-11-11"
        expect_result = "流程结束"
        print("审批征信开始")
        print("审批时的征信账号是:" + self.zhengxindanhao)
        from com.ea.pages.todo_page import TodoPage, ApproveZhengxinPage
        todopage = TodoPage(self.driver)
        approvepage = ApproveZhengxinPage(self.driver)
        menu.go_to_wait_todo_query(self.driver)
        todopage.input_yewuno(self.zhengxindanhao)
        todopage.click_query_all()
        todopage.click_search_button()
        todopage.click_first_row(process_type)
        approvepage.page_down()
        approvepage.input_approve_view(approveview)
        approvepage.click_approve_button()
        approvepage.click_confirm_button()
        time.sleep(3)
        todopage.click_first_row(process_type)
        approvepage.page_down()
        approvepage.upload_file(self.pic_path)
        approvepage.input_cardno_date(card_date)
        approvepage.click_save_button()
        approvepage.click_confirm_button()
        approvepage.input_approve_view(approveview)
        approvepage.click_approve_button()
        approvepage.click_confirm_button()
        time.sleep(3)
        menu.go_to_personnel_zhengxin_query(self.driver)
        actual_result = approvepage.get_result(self.zhengxindanhao)
        assert actual_result == expect_result
        print("审批征信结束")

    def zhengxin_approve_by_role(self, zhengxindanhao, process_type):
        approveview = "OK"
        # process_type = "新征信查询"
        card_date = "2028-11-11"
        expect_result = "流程结束"
        print("审批征信开始")
        print("审批时的征信账号是:" + zhengxindanhao)
        from com.ea.pages.todo_page import TodoPage, ApproveZhengxinPage
        todopage = TodoPage(self.driver)
        approvepage = ApproveZhengxinPage(self.driver)
        menu.go_to_wait_todo_query(self.driver)
        todopage.input_yewuno(zhengxindanhao)
        # todopage.click_query_all()
        todopage.click_search_button()
        todopage.click_first_row(process_type)
        approvepage.page_down()
        approvepage.input_approve_view(approveview)
        approvepage.click_approve_button()
        approvepage.click_confirm_button()
        time.sleep(3)
        todopage.click_first_row(process_type)
        approvepage.page_down()
        approvepage.upload_file(self.pic_path)
        approvepage.input_cardno_date(card_date)
        approvepage.click_save_button()
        approvepage.click_confirm_button()
        approvepage.input_approve_view(approveview)
        approvepage.click_approve_button()
        approvepage.click_confirm_button()
        time.sleep(3)
        menu.go_to_personnel_zhengxin_query(self.driver)
        actual_result = approvepage.get_result(zhengxindanhao)
        assert actual_result == expect_result
        print("审批征信结束")

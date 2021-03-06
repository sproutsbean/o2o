#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@author:user 
@file: loan.py 
@time: 2018/01/03 
"""
from com.ea.common import tools, menu, login
import time


def loan_approve(driver, loanno, screenshot_path, casename):
    u"""贷款审批"""
    number = "0"
    view = "OK"
    process_type = "征信准入"
    except_result = "征信准入完成"
    # self.loanno = "SK0027-BK-1712-00006"
    print("审批贷款开始")
    print("使用的贷款单号是:" + loanno)
    from com.ea.pages.todo_page import TodoPage, ApproveLoanPage
    try:
        todopage = TodoPage(driver)
        approvepage = ApproveLoanPage(driver)
        # 进入待办查询页面
        menu.go_to_wait_todo_query(driver)
        todopage.input_yewuno(loanno)
        todopage.click_query_all()
        todopage.click_search_button()
        todopage.click_first_row(process_type)
        approvepage.scrollto_edit()
        approvepage.click_edit()
        approvepage.input_bank_overdue(number)
        approvepage.input_credit_overdue(number)
        approvepage.input_nobank_overdue(number)
        approvepage.scrollto_save_button()
        approvepage.click_save_button()
        time.sleep(2)
        approvepage.scrollto_approve_view()
        approvepage.input_approve_view(view)
        approvepage.click_tongguo()
        approvepage.click_confirm()
        time.sleep(3)
        menu.go_to_loan_query(driver)
        time.sleep(1)
        actual_result = approvepage.get_result(loanno)
        assert actual_result == except_result
        print("审批贷款结束")
    except Exception as e:
        tools.get_screenshot(driver, screenshot_path, casename)
        raise e


def loan_by_role_approve(driver,loanno, screenshot_path, casename):
    u"""贷款审批"""
    number = "0"
    view = "OK"
    process_type = "征信准入"
    except_result = "征信准入完成"
    # self.loanno = "SK0027-BK-1712-00006"
    print("审批贷款开始")
    print("使用的贷款单号是:" + loanno)
    from com.ea.pages.todo_page import TodoPage, ApproveLoanPage
    try:
        approver_account = tools.get_approver_acount_by_yewuno(loanno, process_type)
        login.login(driver, username=approver_account)
        todopage = TodoPage(driver)
        approvepage = ApproveLoanPage(driver)
        # 进入待办查询页面
        menu.go_to_wait_todo_query(driver)
        todopage.input_yewuno(loanno)
        # todopage.click_query_all()
        todopage.click_search_button()
        todopage.click_first_row(process_type)
        approvepage.scrollto_edit()
        approvepage.click_edit()
        approvepage.input_bank_overdue(number)
        approvepage.input_credit_overdue(number)
        approvepage.input_nobank_overdue(number)
        approvepage.scrollto_save_button()
        approvepage.click_save_button()
        time.sleep(2)
        approvepage.scrollto_approve_view()
        approvepage.input_approve_view(view)
        approvepage.click_tongguo()
        approvepage.click_confirm()
        time.sleep(3)
        menu.go_to_loan_query(driver)
        time.sleep(1)
        actual_result = approvepage.get_result(loanno)
        assert actual_result == except_result
        print("审批贷款结束")
    except Exception as e:
        tools.get_screenshot(driver, screenshot_path, casename)
        raise e

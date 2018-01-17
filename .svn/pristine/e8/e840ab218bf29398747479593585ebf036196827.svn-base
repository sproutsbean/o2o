#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@author:user 
@file: loan_clear.py 
@time: 2018/01/02 
"""

from com.ea.common import tools, menu, login
import time


def loan_clear(driver, payname, loanno, casename, screenshot_path):
    u"""贷款结清"""
    expect_result = "审核中"
    pay_date = "2017-10-10"
    print("申请贷款结清开始")
    print("使用的贷款单号是:" + loanno)
    try:
        menu.go_to_loan_query(driver)
        from com.ea.pages.loan_clear_page import LoanClearPage
        loanclearpage = LoanClearPage(driver)
        loanclearpage.click_loan_no(loanno)
        loanclearpage.click_loan_clear_button()
        loanclearpage.scroll_to_payman()
        loanclearpage.input_payname(payname)
        loanclearpage.input_pay_date(pay_date)
        loanclearpage.click_saveandstart()
        actual_result = loanclearpage.get_result(loanno)
        assert actual_result == expect_result
        print("申请贷款结清结束")
    except Exception as e:
        tools.get_screenshot(driver, screenshot_path, casename)
        raise e


def loan_clear_approve(driver, loanno, screenshot_path, casename):
    u"""审批贷款结清流程"""
    types = "提前还款"
    clear_date = "2017-10-10"
    approve_view = "OK"
    expect_result = "还款完成"
    # self.loanno = "SK0027-BP-1801-00002"
    from com.ea.pages.todo_page import TodoPage, LoanClearApprove
    try:
        print("审批贷款结清开始")
        print("使用的贷款单号是:" + loanno)
        todopage = TodoPage(driver)
        loanclearapprovepage = LoanClearApprove(driver)
        menu.go_to_wait_todo_query(driver)
        todopage.input_yewuno(loanno)
        todopage.click_query_all()
        todopage.click_search_button()
        todopage.click_first_row(types)
        loanclearapprovepage.scroll_to_clear_date()
        loanclearapprovepage.input_clear_date(clear_date)
        loanclearapprovepage.click_save_button()
        loanclearapprovepage.click_confirm_button()
        loanclearapprovepage.input_approve_view(approve_view)
        loanclearapprovepage.click_tongguo_button()
        loanclearapprovepage.click_confirm_button()
        time.sleep(5)
        menu.go_to_loan_query(driver)
        actual_result = loanclearapprovepage.get_result(loanno)
        assert actual_result == expect_result
        print("审批贷款结清结束")
    except Exception as e:
        tools.get_screenshot(driver, screenshot_path, casename)
        raise e


def loan_clear_approve_by_role(driver,loanno, screenshot_path, casename):
    u"""审批贷款结清流程"""
    process_type = "提前还款"
    clear_date = "2017-10-10"
    approve_view = "OK"
    expect_result = "还款完成"
    # self.loanno = "SK0027-BP-1801-00002"
    from com.ea.pages.todo_page import TodoPage, LoanClearApprove
    try:
        print("审批贷款结清开始")
        print("使用的贷款单号是:" + loanno)
        approver_account = tools.get_approver_acount_by_yewuno(loanno, process_type)
        login.login(driver, username=approver_account)
        todopage = TodoPage(driver)
        loanclearapprovepage = LoanClearApprove(driver)
        menu.go_to_wait_todo_query(driver)
        todopage.input_yewuno(loanno)
        # todopage.click_query_all()
        todopage.click_search_button()
        todopage.click_first_row(process_type)
        loanclearapprovepage.scroll_to_clear_date()
        loanclearapprovepage.input_clear_date(clear_date)
        loanclearapprovepage.click_save_button()
        loanclearapprovepage.click_confirm_button()
        loanclearapprovepage.input_approve_view(approve_view)
        loanclearapprovepage.click_tongguo_button()
        loanclearapprovepage.click_confirm_button()
        time.sleep(5)
        menu.go_to_loan_query(driver)
        actual_result = loanclearapprovepage.get_result(loanno)
        assert actual_result == expect_result
        print("审批贷款结清结束")
    except Exception as e:
        tools.get_screenshot(driver, screenshot_path, casename)
        raise e

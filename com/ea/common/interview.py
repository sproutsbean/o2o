#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@author:user 
@file: interview.py 
@time: 2018/01/03 
"""

import time
from com.ea.common import menu, tools, login
from com.ea.resource import globalparameter as gl


def interview_apply(driver, loanno, pic_path, screenshot_path, casename):
    u"""面签提报"""
    expect_result = "审核中"
    jiekuanhetong_flag = "是"
    # self.loanno = "SK0027-BP-1801-00002"
    print("申请面签提报开始")
    print("使用的贷款单号是:" + loanno)
    try:
        from com.ea.pages.interview_page import InterviewPage
        interviewpage = InterviewPage(driver)
        # 进入到面签提报页面
        menu.go_to_interview_report(driver)
        handle1 = driver.current_window_handle
        interviewpage.click_loan_no(loanno)
        handles = driver.window_handles
        for handle in handles:
            if handle != handle1:
                driver.switch_to.window(handle)
        time.sleep(1)
        interviewpage.click_edit_interview_button()
        interviewpage.select_jiekuanhetong(jiekuanhetong_flag)
        interviewpage.click_save_button()
        interviewpage.click_confirm_button()
        time.sleep(1)
        interviewpage.input_file(pic_path)
        time.sleep(1)
        interviewpage.click_close_button()
        time.sleep(2)
        interviewpage.click_interview_submit()
        # 关闭申报详情页面
        driver.close()
        # 切换到内部审批页面
        driver.switch_to.window(handle1)
        # 刷新页面
        driver.refresh()
        actual_result = interviewpage.get_result(loanno)
        assert actual_result == expect_result
        print("申请面签提报结束")
    except Exception as e:
        tools.get_screenshot(driver, screenshot_path, casename)
        raise e


def interview_approve(driver, loanno, fullname, screenshot_path, casename):
    u"""面签审批"""
    expect_result = "已放款"
    types = "面签提报"
    card_daoqi_date = "2017-10-10"
    approve_view = "OK"
    isphonecheck = "是"
    phonecheckmessage = "OK"
    isfujianover = "是"
    file_path = gl.file_path
    # self.loanno = "SK0027-BP-1801-00002"
    # self.fullname = "何器"
    print("面签审批开始")
    print("使用的贷款单号是:" + loanno)
    try:
        from com.ea.pages.todo_page import TodoPage, ApproveInterview
        todopage = TodoPage(driver)
        approveinterviepage = ApproveInterview(driver)
        menu.go_to_wait_todo_query(driver)
        todopage.input_yewuno(loanno)
        todopage.click_query_all()
        todopage.click_search_button()
        todopage.click_first_row(types)
        approveinterviepage.scroll_to_approve_view()
        approveinterviepage.input_approve_view(approve_view)
        approveinterviepage.click_tongguo()
        approveinterviepage.click_confirm()
        time.sleep(5)
        todopage.click_first_row(types)
        approveinterviepage.scroll_to_is_phone_check()
        approveinterviepage.select_is_phone_check(isphonecheck)
        approveinterviepage.input_phone_check_message(phonecheckmessage)
        approveinterviepage.click_phone_save_button()
        time.sleep(1)
        approveinterviepage.select_is_fujian_over(isfujianover)
        approveinterviepage.click_fujian_save_button()
        time.sleep(1)
        approveinterviepage.scroll_to_approve_view()
        approveinterviepage.input_approve_view(approve_view)
        approveinterviepage.click_tongguo()
        approveinterviepage.click_confirm()
        time.sleep(5)
        todopage.click_first_row(types)
        approveinterviepage.scroll_to_card_date()
        approveinterviepage.input_card_daoqi_date(card_daoqi_date)
        approveinterviepage.click_save_bank_loan_data()
        time.sleep(1)
        tools.create_huankuanjihua(fullname)
        approveinterviepage.input_file(file_path)
        time.sleep(3)
        approveinterviepage.input_approve_view(approve_view)
        approveinterviepage.click_tongguo()
        approveinterviepage.click_confirm()
        time.sleep(5)
        menu.go_to_loan_query(driver)
        actual_result = approveinterviepage.get_result(loanno)
        assert actual_result == expect_result
        print("审批面签提报结束")
    except Exception as e:
        tools.get_screenshot(driver, screenshot_path, casename)
        raise e


def interview_approve_by_role(driver, loanno, fullname, screenshot_path, casename):
    u"""面签审批"""
    expect_result = "已放款"
    process_type = "面签提报"
    card_daoqi_date = "2017-10-10"
    approve_view = "OK"
    isphonecheck = "是"
    phonecheckmessage = "OK"
    isfujianover = "是"
    file_path = gl.file_path
    # self.loanno = "SK0027-BP-1801-00002"
    # self.fullname = "何器"
    print("面签审批开始")
    print("使用的贷款单号是:" + loanno)
    try:
        from com.ea.pages.todo_page import TodoPage, ApproveInterview
        approver_account = tools.get_approver_acount_by_yewuno(loanno, process_type)
        login.login(driver, username=approver_account)
        todopage = TodoPage(driver)
        approveinterviepage = ApproveInterview(driver)
        menu.go_to_wait_todo_query(driver)
        todopage.input_yewuno(loanno)
        # todopage.click_query_all()
        todopage.click_search_button()
        todopage.click_first_row(process_type)
        approveinterviepage.scroll_to_approve_view()
        approveinterviepage.input_approve_view(approve_view)
        approveinterviepage.click_tongguo()
        approveinterviepage.click_confirm()
        driver.delete_all_cookies()
        approver_account = tools.get_approver_acount_by_yewuno(loanno, process_type)
        login.login(driver, username=approver_account)
        menu.go_to_wait_todo_query(driver)
        todopage.input_yewuno(loanno)
        # todopage.click_query_all()
        todopage.click_search_button()
        todopage.click_first_row(process_type)
        approveinterviepage.scroll_to_is_phone_check()
        approveinterviepage.select_is_phone_check(isphonecheck)
        approveinterviepage.input_phone_check_message(phonecheckmessage)
        approveinterviepage.click_phone_save_button()
        time.sleep(1)
        approveinterviepage.select_is_fujian_over(isfujianover)
        approveinterviepage.click_fujian_save_button()
        time.sleep(1)
        approveinterviepage.scroll_to_approve_view()
        approveinterviepage.input_approve_view(approve_view)
        approveinterviepage.click_tongguo()
        approveinterviepage.click_confirm()
        driver.delete_all_cookies()
        approver_account = tools.get_approver_acount_by_yewuno(loanno, process_type)
        login.login(driver, username=approver_account)
        menu.go_to_wait_todo_query(driver)
        todopage.input_yewuno(loanno)
        # todopage.click_query_all()
        todopage.click_search_button()
        todopage.click_first_row(process_type)
        approveinterviepage.scroll_to_card_date()
        approveinterviepage.input_card_daoqi_date(card_daoqi_date)
        approveinterviepage.click_save_bank_loan_data()
        time.sleep(1)
        tools.create_huankuanjihua(fullname)
        approveinterviepage.input_file(file_path)
        time.sleep(3)
        approveinterviepage.input_approve_view(approve_view)
        approveinterviepage.click_tongguo()
        approveinterviepage.click_confirm()
        driver.delete_all_cookies()
        login.login(driver)
        menu.go_to_loan_query(driver)
        # time.sleep(5)
        actual_result = approveinterviepage.get_result(loanno)
        assert actual_result == expect_result
        print("审批面签提报结束")
    except Exception as e:
        tools.get_screenshot(driver, screenshot_path, casename)
        raise e

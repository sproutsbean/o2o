#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@author:user 
@file: inside.py 
@time: 2018/01/03 
"""
from com.ea.common import tools, menu, login
import time


def approve_inside(driver, loanno, screenshot_path, casename, loan_mode):
    u"""审批内部审批流程"""
    global y
    expect_result = "结束"
    process_type = "内部审批"
    view = "OK"
    print("开始审批内审流程")
    print("使用的贷款单号是:" + loanno)
    from com.ea.pages.todo_page import TodoPage, ApproveInsidePage
    todopage = TodoPage(driver)
    approveinsidepage = ApproveInsidePage(driver)
    # 进入待办查询页面
    try:
        menu.go_to_wait_todo_query(driver)
        todopage.input_yewuno(loanno)
        todopage.click_query_all()
        todopage.click_search_button()
        if loan_mode == "共享模式":
            y = 7
        elif loan_mode == "自营模式":
            y = 6
        else:
            print("输入的模式有误,请确认!!")
        for i in range(y):
            todopage.click_first_row(process_type)
            approveinsidepage.scroll_to_approve_view()
            approveinsidepage.input_approve_view(view)
            approveinsidepage.click_tongguo_button()
            approveinsidepage.click_confirm_button()
            time.sleep(5)
        # 切换到内部审批页面
        menu.go_to_inside_approve(driver)
        actual_result = approveinsidepage.get_result(loanno)
        assert actual_result == expect_result
        print("审批内审流程结束")
    except Exception as e:
        tools.get_screenshot(driver, screenshot_path, casename)
        raise e


def approve_inside_by_role(driver, loanno, screenshot_path, casename):
    u"""审批内部审批流程"""
    expect_result = "结束"
    process_type = "内部审批"
    view = "OK"
    print("开始审批内审流程")
    print("使用的贷款单号是:" + loanno)
    from com.ea.pages.todo_page import TodoPage, ApproveInsidePage
    # 进入待办查询页面
    try:
        todopage = TodoPage(driver)
        approveinsidepage = ApproveInsidePage(driver)
        while tools.get_approver_acount_by_yewuno(loanno, process_type):
            approver_account = tools.get_approver_acount_by_yewuno(loanno, process_type)
            login.login(driver, username=approver_account)
            menu.go_to_wait_todo_query(driver)
            todopage.input_yewuno(loanno)
            # todopage.click_query_all()
            todopage.click_search_button()
            todopage.click_first_row(process_type)
            approveinsidepage.scroll_to_approve_view()
            approveinsidepage.input_approve_view(view)
            approveinsidepage.click_tongguo_button()
            approveinsidepage.click_confirm_button()
            driver.delete_all_cookies()
        # 切换到内部审批页面
        login.login(driver)
        menu.go_to_inside_approve(driver)
        # time.sleep(5)
        actual_result = approveinsidepage.get_result(loanno)
        assert actual_result == expect_result
        print("审批内审流程结束")
    except Exception as e:
        tools.get_screenshot(driver, screenshot_path, casename)
        raise e

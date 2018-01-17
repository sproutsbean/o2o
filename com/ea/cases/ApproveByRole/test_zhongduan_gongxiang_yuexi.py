#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@author:user 
@file: test_zhongduan_gongxiang.py 
@time: 2017/12/11 
"""
import unittest
from com.ea.common.cardname import cardname
from com.ea.common.cardnumber import IdCardNumber
from com.ea.common import login
from com.ea.resource import globalparameter as gl
from com.ea.common import menu
import time
from com.ea.common import tools
import os
import sys
from com.ea.common import interview, charge, inside, loan
from com.ea.common.newzhengxin import NewZhengxin


class MyTestCase(unittest.TestCase):
    u"""终端贷共享模式"""
    screenshot_path = os.path.join(gl.screenshot_path, os.path.splitext(os.path.basename(__file__))[0])
    print(screenshot_path)
    pic_path = gl.test_pic_path
    cardNo = IdCardNumber.getRandomIdNumber(1)[0]
    fullname, first_name, second_name, english_name = cardname.get_name()
    phoneNo = cardname.createPhone()
    applyer_acount = "feng.yun"
    zhengxindanhao = None
    loanno = None
    loan_type = "终端贷"
    loan_mode = "共享模式"

    @classmethod
    def setUpClass(cls):
        tools.del_pics(cls.screenshot_path)
        cls.driver = tools.get_chrome_driver()
        cls.newzhengxin = NewZhengxin(cls.driver, cls.cardNo, cls.fullname, cls.first_name, cls.second_name, cls.english_name, cls.phoneNo)
        # applyer_acount = tools.get_zhuanyuan_acount()
        # 粤东(xianhui.ling),粤西(feng.yun),山东(wenhui.zhang),重庆(ling.cheng)

    def setUp(self):
        pass

    def tearDown(self):
        try:
            self.driver.delete_all_cookies()
        except Exception as e:
            pass
            print(e)
            # pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # pass

    def test_a_zhengxin_apply(self):
        u"""创建征信"""
        casename = sys._getframe().f_code.co_name
        login.login(self.driver, username=self.applyer_acount)
        try:
            MyTestCase.zhengxindanhao = self.newzhengxin.zhengxin_apply(applyer_account=self.applyer_acount)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_b_zhengxin_approve(self):
        u"""审批征信"""
        casename = sys._getframe().f_code.co_name
        try:
            # self.zhengxindanhao = "O2OZX-1801-00227"
            process_type = "新征信查询"
            approver_account = tools.get_approver_acount_by_yewuno(self.zhengxindanhao, process_type)
            login.login(self.driver, username=approver_account)
            self.newzhengxin.zhengxin_approve_by_role(self.zhengxindanhao, process_type)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_c_loan_apply(self):
        u"""申请贷款"""
        casename = sys._getframe().f_code.co_name
        marray = "未婚"
        loantype = self.loan_type
        operator_mode = self.loan_mode
        loan_amount = "50000"
        sdname = "深圳沃尔玛"
        if self.applyer_acount == "xianhui.ling":
            if self.loan_mode == "共享模式":
                operator_platform = "惠州"
            else:
                operator_platform = "粤东"
            loan_manager = "周晶"
        elif self.applyer_acount == "feng.yun":
            operator_platform = "粤西"
            loan_manager = "陈敏芬"
        elif self.applyer_acount == "wenhui.zhang":
            if self.loan_mode == "共享模式":
                operator_platform = "滨州怡通"
            else:
                operator_platform = "山东"
            loan_manager = "张树贵"
        elif self.applyer_acount == "ling.cheng":
            operator_platform = "重庆"
            loan_manager = "孙姣"
        else:
            operator_platform = "深圳"
            loan_manager = "周晶"
        # operator_platform = "深圳平台"
        print("申请贷款开始")
        print("采用的身份证号: " + self.cardNo)
        # self.cardNo = "230804196210023817"
        from com.ea.pages.apply_loan_page import ApplyLoanPage
        try:
            login.login(self.driver, username=self.applyer_acount)
            menu.go_to_loan_apply(self.driver)
            applyloanpage = ApplyLoanPage(self.driver)
            applyloanpage.input_carno(self.cardNo)
            applyloanpage.click_nextbutton()
            applyloanpage.select_marry(marray)
            applyloanpage.select_loantype(loantype)
            applyloanpage.click_confirm_button()
            applyloanpage.input_loanmanager(loan_manager)
            applyloanpage.input_loanamount(loan_amount)
            applyloanpage.select_managerment_mode(operator_mode)
            applyloanpage.input_sdname(sdname)
            applyloanpage.input_operator_platform(operator_platform)
            applyloanpage.click_savebutton()
            applyloanpage.click_choose_zhengxin_button()
            applyloanpage.click_afterzhengxin_savebutton()
            applyloanpage.page_down()
            applyloanpage.click_savebutton()
            applyloanpage.click_commit_zhengxin_in()
            MyTestCase.loanno = applyloanpage.get_loanno()
            self.assertIsNotNone(self.loanno)
            print("产生的贷款单号是:" + self.loanno)
            print("申请贷款结束")
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_d_loan_approve(self):
        u"""贷款审批"""
        casename = sys._getframe().f_code.co_name
        # self.loanno = "D200-BK-1801-00001"
        loan.loan_by_role_approve(self.driver, self.loanno, self.screenshot_path, casename)

    def test_e_caiwu_approve(self):
        u"""财务审批"""
        casename = sys._getframe().f_code.co_name
        view = "OK"
        except_result = "审批完成"
        process_type = "平台财务"
        # self.loanno = "D200-BK-1801-00002"
        print("财务审批开始")
        print("使用的贷款单号是:" + self.loanno)
        from com.ea.pages.todo_page import TodoPage, ApproveCaiwuPage
        try:
            approver_account = tools.get_approver_acount_by_yewuno(self.loanno, process_type)
            login.login(self.driver, username=approver_account)
            todopage = TodoPage(self.driver)
            approvecaiwupage = ApproveCaiwuPage(self.driver)
            # 进入待办查询页面
            menu.go_to_wait_todo_query(self.driver)
            todopage.input_yewuno(self.loanno)
            # todopage.click_query_all()
            todopage.click_search_button()
            todopage.click_first_row(process_type)
            # 拖动页面到最下面
            approvecaiwupage.scroll_to_special_condition()
            approvecaiwupage.input_special_condition(view)
            approvecaiwupage.click_save_button()
            approvecaiwupage.click_confirm_button()
            approvecaiwupage.input_approve_view(view)
            approvecaiwupage.click_tongguo_button()
            approvecaiwupage.click_confirm_button()
            time.sleep(5)
            menu.go_to_yiban_query(self.driver)
            actual_result = approvecaiwupage.get_result_by_role(self.loanno)
            self.assertEqual(actual_result, except_result)
            print("财务审批结束")
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_f_edit_inside_apply(self):
        u"""启动内部审批"""
        casename = sys._getframe().f_code.co_name
        if self.applyer_acount == "xianhui.ling":
            manager_account = "zhoujing.zhoujing"
        elif self.applyer_acount == "feng.yun":
            manager_account = "minfen.chen"
        elif self.applyer_acount == "wenhui.zhang":
            manager_account = "shugui.zhang"
        elif self.applyer_acount == "ling.cheng":
            manager_account = "jiao.sun"
        else:
            manager_account = "jun.lu"
        login.login(self.driver, username=manager_account)
        expect_result = "审核中"
        organization = "公安局"
        home_phone = "075528560115"
        wechat = "123564456"
        postcode = "518001"
        province = "北京"
        city = "东城区"
        road = "无名路"
        live_years = "5"
        children_description = "这里是子女情况描述"
        contact_names = ["张三", "李四"]
        contact_phones = ["13625648852", "13525648853"]
        relationship = "朋友"
        total_price = "20"
        mj_price = "1"
        zhizhao_name = "YYZZ0001"
        register_no = "1025110001"
        organization_type = "个体工商户"
        register_time = "2017-01-01"
        shareholder_number = "1"
        share_proportion = "100"
        business_isnormal = "无"
        borrower_iscontroler = "是"
        controler_name = self.fullname
        yingye_mode = "便利店"
        vocation_type = "百货"
        start_time = "2017-01-01"
        jinglirun = "20"
        fuzhaizonge = "10"
        nianxiaoshoue = "50"
        six_month_sales = "3"
        personnel_number = "5"
        month_pay = "20000"
        water_pay = "1000"
        other_pay = "500"
        transport_pay = "1500"
        capital = "100"
        nianjinglirun = "20"
        should_pay = "50"
        collect = "60"
        liabilities = "10"
        invest = "10"
        property_type = "租赁"
        env_description = "这里是门店经营环境描述"
        store_phone = "57629280"
        store_date = "2017-01-01"
        area = "20"
        shoprent_year = "20000"
        shoprent_starttime = "2017-01-01"
        shoprent_endtime = "2017-05-05"
        store_value = "500000"
        new_old = "很新"
        zhengqi = "整齐"
        store_description = "这里是存货效期描述"
        channel_product = "酒水"
        month_hezuojine = "50000"
        supplier = "贵州茅台"
        hezuo_product = "飞天茅台"
        caigouzhanbi = "50"
        zhangqi = "30"
        main_product = "飞天茅台"
        brand = "茅台"
        buyin_price = "1000"
        model = "飞天茅台"
        selling_price = "1500"
        lastmonth_sales = "20000"
        loan_time = "6个月"
        huankuan_type = "等额本息"
        loan_yongtu = "流动资金"
        eamount = "50000"
        bankname = "江西银行"
        tuijian_type = "合作方推荐"
        tuijian_name = "李超"
        danbao_type = "其它方式"

        # self.loanno = "D200-BK-1801-00002"
        print("开始申请内部审批")
        print("使用的贷款单号是:" + self.loanno)
        try:
            from com.ea.pages.inside_page import InsidePage
            insidepage = InsidePage(self.driver)
            menu.go_to_inside_approve(self.driver)
            handle1 = self.driver.current_window_handle
            insidepage.click_first_row(self.loanno)
            handles = self.driver.window_handles
            handle2 = ""
            for handle in handles:
                if handle != handle1:
                    self.driver.switch_to.window(handle)
                    handle2 = self.driver.current_window_handle
            time.sleep(2)
            insidepage.click_editinside_button()
            handles = self.driver.window_handles
            for handle in handles:
                if handle != handle1 and handle != handle2:
                    self.driver.switch_to.window(handle)
            # 借款人基本信息
            insidepage.click_editborrower_button()
            insidepage.input_card_organization(organization)
            insidepage.input_home_phone(home_phone)
            insidepage.input_wechat(wechat)
            insidepage.input_postcode(postcode)
            insidepage.select_register_addr_province(province)
            time.sleep(1)
            insidepage.select_register_addr_city(city)
            insidepage.input_register_addr_road(road)
            insidepage.select_sleep_addr_province(province)
            time.sleep(1)
            insidepage.select_sleep_addr_city(city)
            insidepage.input_sleep_addr_road(road)
            insidepage.input_live_years(live_years)
            insidepage.input_children(children_description)
            insidepage.click_borrower_save()
            insidepage.click_borrower_confirm()
            time.sleep(1)
            # 添加紧急联系人
            insidepage.scroll_to_contact()
            time.sleep(1)
            for i in range(2):
                insidepage.click_contact_add()
                insidepage.input_contact_name(contact_names[i])
                insidepage.input_contact_phone(contact_phones[i])
                insidepage.select_contacts_relationship(relationship)
                insidepage.click_contact_save()
                time.sleep(2)
            # 夫妻双方负债情况
            insidepage.click_edit_fuzhai()
            insidepage.input_total_price(total_price)
            insidepage.input_mj_price(mj_price)
            insidepage.click_fuzhai_save()
            time.sleep(1)
            # 经营主体信息
            insidepage.scroll_to_jingyingzhuti_edit_button()
            time.sleep(1)
            insidepage.click_jingyingzhuti_edit()
            insidepage.input_yingyezhizhao_name(zhizhao_name)
            insidepage.input_zhucehao(register_no)
            insidepage.select_organization_type(organization_type)
            insidepage.input_register_time(register_time)
            insidepage.select_zhizhao_addr_province(province)
            time.sleep(1)
            insidepage.select_zhizhao_addr_city(city)
            insidepage.input_zhizhao_addr_road(road)
            insidepage.input_shareholder_number(shareholder_number)
            insidepage.input_share_proportion(share_proportion)
            insidepage.select_business_isnormal(business_isnormal)
            insidepage.select_borrower_iscontroler(borrower_iscontroler)
            insidepage.input_controler_name(controler_name)
            insidepage.select_yingye_mode(yingye_mode)
            insidepage.select_vocation_type(vocation_type)
            insidepage.input_start_time(start_time)
            insidepage.click_zhuti_submit_button()
            time.sleep(3)
            # 经营历史
            insidepage.click_history_add()
            insidepage.click_years()
            insidepage.input_jingli(jinglirun)
            insidepage.input_fuzhaizonge(fuzhaizonge)
            insidepage.input_nianxiaoshoue(nianxiaoshoue)
            insidepage.click_history_save_button()
            time.sleep(2)
            # 近6个月营业额情况
            insidepage.click_six_month_edit()
            insidepage.input_january(six_month_sales)
            insidepage.input_february(six_month_sales)
            insidepage.input_march(six_month_sales)
            insidepage.input_april(six_month_sales)
            insidepage.input_may(six_month_sales)
            insidepage.input_june(six_month_sales)
            insidepage.click_six_month_submit()
            time.sleep(2)
            # 编辑经营状况
            insidepage.click_edit_status()
            insidepage.input_personnel_number(personnel_number)
            insidepage.input_month_pay(month_pay)
            insidepage.input_water_pay(water_pay)
            insidepage.input_other_pay(other_pay)
            insidepage.input_transport_pay(transport_pay)
            insidepage.input_capital(capital)
            insidepage.input_nianjinglirun(nianjinglirun)
            insidepage.click_bank_water()
            insidepage.input_should_pay(should_pay)
            insidepage.input_collect(collect)
            insidepage.input_liabilities(liabilities)
            insidepage.input_invest(invest)
            insidepage.click_status_save_button()
            time.sleep(2)
            # 新增门店信息
            insidepage.scroll_to_store()
            time.sleep(1)
            insidepage.click_store_add_button()
            insidepage.select_property_type(property_type)
            insidepage.input_env_description(env_description)
            insidepage.input_store_phone(store_phone)
            insidepage.input_store_date(store_date)
            insidepage.select_store_addr_province(province)
            time.sleep(1)
            insidepage.select_store_addr_city(city)
            insidepage.input_store_addr_road(road)
            insidepage.input_business_area(area)
            insidepage.input_shoprent_year(shoprent_year)
            insidepage.input_shoprent_starttime(shoprent_starttime)
            insidepage.input_shoprent_endtime(shoprent_endtime)
            insidepage.input_store_value(store_value)
            insidepage.select_new_old(new_old)
            insidepage.select_zhengqi(zhengqi)
            insidepage.input_store_description(store_description)
            insidepage.click_store_submit()
            time.sleep(2)
            # 编辑渠道数据
            insidepage.scroll_to_channel()
            time.sleep(1)
            insidepage.click_channel_edit_button()
            insidepage.input_channel_product(channel_product)
            insidepage.input_month_hezuojine(month_hezuojine)
            insidepage.click_channel_save_button()
            time.sleep(2)
            # 增加上游信息
            insidepage.click_shangyou_add_button()
            insidepage.input_supplier(supplier)
            insidepage.input_hezuo_product(hezuo_product)
            insidepage.input_caigouzhanbi(caigouzhanbi)
            insidepage.input_zhangqi(zhangqi)
            insidepage.click_shangyou_save_button()
            time.sleep(2)
            # 增加主要销售产品
            insidepage.scroll_to_main_product()
            time.sleep(1)
            insidepage.click_main_product_add()
            insidepage.input_main_product_name(main_product)
            insidepage.input_brand(brand)
            insidepage.input_buyin_price(buyin_price)
            insidepage.input_model(model)
            insidepage.input_selling_price(selling_price)
            insidepage.input_lastmonth_sales(lastmonth_sales)
            insidepage.click_main_product_save_button()
            time.sleep(1)
            # 编辑贷款信息
            insidepage.scroll_to_loan_info()
            time.sleep(1)
            insidepage.select_loan_time(loan_time)
            insidepage.select_huankuan_type(huankuan_type)
            insidepage.input_eamount(eamount)
            insidepage.select_loan_yongtu(loan_yongtu)
            insidepage.select_loan_bankname(bankname)
            insidepage.select_tuijian_type(tuijian_type)
            insidepage.input_tuijian_name(tuijian_name)
            insidepage.select_danbao_type(danbao_type)
            insidepage.click_loan_info_save()
            insidepage.click_loan_info_confirm()
            self.driver.close()
            # 切换到内审详情页面
            self.driver.switch_to.window(handle2)
            insidepage.click_submit_inside_approve()
            time.sleep(1)
            # 关闭内审详情页面
            self.driver.close()
            # 切换到内部审批页面
            self.driver.switch_to.window(handle1)
            # 刷新页面
            self.driver.refresh()
            actual_result = insidepage.get_result(self.loanno)
            self.assertEqual(actual_result, expect_result)
            print("申请内部审批结束")
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_g_approve_inside(self):
        u"""审批内部审批流程"""
        casename = sys._getframe().f_code.co_name
        # self.loanno = "D200-BK-1801-00007"
        inside.approve_inside_by_role(self.driver, self.loanno, self.screenshot_path, casename)

    def test_h_charge_apply(self):
        u"""启动收费流程"""
        casename = sys._getframe().f_code.co_name
        # self.loanno = "D200-BK-1801-00006"
        if self.applyer_acount == "xianhui.ling":
            manager_account = "zhoujing.zhoujing"
        elif self.applyer_acount == "feng.yun":
            manager_account = "minfen.chen"
        elif self.applyer_acount == "wenhui.zhang":
            manager_account = "shugui.zhang"
        elif self.applyer_acount == "ling.cheng":
            manager_account = "jiao.sun"
        else:
            manager_account = "jun.lu"
        login.login(self.driver, username=manager_account)
        charge.charge_apply(self.driver, self.loanno, self.screenshot_path, casename)

    def test_i_charge_approve(self):
        u"""审批收费流程"""
        casename = sys._getframe().f_code.co_name
        # self.loanno = "D200-BK-1801-00006"
        charge.charge_approve_by_role(self.driver, self.loanno, self.fullname, self.pic_path, self.screenshot_path, casename)

    def test_j_interview_apply(self):
        u"""面签提报"""
        casename = sys._getframe().f_code.co_name
        # self.loanno = "D200-BK-1801-00008"
        if self.applyer_acount == "xianhui.ling":
            manager_account = "zhoujing.zhoujing"
        elif self.applyer_acount == "feng.yun":
            manager_account = "minfen.chen"
        elif self.applyer_acount == "wenhui.zhang":
            manager_account = "shugui.zhang"
        elif self.applyer_acount == "ling.cheng":
            manager_account = "jiao.sun"
        else:
            manager_account = "jun.lu"
        login.login(self.driver, username=manager_account)
        interview.interview_apply(self.driver, self.loanno, self.pic_path, self.screenshot_path, casename)

    def test_k_interview_approve(self):
        u"""面签审批"""
        casename = sys._getframe().f_code.co_name
        # self.loanno = "D200-BK-1801-00006"
        interview.interview_approve_by_role(self.driver, self.loanno, self.fullname, self.screenshot_path, casename)

    def test_l_loan_clear(self):
        u"""贷款结清"""
        casename = sys._getframe().f_code.co_name
        payname = self.fullname
        if self.applyer_acount == "xianhui.ling":
            manager_account = "zhoujing.zhoujing"
        elif self.applyer_acount == "feng.yun":
            manager_account = "minfen.chen"
        elif self.applyer_acount == "wenhui.zhang":
            manager_account = "shugui.zhang"
        elif self.applyer_acount == "ling.cheng":
            manager_account = "jiao.sun"
        else:
            manager_account = "jun.lu"
        login.login(self.driver, username=manager_account)
        # self.loanno = "SK0027-BP-1801-00002"
        from com.ea.common import loan_clear
        loan_clear.loan_clear(self.driver, payname, self.loanno, casename, self.screenshot_path, )

    def test_m_loan_clear_approve(self):
        u"""审批贷款结清流程"""
        casename = sys._getframe().f_code.co_name
        from com.ea.common import loan_clear
        loan_clear.loan_clear_approve_by_role(self.driver, self.loanno, self.screenshot_path, casename)


if __name__ == '__main__':
    unittest.main()

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


class MyTestCase(unittest.TestCase):
    u"""烟草贷自营模式"""
    screenshot_path = os.path.join(gl.screenshot_path, os.path.splitext(os.path.basename(__file__))[0])
    print(screenshot_path)
    pic_path = gl.test_pic_path
    cardNo = IdCardNumber.getRandomIdNumber(1)[0]
    fullname, first_name, second_name, english_name = cardname.get_name()
    phoneNo = cardname.createPhone()
    loanno = ""
    loan_type = "流通贷-烟草"
    loan_mode = "自营模式"

    @classmethod
    def setUpClass(cls):
        cls.driver = tools.get_chrome_driver()
        tools.del_pics(cls.screenshot_path)
        login.login(cls.driver)
        from com.ea.common.newzhengxin import NewZhengxin
        cls.newzhengxin = NewZhengxin(cls.driver, cls.cardNo, cls.fullname, cls.first_name, cls.second_name,
                                      cls.english_name, cls.phoneNo)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # pass

    def test_a_zhengxin_apply(self):
        u"""创建征信"""
        casename = sys._getframe().f_code.co_name
        try:
            self.newzhengxin.zhengxin_apply()
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_b_zhengxin_approve(self):
        u"""审批征信"""
        casename = sys._getframe().f_code.co_name
        try:
            self.newzhengxin.zhengxin_approve()
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_c_loan_apply(self):
        u"""申请贷款"""
        casename = sys._getframe().f_code.co_name
        marray = "未婚"
        loantype = self.loan_type
        operator_mode = self.loan_mode
        loan_manager = "李"
        loan_amount = "50000"
        channel_name = "中国烟草"
        operator_platform = "北京"
        print("申请贷款开始")
        # self.cardNo = "21020019741022267X"
        print("采用的身份证号: " + self.cardNo)
        from com.ea.pages.apply_loan_page import ApplyLoanPage
        try:
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
            applyloanpage.input_channel_name(channel_name)
            applyloanpage.input_zy_operator_platform(operator_platform)
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
        loan.loan_approve(self.driver, self.loanno, self.screenshot_path, casename)

    def test_f_edit_inside_apply(self):
        u"""启动内部审批"""
        casename = sys._getframe().f_code.co_name
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
        loan_time = "6个月"
        huankuan_type = "等额本息"
        loan_yongtu = "流动资金"
        eamount = "50000"
        bankname = "江西银行"
        tuijian_type = "合作方推荐"
        tuijian_name = "李超"
        danbao_type = "其它方式"

        # self.loanno = "C380Z0067-BK-1712-00007"
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
        inside.approve_inside(self.driver, self.loanno, self.screenshot_path, casename, self.loan_mode)

    def test_h_charge_apply(self):
        u"""启动收费流程"""
        casename = sys._getframe().f_code.co_name
        charge.charge_apply(self.driver, self.loanno, self.screenshot_path, casename)

    def test_i_charge_approve(self):
        u"""审批收费流程"""
        casename = sys._getframe().f_code.co_name
        charge.charge_approve(self.driver, self.loanno, self.fullname, self.pic_path, self.screenshot_path, casename)

    def test_j_interview_apply(self):
        u"""面签提报"""
        casename = sys._getframe().f_code.co_name
        interview.interview_apply(self.driver, self.loanno, self.pic_path, self.screenshot_path, casename)

    def test_k_interview_approve(self):
        u"""面签审批"""
        casename = sys._getframe().f_code.co_name
        interview.interview_approve(self.driver, self.loanno, self.fullname, self.screenshot_path, casename)

    def test_l_loan_clear(self):
        u"""贷款结清"""
        casename = sys._getframe().f_code.co_name
        payname = self.fullname
        # self.loanno = "SK0027-BP-1801-00002"
        from com.ea.common import loan_clear
        loan_clear.loan_clear(self.driver, payname, self.loanno, casename, self.screenshot_path, )

    def test_m_loan_clear_approve(self):
        u"""审批贷款结清流程"""
        casename = sys._getframe().f_code.co_name
        from com.ea.common import loan_clear
        loan_clear.loan_clear_approve(self.driver, self.loanno, self.screenshot_path, casename)


if __name__ == '__main__':
    unittest.main()

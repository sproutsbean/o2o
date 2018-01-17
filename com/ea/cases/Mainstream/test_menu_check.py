#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@author:user 
@file: menu_check.py 
@time: 2018/01/04 
"""
from com.ea.common import tools, login, menu
import unittest
import os
import sys
from com.ea.resource import globalparameter as gl
from com.ea.pages.menu_check_page import MenuPage


class MyTestCase(unittest.TestCase):
    screenshot_path = os.path.join(gl.screenshot_path, os.path.splitext(os.path.basename(__file__))[0])

    @classmethod
    def setUpClass(cls):
        cls.driver = tools.get_chrome_driver()
        tools.del_pics(cls.screenshot_path)
        login.login(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_khgl_ppgl(self):
        u"""客户管理下的品牌管理"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_brand_manage(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_khgl_qdgl(self):
        u"""客户管理下的渠道管理"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_channel_manage(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_query_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_khgl_cjhzfgl(self):
        u"""客户管理下的厂家合作方管理"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_factor_manage(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_khgl_ppdmdcx(self):
        u"""客户管理下的品牌贷门店查询"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_brand_store_query(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_query_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_khgl_jxshzfgl(self):
        u"""客户管理下的经销商合作方管理"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_jxshzf_manage(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_zxgl_zxcx(self):
        u"""征信管理下的征信查询"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_personnel_zhengxin_query(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_zxgl_qyzxcx(self):
        u"""征信管理下的企业征信查询"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_company_zhengxin_query(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_dkgl_szdk(self):
        u"""贷款管理下的申请贷款"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_loan_apply(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_next_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_dkgl_dkcx(self):
        u"""贷款管理下的贷款查询"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_loan_query(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_dkgl_zxzr(self):
        u"""贷款管理下的征信准入"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_allow_zhengxin(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_dkgl_nbsp(self):
        u"""贷款管理下的内部审批"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_inside_approve(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_dkgl_sfcx(self):
        u"""贷款管理下的收费查询"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_charge_query(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_dkgl_mqtb(self):
        u"""贷款管理下的面签提报"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_interview_report(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_dkgl_ptcwsh(self):
        u"""贷款管理下的平台财务审核"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_platform_caiwu_approve(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_dkgl_yhsqdkcx(self):
        u"""贷款管理下的用户申请贷款查询"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_customer_apply_loan_query(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_dkgl_fkxxqr(self):
        u"""贷款管理下的放款信息确认"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_loaned_info_confirm(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_dkgl_sqxd(self):
        u"""贷款管理下的申请续贷"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_apply_loan_again(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    # def test_dkgl_jxtsjcx(self):
    #     u"""贷款管理下的旧系统数据查询"""
    #     casename = sys._getframe().f_code.co_name
    #     try:
    #         menu.go_to_old_platform_data_query(self.driver)
    #         menupage = MenuPage(self.driver)
    #         result = menupage.have_search_button()
    #         self.assertTrue(result)
    #     except Exception as e:
    #         tools.get_screenshot(self.driver, self.screenshot_path, casename)
    #         raise e

    def test_dkgl_tzh(self):
        u"""贷款管理下的通知函"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_notification(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_dkgl_zf(self):
        u"""贷款管理下的作废"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_cancel(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_dkgl_zfdkcx(self):
        u"""贷款管理下的作废贷款查询"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_cancel_loan_query(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_dhgl_dhcx(self):
        u"""贷后管理下的贷后查询"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_afterloan_query(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_dhgl_dhdqjccx(self):
        u"""贷后管理下的贷后定期检查查询"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_daihoudingqijiancha_query(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_dhgl_yhfksj(self):
        u"""贷后管理下的银行放款数据"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_yinhangfangkuanshuju(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_query_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_dhgl_hkjhsj(self):
        u"""贷后管理下的还款计划数据"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_huankuanjihuashuju(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_dhgl_fksjqr(self):
        u"""贷后管理下的放款数据确认"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_fangkuanshujuqueren(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_dhgl_tqhkcx(self):
        u"""贷后管理下的提前还款查询"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_tiqianhuankuanchaxun(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_dhgl_dqyjsrn(self):
        u"""贷后管理下的到期预警(10日内)"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_daoqiyujingshirinei(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_dhgl_dqyjwrn(self):
        u"""贷后管理下的到期预警(5日内)"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_daoqiyujingwurinei(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_dhgl_dcsj(self):
        u"""贷后管理下的代偿数据"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_daichangshuju(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_dhgl_yqlb(self):
        u"""贷后管理下的逾期列表"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_yuqiliebiao(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_dhgl_jlfqsj(self):
        u"""贷后管理下的接力分期数据"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_jielifenqishuju(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_dhgl_dcfukuancx(self):
        u"""贷后管理下的代偿付款查询"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_daichangfukuanchaxun(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_dhgl_dchkjl(self):
        u"""贷后管理下的代偿回款记录"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_daichanghuikuanjilu(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_dhgl_dcfkcx(self):
        u"""贷后管理下的代偿反馈查询"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_daichangfankuichaxun(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_dhgl_dcjq(self):
        u"""贷后管理下的代偿结清"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_daichangjieqing(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_dhgl_dcfqjhcx(self):
        u"""贷后管理下的代偿分期计划查询"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_daichangfenqijihuachaxun(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_dhgl_zxgd(self):
        u"""贷后管理下的征信归档"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_zhengxinguidang(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_dhgl_dhgd(self):
        u"""贷后管理下的贷后归档"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_daihouguidang(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_dhgl_dczllr(self):
        u"""贷后管理下的代偿资料录入"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_daichangziliaoluru(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_css_query_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_dhgl_zxjlcx(self):
        u"""贷后管理下的征信记录查询"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_zhengxinjiluchaxun(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_dhgl_dkflcx(self):
        u"""贷后管理下的贷款分类查询"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_daikuanfenleichaxun(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_css_query_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_dhgl_hkrgfl(self):
        u"""贷后管理下的贷款人工分类"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_daikuanrengongfenlei(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_css_query_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_dhgl_jxyhyhkwh(self):
        u"""贷后管理下的江西银行银行卡维护"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_jiangxiyinhangkaweihu(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_dhgl_bcgd(self):
        u"""贷后管理下的补充归档"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_buchongguidang(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_css_query_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_spgl_dbcx(self):
        u"""审批管理下的代办查询"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_wait_todo_query(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_spgl_ybcx(self):
        u"""审批管理下的已办查询"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_yiban_query(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_spgl_yfqcx(self):
        u"""审批管理下的已发起查询"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_yifaqi_query(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_spgl_sxcx(self):
        u"""审批管理下的时效查询"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_shixiao_query(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_spgl_cxjkr(self):
        u"""审批管理下的查询借款人"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_chaxunjiekuanren(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_spgl_lcsxwjs(self):
        u"""审批管理下的流程时效未结束"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_liuchengshixiaoweijieshu(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_spgl_lcsxyjs(self):
        u"""审批管理下的流程时效已结束"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_liuchengshixiaoyijieshu(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_spgl_jdsxwcl(self):
        u"""审批管理下的节点时效未处理"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_jiedianshixiaoweichuli(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_spgl_jdsxycl(self):
        u"""审批管理下的节点时效已处理"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_jiedianshixiaoyichuli(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_spgl_dksqsxcx(self):
        u"""审批管理下的贷款申请时效查询"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_daikuanshenqingshixiaochaxun(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_cwgl_bzjyglf(self):
        u"""财务管理下的保证金与管理费"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_baozhengjinyuguanlifei(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_cwgl_tfcx(self):
        u"""财务管理下的退费查询"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_tuifeichaxun(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_cwgl_szmx(self):
        u"""财务管理下的收支明细"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_shouzhimingxi(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_cwgl_fkzz(self):
        u"""财务管理下的付款转账"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_fukuanzhuanzhang(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_cwgl_jqqr(self):
        u"""财务管理下的结清确认"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_jieqingqueren(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_cwgl_dhkgn(self):
        u"""财务管理下的代还款功能"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_daihuankuangongneng(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_cwgl_yhzhgl(self):
        u"""财务管理下的银行账户管理"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_yinhangzhanghuguanli(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_xinzeng_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_cwgl_dkdtjtj(self):
        u"""财务管理下的贷款单推荐统计"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_daikuandantuijiantongji(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_css_query_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_fwgl_ajbs(self):
        u"""法务管理下的案件报送"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_anjianbaosong(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_css_query_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_fwgl_ajgl(self):
        u"""法务管理下的案件管理"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_anjianguanli(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_bbcx_ywapttj(self):
        u"""报表查询下的业务按平台统计"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_yewuanpingtaitongji(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_css_query_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_bbcx_ywaxdjltj(self):
        u"""报表查询下的业务按信贷经理统计"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_yewuanxindaijinglitongji(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_css_query_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_bbcx_ywasqtj(self):
        u"""报表查询下的业务按省区统计"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_yewuanshengqutongji(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_css_query_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_bbcx_ywafkyhtj(self):
        u"""报表查询下的业务按放款银行统计"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_yewuanfangkuanyinhangtongji(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_css_query_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_bbcx_asjqj_axdjltjfkl(self):
        u"""按时间区间统计放款量下的按信贷经理统计放款量"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_anxindaijinglitongjifangkuanliang(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_css_query_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_bbcx_asjqj_atdtjfkl(self):
        u"""按时间区间统计放款量下的按团队统计放款量"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_antuanduitongjifangkuanliang(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_css_query_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_bbcx_asjqj_asqtjfkl(self):
        u"""按时间区间统计放款量下的按省区统计放款量"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_anshengqutongjifangkuanliang(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_css_query_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_bbcx_antian_axdjltjfkl(self):
        u"""按天统计放款量下的按信贷经理统计放款量"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_antian_anxindaijinglitongjifangkuanliang(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_css_query_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_bbcx_antian_atdtjfkl(self):
        u"""按天统计放款量下的按团队统计放款量"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_antian_antuanduitongjifangkuanliang(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_css_query_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_bbcx_antian_asqtjfkl(self):
        u"""按天统计放款量下的按省区统计放款量"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_antian_anshengqutongjifangkuanliang(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_css_query_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_bbcx_apttjdkye(self):
        u"""报表查询下的按平台统计贷款余额"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_anpingtaitongjidaikuanyue(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_bbcx_adjstjdkye(self):
        u"""报表查询下的按地级市统计贷款余额"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_andijishitongjidaikuanyue(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_bbcx_asqtjdkye(self):
        u"""报表查询下的按省区统计贷款余额"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_anshengqutongjidaikuanyue(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_bbcx_yhsbscfkje(self):
        u"""报表查询下的银行申报审查放款金额"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_yinhangshenbaoshenchafangkuanjine(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_css_query_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_bbcx_yqaptbbtj(self):
        u"""报表查询下的逾期按平台报表统计"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_yuqianpingtaibaobiaotongji(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_css_query_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_bbcx_yqasqbbtj(self):
        u"""报表查询下的逾期按省区报表统计"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_yuqianshengqubaobiaotongji(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_css_query_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_bbcx_aqdjbrtj(self):
        u"""报表查询下的按渠道经办人统计"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_anqudaojingbanrentongji(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_css_query_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_bbcx_adkdtjzb(self):
        u"""报表查询下的按渠道经办人统计(总部)"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_andaikuandantongjizb(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_css_query_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_bbcx_yhedwh(self):
        u"""报表查询下的银行额度维护"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_yinhangeduweihu(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_xinzeng_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_bbcx_ppdfktzcx(self):
        u"""报表查询下的品牌贷放款台账查询"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_pinpaidaifangkuantaizhangchaxun(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_bbcx_rbcx(self):
        u"""报表查询下的日报查询"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_ribaochaxun(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_ribaodaochu_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_bbcx_jlbb(self):
        u"""报表查询下的奖励报表"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_jianglibaobiao(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_jiangliyuebaodaochu_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_bbcx_ybcx(self):
        u"""报表查询下的月报查询"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_yuebaochaxun(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_yuebaodaochu_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_bbcx_ywhztj(self):
        u"""报表查询下的业务汇总统计"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_yewuhuizongtongji(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_xpath_daochu_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_bbcx_dchkbb(self):
        u"""报表查询下的代偿回款报表"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_daichanghuikuanbaobiao(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_bbcx_yhsbjdcx(self):
        u"""报表查询下的银行申报进度查询"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_yinhangshenbaojinduchaxun(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_bbcx_jqyjdc(self):
        u"""报表查询下的加签意见导出"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_jiaqianyijiandaochu(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_daochu_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_xtsz_jggl(self):
        u"""系统设置下的机构管理"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_jigouguanli(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_tianjiarenyuan_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_xtsz_cdgl(self):
        u"""系统设置下的菜单管理"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_caidanguanli(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_save_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_xtsz_zllxgl(self):
        u"""系统设置下的资料类型管理"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_ziliaoleixingguanli(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_xtsz_czzygl(self):
        u"""系统设置下的操作指引管理"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_caozuozhiyinguanli(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_save_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_xtsz_gdzlpz(self):
        u"""系统设置下的归档资料配置"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_guidangziliaopeizhi(self.driver)
            menupage = MenuPage(self.driver)
            menupage.page_down()
            result = menupage.have_xpath_save_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_xtsz_gwwh(self):
        u"""系统设置下的岗位维护"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_gangweiweihu(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_css_query_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_xtsz_lcmbgl(self):
        u"""系统设置下的流程模板管理"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_liuchengmobanguanli(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_xtsz_lcshrck(self):
        u"""系统设置下的流程审核人查看"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_liuchengshenherenchakan(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_xtsz_lcshrth(self):
        u"""系统设置下的流程审核人替换"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_liuchengshenherentihuan(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_css_query_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_xtsz_lcsq(self):
        u"""系统设置下的流程授权"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_liuchengshouquan(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_xinzeng_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_xtsz_rygxwh(self):
        u"""系统设置下的人员关系维护"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_renyuanguanxiweihu(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_css_query_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_xtsz_jsqx(self):
        u"""系统设置下的角色权限"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_juesequanxian(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_xtsz_rycx(self):
        u"""系统设置下的人员查询"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_renyuanchaxun(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_xtsz_rymdwh(self):
        u"""系统设置下的人员名单维护"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_renyuanmingdanweihu(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_xtsz_ryqxck(self):
        u"""系统设置下的人员权限查看"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_renyuanquanxianchakan(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_xtsz_jqczjlcx(self):
        u"""系统设置下的结清操作记录查询"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_jieqingcaozuojiluchaxun(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_xtsz_zfczjlcx(self):
        u"""系统设置下的作废操作记录查询"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_zuofeicaozuojiluchaxun(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_xtsz_yjgl(self):
        u"""系统设置下的邮件管理"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_youjianguanli(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_query_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_xtsz_dxcx(self):
        u"""系统设置下的短信查询"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_duanxinchaxun(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_css_query_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_xtsz_yhjkjhxx(self):
        u"""系统设置下的银行接口交互信息"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_yinhangjiekoujiaohuxinxi(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_search_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_xtsz_mqyccx(self):
        u"""系统设置下的MQ异常查询"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_MQyichangchaxun(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_yewuid()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_xtsz_qfdx(self):
        u"""系统设置下的群发短信"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_qunfaduanxin(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_query_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_xtsz_xqsq(self):
        u"""系统设置下的需求申请"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_xuqiushenqing(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_shenqingxuqiu_button()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_czzy_ywzy(self):
        u"""操作指引下的业务指引"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_yewuzhiyin(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_yewuzhiyin()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_czzy_yxgl(self):
        u"""操作指引下的营销管理"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_yingxiaoguanli(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_yingxiaoguanli()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_czzy_pxgl(self):
        u"""操作指引下的培训管理"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_peixunguanli(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_peixunguanli()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_czzy_fxgl(self):
        u"""操作指引下的风险管理"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_fengxianguanli(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_fengxianguanli()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_czzy_rlgl(self):
        u"""操作指引下的人力管理"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_renliguanli(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_renliguanli()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_czzy_cwgl(self):
        u"""操作指引下的财务管理"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_caiwuguanli(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_caiwuguanli()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e

    def test_czzy_itgl(self):
        u"""操作指引下的IT管理"""
        casename = sys._getframe().f_code.co_name
        try:
            menu.go_to_ITguanli(self.driver)
            menupage = MenuPage(self.driver)
            result = menupage.have_itguanli()
            self.assertTrue(result)
        except Exception as e:
            tools.get_screenshot(self.driver, self.screenshot_path, casename)
            raise e


if __name__ == '__main__':
    unittest.main()

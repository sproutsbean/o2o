#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@author:user 
@file: inside_page.py 
@time: 2017/12/18 
"""
from selenium.webdriver.common.by import By
from com.ea.common.base_page import BasePage
import time


class InsidePage(BasePage):
    def click_loanno(self, loanno):
        click_loanno_loc = (By.XPATH, "//a[text()='" + loanno + "']")
        self.find_element(*click_loanno_loc).click()

    edit_inside_info_loc = (By.XPATH, "//a[text()='编辑内审信息']")
    # 编辑借款人基本信息
    edit_button_base_loc = (By.XPATH, "//a[text()=' 编辑 ']")
    card_organization_loc = (By.NAME, "issuing_authority")
    home_phone_loc = (By.NAME, "home_phone")
    wechat_loc = (By.NAME, "wechat")
    postcode_loc = (By.NAME, "postcode")
    register_address_province_loc = (By.ID, "select_provinceId_1")
    register_address_city_loc = (By.ID, "select_areaId_1")
    register_address_road_loc = (By.NAME, "permanent_residence")
    sleep_address_province_loc = (By.ID, "select_provinceId_2")
    sleep_address_city_loc = (By.ID, "select_areaId_2")
    sleep_address_road_loc = (By.NAME, "recipient_address")
    live_years_loc = (By.NAME, "live_years")
    children_info_loc = (By.XPATH, "//td[text()='子女情况	:']/following-sibling::td[1]/span/textarea")
    borrower_save_button_loc = (By.XPATH, "//button[text()='保存']")
    borrower_confirm_button_loc = (By.XPATH, "//button[text()='确认']")
    # 新增紧急联系人
    contacts_add_button_loc = (By.CSS_SELECTOR, "a[href*='/contactsInfo/update-index']")
    contacts_name_loc = (By.NAME, "contactsName")
    contacts_phone_loc = (By.NAME, "homePhone")
    contacts_address_loc = (By.NAME, "address")
    contacts_relationship_loc = (By.ID, "netPrice")
    contacts_save_button_loc = (By.CSS_SELECTOR, "div>input[value='保存']")
    # 编辑夫妻双方资产负债情况
    edit_fuzhai_button_loc = (By.CSS_SELECTOR, "a[href*='/tot_assets/tot_assets_op']")
    total_assets_loc = (By.ID, "assetsPrice")
    mjPrice_loc = (By.ID, "mjPrice")
    fuzhai_save_button_loc = (By.CSS_SELECTOR, "input[value='保存']:nth-child(2)")
    # 编辑经营主体信息
    jingyingzhuti_edit_button_loc = (By.CSS_SELECTOR, "a[href*='/mainShopInfoRest/updatePage']")
    yingyezhizhao_name_loc = (By.ID, "licenceName")
    yingyezhizhaozhucehao_loc = (By.ID, "blrNumber")
    organization_type_loc = (By.NAME, "organizationForm")
    yingyezhizhao_province_loc = (By.ID, "select_shop_provinceId")
    yingyezhizhao_city_loc = (By.ID, "select_shop_cityId")
    yingyezhizhao_road_loc = (By.ID, "shopaddress")
    shareholders_loc = (By.ID, "shareholders")
    register_time_loc = (By.ID, "stupdate")
    iframe_loc = (By.TAG_NAME, "iframe")
    datetime_loc = (By.XPATH, "//td[text()='15']")
    share_proportion_loc = (By.ID, "shoprent")
    isbusiness_except_loc = (By.ID, "isAbnermal")
    iscontrolman_loc = (By.NAME, "isLoadname")
    controllername_loc = (By.ID, "controllername")
    business_mode_loc = (By.NAME, "businessType")
    vocation_type_loc = (By.NAME, "vocation")
    start_time_loc = (By.ID, "businesshours")
    zhuti_submit_loc = (By.CSS_SELECTOR, "input[value='提交']")
    # 新增经营历史
    history_add_button_loc = (By.CSS_SELECTOR, "a[href*='/management/td/rest/addPage']")
    date_loc = (By.NAME, "tdYear")
    first_date_loc = (By.CSS_SELECTOR, "tr.MTitle+tr")
    jingli_loc = (By.ID, "netPrice")
    fuzhaizonge_loc = (By.ID, "fzTot")
    nianxiaoshoue_loc = (By.ID, "yearmoney")
    history_save_button_loc = (By.CSS_SELECTOR, "div>input[value='保存']")
    # 编辑近六个月营业额情况
    edit_six_month_loc = (By.CSS_SELECTOR, "a[href*='/mainMonthInfoRest/updatePage']")
    january_loc = (By.ID, "turnover1th")
    february_loc = (By.ID, "turnover2th")
    march_loc = (By.ID, "turnover3th")
    april_loc = (By.ID, "turnover4th")
    may_loc = (By.ID, "turnover5th")
    june_loc = (By.ID, "turnover6th")
    six_month_submit_loc = (By.CSS_SELECTOR, "input[value='提交']")
    # 编辑经营状况
    edit_status_loc = (By.CSS_SELECTOR, "a[href*='/managementInfo/update']")
    personnel_number_loc = (By.ID, "personnel")
    monthpay_loc = (By.ID, "monthPay")
    waterpay_loc = (By.ID, "waterPay")
    otherpay_loc = (By.ID, "otherPay")
    transport_loc = (By.ID, "transport")
    capital_loc = (By.ID, "capital")
    profit_loc = (By.ID, "profit")
    pay_loc = (By.ID, "pay")
    collect_loc = (By.ID, "collect")
    liabilities_loc = (By.ID, "liabilities")
    invest_loc = (By.ID, "invest")
    bank_water_loc = (By.XPATH, "//input[@value='YH'][not(@disabled)]")
    status_save_button_loc = (By.CSS_SELECTOR, "div>input[value='保存']")
    # 新增门店信息
    store_add_button_loc = (By.CSS_SELECTOR, "a[href*='/customer/shop/rest/addPagenew']")
    propertytype_loc = (By.NAME, "propertytype")
    env_description_loc = (By.ID, "manageps")
    store_phone_loc = (By.ID, "telephone")
    store_date_loc = (By.ID, "stupdate")
    store_addr_province_loc = (By.ID, "select_shop_provinceId")
    store_addr_city_loc = (By.ID, "select_shop_cityId")
    store_addr_road_loc = (By.ID, "shopaddress")
    businessarea_loc = (By.ID, "businessarea")
    shoprentyear_loc = (By.ID, "shoprentyear")
    shoprentstarttime_loc = (By.ID, "shoprentstart")
    shoprentendtime_loc = (By.ID, "shoprentend")
    store_value_loc = (By.ID, "storeinvamount")
    new_old_loc = (By.NAME, "newtype")
    zhengqi_loc = (By.NAME, "istype")
    store_description_loc = (By.ID, "stockps")
    store_commit_loc = (By.CSS_SELECTOR, "input[value='提交']")
    # 编辑渠道数据
    edit_channel_loc = (By.CSS_SELECTOR, "a[href$='type=addbk']")
    channel_product_loc = (By.CSS_SELECTOR, "textarea[placeholder='汉字，限200字内']")
    hezuojine_loc = (By.NAME, "monthPrice")
    channel_save_button_loc = (By.CSS_SELECTOR, "input[value='保存'][class=' edit btn_blue']")
    # 商超渠道数据
    whitelistTime_loc = (By.NAME, "whitelistTime")

    # 蔬果渠道数据
    startOperateTime_loc = (By.NAME, "startOperateTime")
    isParking_loc = (By.NAME, "isParking")

    # 新增上游信息
    shangyou_add_loc = (By.CSS_SELECTOR, "a[href$='type=addsy']")
    supplier_loc = (By.NAME, "supplier")
    hezuo_product_loc = (By.NAME, "cooperation")
    caigouzhanbi_loc = (By.NAME, "purchase")
    zhangqi_loc = (By.NAME, "period")
    shangyou_save_button_loc = (By.CSS_SELECTOR, "input[value='保存'][class=' edit btn_blue']")

    # 蔬果上游信息
    isOwnFarm_loc = (By.NAME, "isOwnFarm")
    isOtherPurchase_loc = (By.NAME, "isOtherPurchase")
    isFarmer_loc = (By.NAME, "isFarmer")
    farme_address_province_loc = (By.ID, "provinceId")
    farme_address_city_loc = (By.ID, "cityId")
    farme_address_detailAddress_loc = (By.NAME, "detailAddress")
    otherModeRemark_loc = (By.NAME, "otherModeRemark")
    # 蔬果下游信息
    six_month_sales_twobatch_loc = (By.NAME, "twoBatch")
    six_month_sales_supermarket_loc = (By.NAME, "supermarket")
    six_month_sales_groupPurch_loc = (By.NAME, "groupPurch")
    # 商超带没有团购只有下面的直接零售
    directRetail_loc = (By.NAME, "directRetail")
    six_month_sales_retail_loc = (By.NAME, "retail")
    fruits_save_button_loc = (By.CSS_SELECTOR, "input[value='保  存']")

    # 商超下游信息
    xiayou_add_button_loc = (By.CSS_SELECTOR, "a[href$='type=addc']")
    cusName_loc = (By.NAME, "cusName")
    settlementDate_loc = (By.NAME, "settlementDate")
    supplyQuantity_loc = (By.NAME, "supplyQuantity")
    xiayou_save_button_loc = (By.CSS_SELECTOR, "input[value='保存'][class=' edit btn_blue']")
    # 商超十大销售产品
    sale_product_add_loc = (By.CSS_SELECTOR, "a[href$='type=addg']")
    productBrand_loc = (By.NAME, "productBrand")
    productType_loc = (By.NAME, "productType")
    agentQuali_loc = (By.NAME, "agentQuali")
    coopTerm_loc = (By.NAME, "coopTerm")
    y_saleTask_loc = (By.NAME, "y_saleTask")
    sale_product_save_loc = (By.CSS_SELECTOR, "input[value='保存'][class=' edit btn_blue']")
    # 蔬果主要销售产品
    fruits_main_product_add_loc = (By.CSS_SELECTOR, "a[href$='type=addp']")
    fruits_product_name_loc = (By.NAME, "productName")
    lastMonthSaleNum_loc = (By.NAME, "lastMonthSaleNum")
    productionAddress_loc = (By.NAME, "productionAddress")
    fruits_main_product_save_loc = (By.CSS_SELECTOR, "input[value='保存'][class=' edit btn_blue']")
    # 新增主要销售产品
    main_product_add_loc = (By.CSS_SELECTOR, "a[href$='type=addbkp']")
    product_name_loc = (By.CSS_SELECTOR, "input[name='productName']")
    brand_loc = (By.NAME, "brand")
    buyingprice_loc = (By.NAME, "buyingPrice")
    model_loc = (By.NAME, "model")
    sellingprice_loc = (By.NAME, "sellingPrice")
    lastmonthsales_loc = (By.NAME, "lastMonthSales")
    product_save_button_loc = (By.CSS_SELECTOR, "input[value='保存'][class=' edit btn_blue']")
    # 编辑贷款信息
    loan_time_loc = (By.ID, "loanTerm")
    huankuan_type_loc = (By.ID, "repayMentway")
    loan_yongtu_loc = (By.ID, "paymentType")
    eamount_loc = (By.ID, "eaMount")
    bankloanname_loc = (By.ID, "bankLoanName")
    tuijian_type = (By.NAME, "recommendType")
    tuijian_name_loc = (By.NAME, "referrerName")
    first_name_loc = (By.ID, "suggest_row1")
    danbao_type_loc = (By.NAME, "guarAnteeWay")
    loan_save_loc = (By.CSS_SELECTOR, "input[value='保存']")
    loan_confirm_loc = (By.XPATH, "//button[text()='确认']")
    conmmit_inside_approve_loc = (By.XPATH, "//a[text()='提交内审']")

    def get_result(self, loanno):
        u"""获取提交内审后流程的状态"""
        return self.find_element(*(By.XPATH, "//a[text()='" + loanno + "']/../following-sibling::td[9]")).text

    def click_first_row(self, loanno):
        u"""点击贷款单号的链接"""
        self.find_element(*(By.XPATH, "//a[text()='" + loanno + "']")).click()

    def click_editinside_button(self):
        u"""点击编辑内审信息按钮"""
        self.find_element(*self.edit_inside_info_loc).click()

    # -------------------------借款人基本信息---------------------------------------------------------------
    def click_editborrower_button(self):
        u"""点击借款人基本信息的编辑按钮"""
        self.find_element(*self.edit_button_base_loc).click()

    def input_card_organization(self, organization):
        u"""输入发证机构"""
        self.send_keys(self.card_organization_loc, organization)

    def input_home_phone(self, home_phone):
        u"""输入住宅电话"""
        self.send_keys(self.home_phone_loc, home_phone)

    def input_wechat(self, wechat):
        u"""输入微信号"""
        self.send_keys(self.wechat_loc, wechat)

    def input_postcode(self, postcode):
        u"""输入邮政编码"""
        self.send_keys(self.postcode_loc, postcode)

    def select_register_addr_province(self, province):
        u"""选择户籍所在省份"""
        self.select_widget(province, *self.register_address_province_loc)

    def select_register_addr_city(self, city):
        u"""选择户籍所在城市"""
        self.select_widget(city, *self.register_address_city_loc)

    def input_register_addr_road(self, road):
        u"""输入户籍详细地址"""
        self.send_keys(self.register_address_road_loc, road)

    def select_sleep_addr_province(self, provice):
        u"""选择居住地址所在省份"""
        self.select_widget(provice, *self.sleep_address_province_loc)

    def select_sleep_addr_city(self, city):
        u"""选择居住地址所在城市"""
        self.select_widget(city, *self.sleep_address_city_loc)

    def input_sleep_addr_road(self, road):
        u"""输入居住地址详细信息"""
        self.send_keys(self.sleep_address_road_loc, road)

    def input_live_years(self, years):
        u"""输入居住年限"""
        self.send_keys(self.live_years_loc, years)

    def input_children(self, description):
        u"""输入子女情况"""
        self.send_keys(self.children_info_loc, description)

    def click_borrower_save(self):
        u"""点击借款人基本信息界面的保存按钮"""
        self.find_element(*self.borrower_save_button_loc).click()

    def click_borrower_confirm(self):
        u"""点击确认按钮"""
        self.find_element(*self.borrower_confirm_button_loc).click()
        time.sleep(1)

    # -----------------紧急联系人-----------------------------------------------------------------
    def scroll_to_contact(self):
        u"""滑动页面到紧急联系人位置"""
        self.script(*self.contacts_add_button_loc)
        time.sleep(1)

    def click_contact_add(self):
        u"""点击新增紧急联系人"""
        self.find_element(*self.contacts_add_button_loc).click()

    def input_contact_name(self, name):
        u"""输入紧急联系人姓名"""
        self.send_keys(self.contacts_name_loc, name)

    def input_contact_phone(self, phone):
        u"""输入紧急联系人电话"""
        self.send_keys(self.contacts_phone_loc, phone)

    def select_contacts_relationship(self, relationship):
        u"""选择与借款人关系"""
        self.select_widget(relationship, *self.contacts_relationship_loc)

    def click_contact_save(self):
        u"""点击紧急联系人页面的保存按钮"""
        self.find_element(*self.contacts_save_button_loc).click()
        time.sleep(1)

    # ------------------------夫妻双方负债情况--------------------------------------------------------------------
    def click_edit_fuzhai(self):
        u"""点击负债情况的编辑按钮"""
        self.find_element(*self.edit_fuzhai_button_loc).click()

    def input_total_price(self, total):
        u"""输入资产总计"""
        self.send_keys(self.total_assets_loc, total)

    def input_mj_price(self, price):
        u"""输入民间借贷"""
        self.send_keys(self.mjPrice_loc, price)

    def click_fuzhai_save(self):
        u"""点击负债情况页面的保存按钮"""
        self.find_element(*self.fuzhai_save_button_loc).click()
        time.sleep(1)

    # ------------------经营主体信息-------------------------------------------------------------------
    def scroll_to_jingyingzhuti_edit_button(self):
        u"""滑动页面到经营主体信息位置"""
        self.script(*self.jingyingzhuti_edit_button_loc)
        time.sleep(1)

    def click_jingyingzhuti_edit(self):
        u"""点击经营主体信息页面的编辑按钮"""
        self.find_element(*self.jingyingzhuti_edit_button_loc).click()

    def input_yingyezhizhao_name(self, zhizhao_name):
        u"""输入营业执照名称"""
        self.send_keys(self.yingyezhizhao_name_loc, zhizhao_name)

    def input_zhucehao(self, register_no):
        u"""输入营业执照注册号"""
        self.send_keys(self.yingyezhizhaozhucehao_loc, register_no)

    def select_organization_type(self, types):
        u"""选择组织形式"""
        self.select_widget(types, *self.organization_type_loc)

    def input_register_time(self, date):
        u"""点击注册时间"""
        self.input_date_time(self.register_time_loc, date, click=False)

    def select_zhizhao_addr_province(self, province):
        u"""选择营业执照注册地址的省份"""
        self.select_widget(province, *self.yingyezhizhao_province_loc)

    def select_zhizhao_addr_city(self, city):
        u"""选择营业至少注册地址的城市"""
        self.select_widget(city, *self.yingyezhizhao_city_loc)

    def input_zhizhao_addr_road(self, road):
        u"""输入营业执照注册地址的详细信息"""
        self.send_keys(self.yingyezhizhao_road_loc, road)

    def input_shareholder_number(self, number):
        u"""输入股东人数"""
        self.send_keys(self.shareholders_loc, number)

    def input_share_proportion(self, share_proportion):
        u"""输入借款人夫妻占股比例"""
        self.send_keys(self.share_proportion_loc, share_proportion)

    def select_business_isnormal(self, isnormal):
        u"""选择工商查询是否异常"""
        self.select_widget(isnormal, *self.isbusiness_except_loc)

    def select_borrower_iscontroler(self, iscontroler):
        u"""选择借款人是否为实际控制人"""
        self.select_widget(iscontroler, *self.iscontrolman_loc)

    def input_controler_name(self, name):
        u"""输入实际控制人名"""
        self.send_keys(self.controllername_loc, name)

    def select_yingye_mode(self, mode):
        u"""选择营业模式"""
        self.select_widget(mode, *self.business_mode_loc)

    def select_vocation_type(self, types):
        u"""选择行业类别"""
        self.select_widget(types, *self.vocation_type_loc)

    def input_start_time(self, date):
        u"""点击经营起始时间"""
        self.input_date_time(self.start_time_loc, date, click=False)

    def click_zhuti_submit_button(self):
        u"""点击提交按钮"""
        self.find_element(*self.zhuti_submit_loc).click()

    # --------------------------经营历史--------------------------------------------------------------------------------
    def click_history_add(self):
        u"""点击经营历史的增加按钮"""
        self.find_element(*self.history_add_button_loc).click()

    def click_years(self):
        u"""点击选择年份"""
        self.click_date_time(self.date_loc, self.iframe_loc, self.first_date_loc)
        # self.input_date_time(self.date_loc, year, clear=False)

    def input_jingli(self, jingli):
        u"""输入净利润"""
        self.send_keys(self.jingli_loc, jingli)

    def input_fuzhaizonge(self, fuzhaizonge):
        u"""输入负债总额"""
        self.send_keys(self.fuzhaizonge_loc, fuzhaizonge)

    def input_nianxiaoshoue(self, nianxiaoshoue):
        u"""输入年销售额"""
        self.send_keys(self.nianxiaoshoue_loc, nianxiaoshoue)

    def click_history_save_button(self):
        u"""点击经营历史页面的保存按钮"""
        self.find_element(*self.history_save_button_loc).click()
        time.sleep(1)

    # -----------------------------编辑近6个月营业额情况---------------------------------------------------------------
    def click_six_month_edit(self):
        u"""点击近6个月营业额页面的编辑按钮"""
        self.find_element(*self.edit_six_month_loc).click()

    def input_january(self, values):
        u"""输入1月份营业额"""
        self.send_keys(self.january_loc, values)

    def input_february(self, values):
        u"""输入2月份营业额"""
        self.send_keys(self.february_loc, values)

    def input_march(self, values):
        u"""输入3月份营业额"""
        self.send_keys(self.march_loc, values)

    def input_april(self, values):
        u"""输入4月份营业额"""
        self.send_keys(self.april_loc, values)

    def input_may(self, values):
        u"""输入5月份营业额"""
        self.send_keys(self.may_loc, values)

    def input_june(self, values):
        u"""输入6月份营业额"""
        self.send_keys(self.june_loc, values)

    def click_six_month_submit(self):
        u"""点击近6个月营业额情况页面的提交按钮"""
        self.find_element(*self.six_month_submit_loc).click()

    # -------------------编辑经营状况---------------------------------------------------------------------------
    def click_edit_status(self):
        u"""点击经营状况的编辑按钮"""
        self.find_element(*self.edit_status_loc).click()

    def input_personnel_number(self, number):
        u"""输入员工人数"""
        self.send_keys(self.personnel_number_loc, number)

    def input_month_pay(self, monthpay):
        u"""输入月工资支出"""
        self.send_keys(self.monthpay_loc, monthpay)

    def input_water_pay(self, waterpay):
        u"""输入水电费"""
        self.send_keys(self.waterpay_loc, waterpay)

    def input_other_pay(self, otherpay):
        u"""输入其他支出"""
        self.send_keys(self.otherpay_loc, otherpay)

    def input_transport_pay(self, transport):
        u"""输入运输支出"""
        self.send_keys(self.transport_loc, transport)

    def input_capital(self, capital):
        u"""输入年营业额"""
        self.send_keys(self.capital_loc, capital)

    def input_nianjinglirun(self, jinglirun):
        u"""输入年净利润"""
        self.send_keys(self.profit_loc, jinglirun)

    def input_should_pay(self, should_pay):
        u"""输入应付账款"""
        self.send_keys(self.pay_loc, should_pay)

    def input_collect(self, collect):
        u"""输入应收账款"""
        self.send_keys(self.collect_loc, collect)

    def input_liabilities(self, liabilities):
        u"""输入公司负债"""
        self.send_keys(self.liabilities_loc, liabilities)

    def input_invest(self, invest):
        u"""输入货币资金"""
        self.send_keys(self.invest_loc, invest)

    def click_bank_water(self):
        u"""点击银行流水"""
        el = self.find_element(*self.bank_water_loc)
        if not el.is_selected():
            el.click()

    def click_status_save_button(self):
        u"""点击经营状况页面的保存按钮"""
        self.find_element(*self.status_save_button_loc).click()
        time.sleep(1)

    # ----------------新增门店信息--------------------------------------------------------
    def scroll_to_store(self):
        u"""拖动页面到新增门店位置"""
        self.script(*self.store_add_button_loc)
        time.sleep(1)

    def click_store_add_button(self):
        u"""点击新增门店按钮"""
        self.find_element(*self.store_add_button_loc).click()

    def select_property_type(self, property_type):
        u"""选择产权性质"""
        self.select_widget(property_type, *self.propertytype_loc)

    def input_env_description(self, description):
        u"""输入门店经营环境描述"""
        self.send_keys(self.env_description_loc, description)

    def input_store_phone(self, phone):
        u"""输入门店电话"""
        self.send_keys(self.store_phone_loc, phone)

    def input_store_date(self, date):
        u"""点选门店成立日期"""
        self.input_date_time(self.store_date_loc, date)

    def select_store_addr_province(self, province):
        u"""选择门店地址所在省份"""
        self.select_widget(province, *self.store_addr_province_loc)

    def select_store_addr_city(self, city):
        u"""选择门店地址所在城市"""
        self.select_widget(city, *self.store_addr_city_loc)

    def input_store_addr_road(self, road):
        u"""输入门店地址详细信息"""
        self.send_keys(self.store_addr_road_loc, road)

    def input_business_area(self, area):
        u"""输入营业面积"""
        self.send_keys(self.businessarea_loc, area)

    def input_shoprent_year(self, shoprent_year):
        u"""输入年租金"""
        self.send_keys(self.shoprentyear_loc, shoprent_year)

    def input_shoprent_starttime(self, date):
        u"""点选租赁合同开始时间"""
        self.input_date_time(self.shoprentstarttime_loc, date)

    def input_shoprent_endtime(self, date):
        u"""点选租赁合同结束时间"""
        self.input_date_time(self.shoprentendtime_loc, date)

    def input_store_value(self, values):
        u"""输入存货价值预估"""
        self.send_keys(self.store_value_loc, values)

    def select_new_old(self, new_old):
        u"""选择装修新旧程度"""
        self.select_widget(new_old, *self.new_old_loc)

    def select_zhengqi(self, zhengqi):
        u"""选择货架是否整齐"""
        self.select_widget(zhengqi, *self.zhengqi_loc)

    def input_store_description(self, description):
        u"""输入存货效期描述"""
        self.send_keys(self.store_description_loc, description)

    def click_store_submit(self):
        u"""点击新增门店页面的提交按钮"""
        self.find_element(*self.store_commit_loc).click()
        time.sleep(1)

    # -----------编辑渠道数据-------------------------------------------------------------------
    def scroll_to_channel(self):
        u"""拖动页面到渠道数据位置"""
        self.script(*self.edit_channel_loc)
        time.sleep(1)

    def click_channel_edit_button(self):
        u"""点击渠道数据的编辑按钮"""
        self.find_element(*self.edit_channel_loc).click()

    def input_channel_product(self, product):
        u"""输入渠道产品"""
        self.send_keys(self.channel_product_loc, product)

    def input_month_hezuojine(self, jine):
        u"""输入月均合作金额"""
        self.send_keys(self.hezuojine_loc, jine)

    def click_channel_save_button(self):
        u"""点击渠道数据页面的保存按钮"""
        self.find_element(*self.channel_save_button_loc).click()
        time.sleep(1)

    # 蔬果渠道数据
    def scroll_to_fruits_channel(self):
        u"""拖动页面到编辑渠道数据"""
        self.script(*self.startOperateTime_loc)
        time.sleep(1)

    def input_startoperatetime(self, date):
        u"""点选本市场经营开始时间"""
        self.input_date_time(self.startOperateTime_loc, date)

    def select_isParking(self, isparking):
        u"""选择档口有无车位"""
        self.select_widget(isparking, *self.isParking_loc)

    # 商超渠道数据
    def scroll_to_shangchao_channel(self):
        u"""拖动页面到商超的渠道数据位置"""
        self.script(*self.whitelistTime_loc)
        time.sleep(1)

    def input_whitelisttime(self, date):
        u"""点选与白名单内商超合作开始时间"""
        self.input_date_time(self.whitelistTime_loc, date, click=False)

    # -----------增加上游信息-------------------------------------------------------------------
    def click_shangyou_add_button(self):
        u"""点击上游信息的新增按钮"""
        self.find_element(*self.shangyou_add_loc).click()

    def input_supplier(self, supplier):
        u"""输入重要供应商"""
        self.send_keys(self.supplier_loc, supplier)

    def input_hezuo_product(self, product):
        u"""输入合作产品"""
        self.send_keys(self.hezuo_product_loc, product)

    def input_caigouzhanbi(self, caigouzhanbi):
        u"""输入采购占比"""
        self.send_keys(self.caigouzhanbi_loc, caigouzhanbi)

    def input_zhangqi(self, zhangqi):
        u"""输入账期"""
        self.send_keys(self.zhangqi_loc, zhangqi)

    def click_shangyou_save_button(self):
        u"""点击上游信息页面的保存按钮"""
        self.find_element(*self.shangyou_save_button_loc).click()
        time.sleep(1)

    # 蔬果上游信息
    def select_isOwnFarm(self, isownfarm):
        u"""选择是否有自有农场"""
        self.select_widget(isownfarm, *self.isOwnFarm_loc)

    def select_isFarmer(self, isfarmer):
        u"""选择是否向固定农户采购"""
        self.select_widget(isfarmer, *self.isFarmer_loc)

    def select_isOtherPurchase(self, isotherpurchase):
        u"""选择是否向其他供菜商采购"""
        self.select_widget(isotherpurchase, *self.isOtherPurchase_loc)

    def select_farme_address_province(self, farme_address_province):
        u"""选择自有农场地址省份"""
        self.select_widget(farme_address_province, *self.farme_address_province_loc)

    def select_farme_address_city(self, farme_address_city):
        u"""选择自有农场地址城市"""
        self.select_widget(farme_address_city, *self.farme_address_city_loc)

    def input_farme_address_road(self, farme_address_road):
        u"""输入自有农场详细地址"""
        self.send_keys(self.farme_address_detailAddress_loc, farme_address_road)

    def input_othermode(self, othermode):
        u"""输入其他方式说明"""
        self.send_keys(self.otherModeRemark_loc, othermode)

    # 蔬果下游信息
    def input_twobatch(self, twobatch):
        u"""输入二批商近六个月销售量"""
        self.send_keys(self.six_month_sales_twobatch_loc, twobatch)

    def input_supermarket(self, supermarket):
        u"""输入商超近六个月销售量"""
        self.send_keys(self.six_month_sales_supermarket_loc, supermarket)

    def input_groupPurch(self, grouppurch):
        u"""输入团购近六个月销售量"""
        self.send_keys(self.six_month_sales_groupPurch_loc, grouppurch)

    def input_directRetail(self, directRetail):
        u"""输入直接零售近六个月销售量"""
        self.send_keys(self.directRetail_loc, directRetail)

    def input_retail(self, retail):
        u"""输入零售终端近六个月销售量"""
        self.send_keys(self.six_month_sales_retail_loc, retail)

    def click_fruits_save_button(self):
        self.find_element(*self.fruits_save_button_loc).click()
        time.sleep(1)

    # 商超十大下游客户近6月供货量
    def click_xiayou_add(self):
        u"""点击十大下游客户近6月供货量的增加按钮"""
        self.find_element(*self.xiayou_add_button_loc).click()

    def input_custom_name(self, custom_name):
        u"""输入客户名称"""
        self.send_keys(self.cusName_loc, custom_name)

    def input_jiesuanzhangqi(self, jiesuanzhangqi):
        u"""输入结算账期"""
        self.send_keys(self.settlementDate_loc, jiesuanzhangqi)

    def input_gonghuoliang(self, gonghuoliang):
        u"""输入供货量"""
        self.send_keys(self.supplyQuantity_loc, gonghuoliang)

    def click_xiayou_save_button(self):
        u"""点击保存按钮"""
        self.find_element(*self.xiayou_save_button_loc).click()
        time.sleep(1)

    # -----------增加主要销售产品-------------------------------------------------------------------
    def scroll_to_main_product(self):
        u"""拖动页面到主要销售产品位置"""
        self.script(*self.main_product_add_loc)
        time.sleep(1)

    def click_main_product_add(self):
        u"""点击主要销售产品页面的新增按钮"""
        self.find_element(*self.main_product_add_loc).click()

    def input_main_product_name(self, product_name):
        u"""输入产品名称"""
        self.send_keys(self.product_name_loc, product_name)

    def input_brand(self, brand):
        u"""输入品牌名称"""
        self.send_keys(self.brand_loc, brand)

    def input_buyin_price(self, price):
        u"""输入进货价"""
        self.send_keys(self.buyingprice_loc, price)

    def input_model(self, model):
        u"""输入型号"""
        self.send_keys(self.model_loc, model)

    def input_selling_price(self, price):
        u"""输入销售价"""
        self.send_keys(self.sellingprice_loc, price)

    def input_lastmonth_sales(self, sales):
        u"""输入上月销量"""
        self.send_keys(self.lastmonthsales_loc, sales)

    def click_main_product_save_button(self):
        u"""点击主要销售产品页面的保存按钮"""
        self.find_element(*self.product_save_button_loc).click()
        time.sleep(1)

    # 蔬果主要销售产品
    def click_fruits_main_product_add(self):
        u"""点击蔬果主要销售产品的增加按钮"""
        self.find_element(*self.fruits_main_product_add_loc).click()

    def input_fruits_product_name(self, fruits_product_name):
        u"""输入蔬果的产品名称"""
        self.send_keys(self.fruits_product_name_loc, fruits_product_name)

    def click_fruits_chandi(self):
        u"""点选择蔬果产地"""
        self.find_element(*self.productionAddress_loc).click()

    def input_last_six_month_sales(self, last_six_month_sales):
        u"""输入蔬果最近6个月的销售情况"""
        self.send_keys(self.lastMonthSaleNum_loc, last_six_month_sales)

    def click_fruits_main_product_save(self):
        u"""点击蔬果主要销售产品页面的保存按钮"""
        self.find_element(*self.fruits_main_product_save_loc).click()
        time.sleep(1)

    # 商超十大销售产品
    def click_shangchao_product_add(self):
        u"""点击十大销售产品的新增按钮"""
        self.find_element(*self.sale_product_add_loc).click()

    def input_productBrand(self, productBrand):
        u"""输入产品品牌"""
        self.send_keys(self.productBrand_loc, productBrand)

    def input_productType(self, productType):
        u"""输入产品类型"""
        self.send_keys(self.productType_loc, productType)

    def input_dailizizhi(self, dailizizhi):
        u"""输入代理资质"""
        self.send_keys(self.agentQuali_loc, dailizizhi)

    def input_hezuoqixian(self, hezuoqixian):
        u"""输入合作期限"""
        self.send_keys(self.coopTerm_loc, hezuoqixian)

    def input_y_saleTask(self, y_saleTask):
        u"""输入年销售任务"""
        self.send_keys(self.y_saleTask_loc, y_saleTask)

    def click_sale_product_save(self):
        u"""点击保存按钮"""
        self.find_element(*self.sale_product_save_loc).click()
        time.sleep(1)

    # -----------编辑贷款信息-------------------------------------------------------------------
    def scroll_to_loan_info(self):
        u"""拖动页面到贷款信息位置"""
        self.script(*self.loan_time_loc)
        time.sleep(1)

    def select_loan_time(self, long):
        u"""选择贷款期限"""
        self.select_widget(long, *self.loan_time_loc)

    def select_huankuan_type(self, types):
        u"""选择还款方式"""
        self.select_widget(types, *self.huankuan_type_loc)

    def select_loan_yongtu(self, yongtu):
        u"""选择贷款用途"""
        self.select_widget(yongtu, *self.loan_yongtu_loc)

    def input_eamount(self, eamount):
        u"""输入EA批复额度"""
        self.send_keys(self.eamount_loc, eamount)

    def select_loan_bankname(self, bankname):
        u"""选择送审银行"""
        self.select_widget(bankname, *self.bankloanname_loc)

    def select_tuijian_type(self, types):
        u"""选择推荐类型"""
        self.select_widget(types, *self.tuijian_type)

    def input_tuijian_name(self, name):
        u"""输入内部推荐人"""
        self.send_keys(self.tuijian_name_loc, name)
        self.find_element(*self.first_name_loc).click()

    def select_danbao_type(self, types):
        u"""选择担保方式"""
        self.select_widget(types, *self.danbao_type_loc)

    def click_loan_info_save(self):
        u"""点击贷款信息页面的保存按钮"""
        self.find_element(*self.loan_save_loc).click()
        time.sleep(1)

    def click_loan_info_confirm(self):
        u"""点击确认按钮"""
        self.find_element(*self.loan_confirm_loc).click()
        time.sleep(1)

    def click_submit_inside_approve(self):
        u"""点击提交内审按钮"""
        self.find_element(*self.conmmit_inside_approve_loc).click()

# coding=utf-8
import random
import time

import logging

from selenium.webdriver import ActionChains

from utils.mytestcase import MyTestCase
from utils.logincookie import dengLuPage
from utils.random import Unicode
from utils.screenshort import get_screenshort


class HwGsTest(MyTestCase):
    """海外高速测试集"""

    def test_hwgs_1(self):
        """海外高速测试"""

        # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        #                     format='[%(asctime)s-%(filename)s-%(levelname)s: %(message)s]', level=logging.DEBUG,
        #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
        dl = dengLuPage(self.driver)
        # 官方推荐有find_element(By.*(""))代替find_element_by_*("")
        # self.driver.find_element_by_id()
        # self.driver.find_element()
        dl.dengLu()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > div > dl:nth-child(3) > dd > a:nth-child(4)").click()
        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        time.sleep(3)
        self.assertIn("海外公司智能注册-权大师", self.driver.title)
        print(self.driver.title)
        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-serviceItems > table > tbody > tr > td.td-cont > ul > li:nth-child(4)").click()
        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:"+a.text)
            aa=a.text
        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        ss=Unicode()

        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page.smartRegister3-page > div:nth-child(4) > div > table > tbody > tr.row-name > td.td-content > input").send_keys(
            "{}".format(ss))
        print("商标名称：{}".format(ss))
        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page.smartRegister3-page > div:nth-child(4) > div > table > tbody > tr.row-tuyang.show-create.show-create1 > td.td-content > div.zidongdong-create > ul > li > div.bottom.getBrandPic > a").click()
        self.driver.find_element_by_css_selector("#create-tuyang > label.label.checked").click()
        time.sleep(5)

        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page.smartRegister3-page > div:nth-child(14) > div.categoryInfo-wrap > div.c-row.row-way > div > a.btn-choice.active").click()
        suiji=random.randint(2,46)
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li:nth-child({}) > span".format(suiji)).click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(1) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(2) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(3) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(4) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(5) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(6) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(7) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(8) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(9) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(10) > span").click()
        print("选择了第{}类商标分类！".format(suiji))
        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page.smartRegister3-page > div.last-pay > ul > li.row-step > a").click()

        time.sleep(1)

        # 企业 国外

        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").send_keys(
            "{}".format(Unicode()))
        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(2) > td.td-content > input").send_keys(
            "tesr")
        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(3) > td.td-content.fcountry-container > input.myInput").click()
        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(3) > td.td-content.fcountry-container > div > div.country-list.country-list-ag.active > span:nth-child(1)").click()
        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(4) > td.td-title").click()
        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(4) > td.td-content > input").send_keys(
            "test01")
        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(5) > td.td-content > input").send_keys(
            "test01")
        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(6) > td.td-content > input").send_keys(
            "test02")
        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(7) > td.td-content > input").send_keys(
            "15624992422")
        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-qiye > tr:nth-child(8) > td.td-content > input").send_keys(
            "4654564@qq.com")
        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap.overseas > div.section-btns.clearfix > a:nth-child(2)").click()

        """订单备注"""
        self.driver.find_element_by_css_selector(
            "html body div.smartRegister-page div.orderinfo-wrap div.order-content textarea").send_keys(
            time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")



        get_screenshort(self.driver, "test_hwgs_1.png")
        for i in self.driver.find_elements_by_css_selector("body > div.smartRegister-page > div.orderinfo-wrap > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):
            print("总价:"+i.text)
            ii=i.text

        self.assertIn(aa,ii)
        print("价格一致")
        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page > div.orderinfo-wrap > div.last-pay.personal-last-pay > div > a").click()
        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:"+o.text)
            oo=o.text

        self.assertIn(oo,ii)

        print("测试通过")
        self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_hwgs_2(self):
        """海外高速_自然人测试"""

        # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        #                     format='[%(asctime)s-%(filename)s-%(levelname)s: %(message)s]', level=logging.DEBUG,
        #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
        dl = dengLuPage(self.driver)
        # 官方推荐有find_element(By.*(""))代替find_element_by_*("")
        # self.driver.find_element_by_id()
        # self.driver.find_element()
        dl.dengLu()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > div > dl:nth-child(3) > dd > a:nth-child(4)").click()
        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        time.sleep(3)
        self.assertIn("海外公司智能注册-权大师", self.driver.title)
        print(self.driver.title)
        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-serviceItems > table > tbody > tr > td.td-cont > ul > li:nth-child(4)").click()
        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:"+a.text)
            aa=a.text
        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        ss=Unicode()
        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page.smartRegister3-page > div:nth-child(4) > div > table > tbody > tr.row-name > td.td-content > input").send_keys(
            "{}".format(ss))
        print("商标名称：{}".format(ss))
        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page.smartRegister3-page > div:nth-child(4) > div > table > tbody > tr.row-tuyang.show-create.show-create1 > td.td-content > div.zidongdong-create > ul > li > div.bottom.getBrandPic > a").click()
        self.driver.find_element_by_css_selector("#create-tuyang > label.label.checked").click()
        time.sleep(5)

        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page.smartRegister3-page > div:nth-child(14) > div.categoryInfo-wrap > div.c-row.row-way > div > a.btn-choice.active").click()
        suiji=random.randint(2,46)
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li:nth-child({}) > span".format(suiji)).click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > span").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(1) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(2) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(3) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(4) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(5) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(6) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(7) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(8) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(9) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(10) > span").click()
        print("选择了第{}类商标分类！".format(suiji))


        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page.smartRegister3-page > div.last-pay > ul > li.row-step > a").click()

        time.sleep(1)

        # 企业 自然人

        self.driver.find_element_by_css_selector("body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base > table > thead > tr:nth-child(1) > td.td-content > a:nth-child(2)").click()
        self.driver.find_element_by_css_selector("body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base.open > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-gsh > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").send_keys("{}".format(Unicode()))
        self.driver.find_element_by_css_selector("body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base.open > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-gsh > tr:nth-child(2) > td.td-content > input").send_keys("dalao")
        self.driver.find_element_by_css_selector("body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base.open > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-gsh > tr:nth-child(4) > td.td-content > input").send_keys("140121199506133513")
        self.driver.find_element_by_css_selector("body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base.open > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-gsh > tr:nth-child(5) > td.td-content.fcountry-container > input.myInput").click()
        self.driver.find_element_by_css_selector("body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base.open > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-gsh > tr:nth-child(5) > td.td-content.fcountry-container > div > div.country-list.country-list-ag.active > span:nth-child(1)").click()
        self.driver.find_element_by_css_selector("body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base.open > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-gsh > tr:nth-child(5) > td.td-title").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base.open > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-gsh > tr:nth-child(6) > td.td-content > input").send_keys("外国人")
        self.driver.find_element_by_css_selector("body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base.open > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-gsh > tr:nth-child(7) > td.td-content > input").send_keys("waiguoren")
        self.driver.find_element_by_css_selector("body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base.open > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-gsh > tr:nth-child(8) > td.td-content > input").send_keys("laotie")
        self.driver.find_element_by_css_selector("body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base.open > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-gsh > tr:nth-child(9) > td.td-content > input").send_keys("17801188215")
        self.driver.find_element_by_css_selector("body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base.open > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-gsh > tr:nth-child(10) > td.td-content > input").send_keys("1456470136@qq.com")
        self.driver.find_element_by_css_selector("body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap.overseas > div.section-base.open > div.overseas-form > table.table-1.table-overseas.table-type2.active > tbody.tbody-gsh > tr:nth-child(11) > td.td-content > input").send_keys("03515925212")

        self.driver.find_element_by_css_selector("body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap.overseas > div.section-btns.clearfix > a:nth-child(2)").click()
        time.sleep(2)

        """订单备注"""
        self.driver.find_element_by_css_selector(
            "html body div.smartRegister-page div.orderinfo-wrap div.order-content textarea").send_keys(
            time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")



        get_screenshort(self.driver, "test_hwgs_2.png")
        for i in self.driver.find_elements_by_css_selector("body > div.smartRegister-page > div.orderinfo-wrap > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):
            print("总价:"+i.text)
            ii=i.text

        self.assertIn(aa,ii)
        print("价格一致")
        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page > div.orderinfo-wrap > div.last-pay.personal-last-pay > div > a").click()
        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:"+o.text)
            oo=o.text

        self.assertIn(oo,ii)

        print("测试通过")
        self.driver.find_element_by_css_selector("#alisubmit").click()
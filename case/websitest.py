import re
import time

import requests

from utils.logincookie import dengLuPage
from utils.mytestcase import MyTestCase
from utils.random import Unicode


class WebSiTest(MyTestCase):
    """相似商标个数测试集"""
    def test_number1(self):

        """网站地图测试"""

        dl = dengLuPage(self.driver)
        dl.dengLu()
        time.sleep(2)
        self.driver.find_element_by_css_selector("body > div.footer-wrap > div > ul.items-2 > li:nth-child(7) > a").click()
        # url = 'https://pre-www.quandashi.com/site-map/index'
        # r = requests.get(url)
        # r.encoding = 'gb2312'
        #
        # # 利用 re （太黄太暴力！）
        # matchs = re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')", r.text)
        # for link in matchs:
        #     print(link)

        for link in self.driver.find_elements_by_tag_name("a"):
            print(link.get_attribute("href"))
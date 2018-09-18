from selenium import webdriver
from selenium.webdriver import ActionChains
from pandas import *
import time

op = webdriver.ChromeOptions()
prefs = {
    "profile.default_content_setting_values.plugins": 1,
    "profile.content_settings.plugin_whitelist.adobe-flash-player": 1,
    "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1,
    "PluginsAllowedForUrls": "https://url.com"
}

op.add_experimental_option("prefs",prefs)
op.add_argument("--window-size=2560,1600")
dr = webdriver.Chrome('/Users/joono/chromedriver',chrome_options=op)

dr.get('http://www.kta.or.kr/index.asp')
time.sleep(2)
dr.switch_to.window(dr.window_handles[0])
# dr.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[3]/a').click()
# dr.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[3]/a').click()
dr.switch_to.frame(dr.find_element_by_css_selector('frame[name="subFrame"]'))
time.sleep(2)
dr.find_element_by_xpath('/html/body/table/tbody/tr[4]/td[1]/table/tbody/tr/td[1]/table/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td/table/tbody/tr/td[3]/input').click()
dr.find_element_by_xpath('/html/body/table/tbody/tr[4]/td[1]/table/tbody/tr/td[1]/table/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/input').send_keys('tsgl')
dr.find_element_by_xpath('/html/body/table/tbody/tr[4]/td[1]/table/tbody/tr/td[1]/table/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/input').send_keys('1022')
dr.find_element_by_xpath('/html/body/table/tbody/tr[4]/td[1]/table/tbody/tr/td[1]/table/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr[1]/td[3]/input').click()
time.sleep(2)
for page in range(1,2):
    url = 'http://www.kta.or.kr/Mem/mem_db.asp?OC=&OV=&OB=&Tblname=&searchPart=&searchtext=&page='+str(page)
    dr.get(url)
    table = dr.find_elements_by_css_selector('table[cellspacing="4"]')
    for cont in table:
        text = cont.text

from bs4 import BeautifulSoup
from selenium import webdriver
import time
dr = webdriver.Chrome('/Users/joono/chromedriver')

dr.get('https://domain.whois.co.kr/')
dr.find_element_by_xpath('//*[@id="Text1"]').send_keys('금형제작')
dr.find_element_by_xpath('//*[@id="Image1"]').click()
time.sleep(3)
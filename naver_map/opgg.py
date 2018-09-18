from bs4 import BeautifulSoup
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


executable_path = '/Users/joono/chromedriver'
os.environ["webdriver.chrome.driver"] = executable_path
chrome_options = Options()
chrome_options.add_extension('/Users/joono/AdBlock_v3.23.0.crx')

dr = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)
dr.get('http://www.op.gg/summoner/userName=%EC%AD%88%EB%85%B8%EC%AE%B8%EB%85%B8')
time.sleep(1)
dr.get('http://www.op.gg/summoner/userName=%EC%AD%88%EB%85%B8%EC%AE%B8%EB%85%B8')

dr.find_element_by_xpath('//*[@id="SummonerLayoutContent"]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div[1]/div[7]/div/div/a/span[1]').click()
time.sleep(1)
dr.find_element_by_xpath('//*[@id="SummonerLayoutContent"]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/ul/li[2]/a').click()
time.sleep(1)
dr.find_element_by_xpath('//*[@id="SummonerLayoutContent"]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/ul/li[3]/a').click()
time.sleep(1)
dr.find_element_by_xpath('//*[@id="SummonerLayoutContent"]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/ul/li[4]/a').click()
time.sleep(1)
drt = dr.page_source
soup = BeautifulSoup(drt,'html.parser')
bars = soup.find_all('script')
bars_text = []
for i in bars:
    bars_text.append(i.text)
print(bars_text)
dr.quit()
from selenium import webdriver
from bs4 import BeautifulSoup
from pandas import *
import time
import re
dt = read_excel('행정구역코드(법정동코드)_전체본.xls',0)
dt_dong = dt['법정동명']
dt_dong_new = []
for i in dt_dong:
    if i[-1] == '동':
        dt_dong_new.append(i)
query = []

for i in dt_dong_new:
    query.append(i+' 제조업 > 기계, 장비제조')


names = []
tels = []
addrss = []

dr = webdriver.Chrome('/Users/joono/chromedriver')
dr.get('https://map.naver.com/')

dr.find_element_by_xpath('//*[@id="search-input"]').send_keys(query[0])

dr.find_element_by_xpath('//*[@id="header"]/div[1]/fieldset/button').click()

time.sleep(1)


drt = dr.page_source
soup = BeautifulSoup(drt,'html.parser')
num = soup.find('span',attrs = {'class':'n'}).text[]
whole = soup.find_all('dl',attrs={'class':'lsnx_det'})

for i in whole:
    print(str(i))
    i = str(i)
    if 'href=\"#\">' in i:
        name = i.split('href="#">')[1].split('</a>')[0]
        names.append(name.strip())
    else:
        names.append('없음')
    if 'class=\"addr\">' in i:
        addr = i.split('class="addr">')[1].split('<a')[0]
        addrss.append(addr.strip())
    else:
        addrss.append('없음')
    if 'class=\"tel\">' in i:
        tel1 = i.split('class="tel">')[1].split('</dd>')[0]
        tels.append(tel1.strip())
    else:
        tels.append('없음')



print(names)
print(tels)
print(addrss)
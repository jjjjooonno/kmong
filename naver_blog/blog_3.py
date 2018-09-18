from bs4 import BeautifulSoup
from selenium import webdriver
import time
import datetime
from pandas import *

''' 필요 패키지 및 파일
1. bs4
2. selenium
3. pandas
4. chromedriver -> 구글에 크롬드라이버 검색하셔서 윈도우 버젼에 맞는 것을 설치해주시면 됩니다. 
'''

driver_path = ''
# 크롬드라이버의 설치 경로(폴더 주소)를 넣어주세요!

dr = webdriver.Chrome(driver_path+'/Users/joono/chromedriver')
# 설치경로를 넣어주셨다면 /Users/joono를 지워주시고 /chromedriver만 남겨주세요
url = 'https://search.naver.com/search.naver?where=post&sm=tab_jum&query='
keyword = '테일즈런너'
# 블로그 검색 키워드입니다. 키워드를 변경해서 넣어주시면 됩니다.

dr.get(url+keyword)
time.sleep(2)

begin_date = '2018.05.01'
end_date = '2018.05.07'
# 기간을 설정하는 변수들 입니다. begin_date~end_date까지의 게시물만 검색결과로 표현합니다.
dr.find_element_by_xpath('//*[@id="_search_option_btn"]').click()
dr.find_element_by_xpath('//*[@id="snb"]/div/ul/li[2]/a').click()
time.sleep(5)

dr.execute_script("document.getElementById('blog_input_period_begin').value='{0}'".format(begin_date))
time.sleep(5)
dr.execute_script("document.getElementById('blog_input_period_end').value='{0}'".format(end_date))
dr.find_element_by_xpath('//*[@id="_nx_option_date"]/div/span/button').click()
dr.find_element_by_xpath('//*[@id="nx_option_mson"]').click()
time.sleep(5)

title_list = []
date_list = []
contents_list = []
link = []

pnum = int(int(''.join(dr.find_element_by_class_name('title_num').text.split('/')[1].split(','))[1:-1])//10)+1
print(pnum)
for num in range(0,pnum):
    blogs = dr.find_elements_by_css_selector("a[class^=\"sh_blog_title\"]")
    for blog in blogs:
        link_url = blog.get_attribute('href')
        blog.click()
        dr.switch_to.window(dr.window_handles[1])
        time.sleep(1)
        try:
            dr.switch_to.frame(dr.find_element_by_id('mainFrame'))
        except:
            try:
                dr.switch_to.frame(dr.find_element_by_id('screenFrame'))
                dr.switch_to.frame(dr.find_element_by_id('mainFrame'))
            except:
                pass
        drt = dr.page_source

        soup = BeautifulSoup(drt,'html.parser')
        try:
            title = soup.find('div',attrs = {'class' : 'htitle'}).text
            date = soup.find('p',attrs = {'class' : 'date fil5 pcol2 _postAddDate'}).text
            try:
                content = soup.find('div',attrs = {'id' : 'postViewArea'}).text
            except:
                case_b = []
                content = soup.find_all('p', attrs= {'class': '0'})
                for c in content:
                    case_b.append(c.text)
                content = ''.join(case_b)
        except:
            try:
                title = soup.find('h3', attrs={'class': 'se_textarea'}).text
                date = soup.find('span', attrs={'class': 'se_publishDate pcol2 fil5'}).text
                content = soup.find('div', attrs={'class': 'se_component_wrap sect_dsc __se_component_area'}).text
            except:
                try:
                    title = soup.find('h2').text
                    date = soup.find('span', attrs={'class': 'date'}).text
                    content = soup.find('div', attrs={'class': 'tt_article_useless_p_margin'}).text
                except:
                    pass
        if (title == '') or (date == '') or (link_url == '') or (content == ''):
            pass
        else:
            try:
                title_list.append(title.strip())
                date_list.append(date)
                contents_list.append(content.strip())
                link.append(link_url)
            except:
                pass
        dr.close()
        dr.switch_to.window(dr.window_handles[0])
        title = ''
        date = ''
        link_url = ''
        content = ''
    try:
        next_button = dr.find_element_by_class_name('next')
        next_button.click()
    except:
        pass

'''
검색 결과에서 블로그 링크를 하나하나 타고 들어가서 제목, 본문, 게시일자를 가져옵니다.

양식이 다른 블로그 대부분을 담으려고 했으나, 가끔 개인 블로그를 운영하시는 분들의 블로그 내용은 HTML 태그가 달라 제외하는 방식으로 코드를 구성했습니다.
혹시 이용하시려는 블로그가 있으시면 A/S로 코드를 추가해 드리겠습니다.
'''

data_frame = DataFrame({'title' : title_list,
                        'date' : date_list,
                        'contents' : contents_list,
                        'link' : link})
data_frame.drop_duplicates(subset = 'title')
data_frame.to_excel(keyword+datetime.now().strftime('%Y-%m-%d %H%M%S'+'.xlsx'))
# 결과 파일은 키워드2018-05-01 17-40-23.xlsx 와 같은 형식으로 파일명이 저장됩니다.
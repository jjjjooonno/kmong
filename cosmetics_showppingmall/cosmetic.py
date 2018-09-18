from selenium import webdriver
import time

dr = webdriver.Chrome('/Users/joono/chromedriver')
products = ['skincare','makeup','cleansing','body-and-hair']
for product in products:
    url = 'https://www.roseroseshop.com/'+product+'?page='
    dr.get(url+str(1))
    page_range = int(dr.find_element_by_css_selector('div[class = "results"]').text.split('(')[1].split('P')[0][:-1])
    print(page_range)
    for page in range(1,3):
        dr.get(url+str(page))
        whole = dr.find_element_by_css_selector('div[class="product-grid"]')
        rows = whole.find_elements_by_css_selector('div[class="row"]')
        item_url = []
        for row in rows:
            imgs = row.find_elements_by_css_selector('div[class = "image"')
            for img in imgs:
                link = img.find_element_by_tag_name('a')
                item_url.append(link.get_attribute('href'))
        for url in item_url:
            dr.get(url)
            print()
            time.sleep(2)
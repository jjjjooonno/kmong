from pandas import DataFrame, read_csv
from bs4 import BeautifulSoup
import urllib.request
import json
price = []
year_df = []
add = []
ptnum = read_csv('ptnum.csv')
ptnums = list(ptnum['num'])
years = ['2013','2014','2015','2016','2017']
for year in years:
    for num in ptnums:
        url = 'http://apis.data.go.kr/1611000/nsdi/ReferLandPriceService/attr/getReferLandPriceAttr?serviceKey=XGjk3lw3HWVPQUnt%2FbK0ps7Oun48a%2FVgEb0n1PnbqqERTRXj2wwdybeabsJBVinRb2braJKLp9y0jGc8RpQAdw%3D%3D&ldCode={0}&stdrYear={1}&format=json&numOfRows=999&pageSize=999&pageNo=1&startPage=1'.format(num,year)
        data = urllib.request.urlopen(url).read().decode('utf8')
        data_json = json.loads(data)
        parsed_json = data_json['referLandPrices']['field']

        for i in parsed_json:
            print(i)
            price.append(i['pblntfPclnd'])
            year_df.append(i['stdrYear'])
            add.append(i['ldCodeNm'])

dt = DataFrame({'price' : price, 'year' : year_df,'address':add})

dt.to_csv('ptprices.csv')
from pandas import DataFrame
from bs4 import BeautifulSoup
import urllib.request

years = ['2013','2014','2015','2016','2017']
months = ['01','02','03','04','05','06','07','08','09','10','11','12']
date_list = []
address = []
prices = []
for year in years:
    for month in months:
        date = year+month
        url = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcLandTrade?&type=json&serviceKey=XGjk3lw3HWVPQUnt%2FbK0ps7Oun48a%2FVgEb0n1PnbqqERTRXj2wwdybeabsJBVinRb2braJKLp9y0jGc8RpQAdw%3D%3D&LAWD_CD=41220&DEAL_YMD={0}'.format(date)
        p = urllib.request.urlopen(url)
        soup = BeautifulSoup(p,'lxml')
        for i in soup.find_all('item'):
            group = str(i).split('&gt;')
            print(group)
            price = group[0][6:-4].replace(",", "")
            pyung = group[1][:-4].replace(",", "")
            prices.append(int(price)/int(pyung))
            date_list.append(year)
            if group[3]==year + '년':
                address.append(group[4][:-3])
            else:
                address.append(group[3][:-3])
dt = DataFrame({'date' : date_list,'price' : prices,'address':address})
dt.to_csv('pyungteak_sil.csv')
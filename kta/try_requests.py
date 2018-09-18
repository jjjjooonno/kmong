import requests
from bs4 import BeautifulSoup

for page in range(1,2):
    url = 'http://www.kta.or.kr/Mem/mem_db.asp?OC=&OV=&OB=&Tblname=&searchPart=&searchtext=&page='+str(page)
    if page !=1:
        header = {
        'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8',
        'Accept - Encoding' : 'gzip, deflate',
        'Accept - Language' : 'ko - KR, ko; q = 0.9, en - US; q = 0.8, en; q = 0.7',
        'Connection' : 'keep - alive',
        'Cookie' : 'ASPSESSIONIDSACSRSRC = LOHJEDFDODNINLIODBFPMHJD; DOA_1679 = done; DOA_1724 = done',
        'Host': 'www.kta. or.kr',
        'Referer': 'http: // www.kta. or.kr / Mem / mem_db.asp?OC = & OV = & OB = & Tblname = & searchPart = & searchtext = & page = '+str(page-1),
        'Upgrade - Insecure - Requests': '1',
        'User - Agent': 'Mozilla / 5.0(Macintosh; Intel Mac OS X 10_13_4) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 67.0 .3396 .87 Safari / 537.36'
        }
    else:
        header = {
            'Cookie': 'ASPSESSIONIDSACSRSRC = LOHJEDFDODNINLIODBFPMHJD; DOA_1679 = done; DOA_1724 = done',
        }
    r = requests.get(url)
    print(url)
    rcod = r.status_code
    print(rcod)
    if(rcod==200):
        print(r.text)
        soup = BeautifulSoup(r.text,'html.parser')
        tr = soup.find_all('table',attrs=({'width' : '660','border' : '0','cellspacing' : '4','cellpadding' : '0'}))
        print(tr)
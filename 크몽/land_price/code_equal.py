from pandas import *
dt_gong = read_csv('ptgong.csv')
dt_sil = read_csv('ptsil.csv')
dt_code = read_csv('ptcodes.csv')
codes = [[],[]]
# for i in range(dt_code['address']):
#     codes[0].append(dt_code['address'][i])
#     codes[1].append(dt_code['codes'][i])
# gong_codes = []
# for j in range(0,dt_gong['newaddress']):
#     idx = codes[0].index(dt_gong['newaddress'][j])

dt_gong_gb = dt_gong.groupby(['year','newaddress']).mean()
print(dt_gong_gb.head())
dt_gong_gb['price'].to_excel('gb_gong.xlsx')
dt_sil_gb = dt_sil.groupby(['date','newaddress']).mean()
print(dt_sil_gb.head())
dt_sil_gb['price'].to_excel('gb_sil.xlsx')
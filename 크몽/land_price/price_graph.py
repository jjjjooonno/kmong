from pandas import *
dt = read_csv('2017_gong.csv',encoding = 'cp949')
dt_1 = dt[dt['시군구명'] == '평택시']

print(dt_1.head())
dt_1.to_csv('gong_17.csv')
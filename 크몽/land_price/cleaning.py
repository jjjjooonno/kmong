from pandas import *
dt = read_csv('pyungteak_sil.csv')
print(dt.head())
dt_gijun =read_excel('행정구역코드(법정동코드)_전체본.xls',0)
print(dt_gijun.head())
addresses = unique(dt['address'])
print(addresses)
new_add = []
for i in addresses:
    if '면' in i:
        new_name = i.split('면')[0]+'면'
        new_add.append(new_name)
    elif '읍' in i :
        new_name = i.split('읍')[0] + '읍'
        new_add.append(new_name)
    else:
        new_add.append(i)
new_add = unique(new_add)
print(new_add)
add_dict = {}
for i in new_add:
    for j in range(0,len(dt_gijun['법정동명'])):
        if (i in dt_gijun.ix[j,'법정동명']) & ('평택' in dt_gijun.ix[j,'법정동명']) & (dt_gijun.ix[j,'법정동명'][-1] != '리'):
            add_dict.update({dt_gijun.ix[j,'법정동명'] : dt_gijun.ix[j,'법정동코드']})
    print('{0}cycle'.format(list(new_add).index(i)))
print(add_dict)

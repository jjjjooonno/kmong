from pandas import *
dt_gong = read_csv('ptprices.csv')
dt_sil = read_csv('pyungteak_sil.csv')
dt_code = read_csv('ptcodes.csv')

new_gong_add = []
new_sil_add = []

for i in dt_gong['address']:
    i = str(i)
    if i[-1] == '리':
        new_gong_add.append(i.split(' ')[-2].strip())
    else:
        new_gong_add.append(i.split(' ')[-1].strip())
for j in dt_sil['address']:
    j = str(j)
    if j[-1] == '리':
        new_sil_add.append(j.split(' ')[-2].strip())
    else:
        new_sil_add.append(j.split(' ')[-1].strip())
dt_gong['newaddress'] = new_gong_add
dt_sil['newaddress'] = new_sil_add
print(type(new_gong_add[2466]))
dt_gong = dt_gong[dt_gong.newaddress != 'nan']
dt_sil = dt_sil[dt_sil.newaddress != 'nan']

dt_gong.to_csv('ptgong.csv')
dt_sil.to_csv('ptsil.csv')
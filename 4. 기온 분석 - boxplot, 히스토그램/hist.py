import csv
import matplotlib.pyplot as plt

f = open('seoul.csv')
data = csv.reader(f)
next(data)
winter = []
summer = []
# 히스토그램 -> 이 경우 기온이 x좌표에 출력됨
for row in data:
    if row[5] != '':
        if row[-1].split('-')[1] == '07' or row[-1].split('-')[1] == '08':
            summer.append(float(row[5]))
    if row[-2] != '':
        if row[-1].split('-')[1] == '01' or row[-1].split('-')[1] == '02':
            winter.append(float(row[-2]))
print(summer)
print(winter)
plt.hist(summer, color = 'r', label = 'summer')
plt.hist(winter, color = 'b', label = 'winter')
plt.legend()
plt.show()

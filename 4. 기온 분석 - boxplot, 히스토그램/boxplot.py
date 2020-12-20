import matplotlib.pyplot as plt
import csv
import numpy as np # 주석이 붙은 부분은 1/4, 2/4, 3/4 부분에 위치한 정확한 값을 알기 위할때 필요한 코드
f = open('seoul.csv')
data = csv.reader(f)
next(data)
summer = []
winter = []
np_summer = np.array(summer)#
np_winter = np.array(winter)#
# boxplot = 상자 그림
# 이 그래프의 장점은  1/4, 2/4, 3/4 에 위치한 값을 보여준다.
'''
for row in data:
    if row[5] != '':
        if row[-1].split('-')[1] == '07' or row[-1].split('-')[1] == '08':
            summer.append(float(row[5]))
    if row[-2] != '':
        if row[-1].split('-')[1] == '01' or row[-1].split('-')[1] == '02':
            winter.append(float(row[-2]))

print('summer temperature 1/4 =', str(np.percentile(summer, 25)))#
print('summer temperature 2/4 =', str(np.percentile(summer, 50)))#
print('summer temperature 3/4 =', str(np.percentile(summer, 75)))#
print('winter temperature 1/4 =', str(np.percentile(winter, 25)))#
print('winter temperature 2/4 =', str(np.percentile(winter, 50)))#
print('winter temperature 3/4 =', str(np.percentile(winter, 75)))#
plt.boxplot(summer)
plt.boxplot(winter)
#plt.boxplot([summer, winter])# 둘이 합쳐져서 다른 열에 출력되는 코드
plt.show()
'''
# 월별 최고기온을 가시성 좋게 표현 ( boxplot의 장점이 두드러짐)
'''
month = [ [], [], [], [], [], [], [], [], [], [], [], [] ]
for row in data:
    if row[5] != '':
        month[ int(row[-1].split('-')[1]) - 1 ].append(float(row[5]))
plt.boxplot(month)
plt.show()
'''
# 월별 최저,최고 기온을 가시성 좋게 표현 ( boxplot의 장점이 두드러짐)

high_month = [ [], [], [], [], [], [], [], [], [], [], [], [] ]
low_month = [ [], [], [], [], [], [], [], [], [], [], [], [] ]
for row in data:
    if row[5] != '':
        high_month[ int(row[-1].split('-')[1]) - 1 ].append(float(row[5]))
    if row[-2] != '':
        low_month[ int(row[-1].split('-')[1]) - 1 ].append(float(row[-2]))
plt.boxplot(high_month)
plt.boxplot(low_month)
plt.show()

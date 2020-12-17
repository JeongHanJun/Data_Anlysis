import csv
import matplotlib as mpl
import matplotlib.pyplot as plt
""" f = open('seoul.csv')
data = csv.reader(f)
next(data)
max_temp_result = []
min_temp_result = [] """# 위 부분은 공통으로 해당 하는 부분
"""
# 1. 25년간 최고 및 최저 기온 그래프
f = open('seoul.csv')
data = csv.reader(f)
next(data)
max_temp_result = []
min_temp_result = []

for row in data:
    if row[5] != '':
        max_temp_result.append(float(row[5]))
    if row[-2] != '':
        min_temp_result.append(float(row[-2]))
plt.xlabel('Months')
plt.ylabel('Temperature')

plt.plot(max_temp_result, 'r', label = "Max_Temperature")
plt.plot(min_temp_result, 'b', label = "Min_Temperature")
plt.legend()
plt.show()
print(len(min_temp_result))
print(len(max_temp_result)) """
# 2. 25년간 생일인 날들 의 최고 및 최저 기온 그래프
"""
f = open('seoul.csv')
data = csv.reader(f)
next(data)
max_temp_result = []
min_temp_result = []

for row in data:
    if row[5] != '':
        if row[-1].split('-')[1] == '02': # 주어진 자료가 매일 기온 체크가 아닌 매월이므로,  만약 매일에 대한 기온 분석이라면 생일인 날만을 찾기 위해and row[-1].split('-')[2] == '02'
            max_temp_result.append(float(row[5]))
    if row[-2] != '':
        if row[-1].split('-')[1] == '02':
            min_temp_result.append(float(row[-2]))
plt.plot(max_temp_result, 'r', label = "Max_Temperature")
plt.plot(min_temp_result, 'b', label = "Min_Temperature")
plt.legend()
plt.show()"""
#3. 최근 10년간 생일인 날들의 최고 및 최저 기온 그래프
"""
f = open('seoul.csv')
data = csv.reader(f)
next(data)
max_temp_result = []
min_temp_result = []

for row in data:
    if row[5] != '':
        if int(row[-1].split('-')[0]) >= 2000 and row[-1].split('-')[1] == '02':
             max_temp_result.append(float(row[5]))
    if row[-2] != '':
        if int(row[-1].split('-')[0]) >= 2000 and row[-1].split('-')[1] == '02':
            min_temp_result.append(float(row[-2]))
plt.plot(max_temp_result, 'r', label = "Max_Temperature")
plt.plot(min_temp_result, 'b', label = "Min_Temperature")
plt.legend()
plt.show()
"""
# 4. Final 최근 20년간 내 생일의 기온변화를 그래프로 그리기 전체 코드
f = open('seoul.csv')
data = csv.reader(f)
next(data)  # 첫줄 제외 (맨윗행은 데이터의 종류에 대한 소개이므로)
high_temp = []
low_temp = []
for row in data:
    if row[5] != '' and row[-2] != '':
        date = row[-1].split('-')
        if 2000 <= int(date[0]):
            high_temp.append(float(row[5]))
            low_temp.append(float(row[-2]))
plt.rc('font', family = 'MalGun Gothic')            # 맑은 고딕을 기본 글꼴로 설정
plt.rcParams['axes.unicode_minus'] = False          # '-' 꺠짐 방지
plt.title('최근 20년간 내 생일의 기온 변화 그래프')
plt.xlabel('월(Month)')
plt.ylabel('온도(Temperature)')
plt.plot(high_temp, 'hotpink', label = 'high')
plt.plot(low_temp, 'skyblue', label = 'low')
plt.legend()
plt.show()
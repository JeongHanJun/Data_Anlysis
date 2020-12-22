import csv
import matplotlib.pyplot as plt

f = open('2020년 11월 성남시 인구1살간격통계, 행정안전부, ANSI.csv', 'rt', encoding='euc-kr')
data = csv.reader(f)
result = []

for row in data:
    if '서현1동' in row[0]:
        for i in row[3:]:
            result.append(int(i))
plt.bar(range(101), result)# plt.bar(막대를 표시할 위치(x), 막대의 높이(y)) 
#plt.barh(range(101), result)# 이러면 위의 bar 그래프를 왼쪽으로 90도 회전시킨 수평막대그래프가 출력됨
plt.show()
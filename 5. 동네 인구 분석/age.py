# -*- coding: euc-kr -*-
import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

f = open('2020년 11월 성남시 인구1살간격통계, 행정안전부, ANSI.csv', 'rt', encoding='euc-kr')
data = csv.reader(f)

'''
for row in data:
    if '서현1동' in row[0]:
        print(len(row[3:]))# 101 이 출력된다.
        for i in row[3:]:# 0살 ~ 100살 이상까지 인구수 출력 즉 101개의 행 출력
            print(i)
'''
# 리스트에 서현1동의 사람들을 0세 ~ 100세 순으로 순차적으로 담기
result = []
for row in data:
    if '서현1동' in row[0]:
        for i in row[3:]:
            #result.append(i)# 이렇게 하면 문자열형태로 저장됨
            result.append(int(i))
print(result)

# 이제 데이터 시각화를 해보면
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.rc('font', family = 'MalGun Gothic')    # 한글출력 위한 코드 
plt.rcParams['axes.unicode_minus'] = False  # # 한글출력 위한 코드
plt.title('성남시 서현1동 나이별 인구수')
plt.xlabel('나이')
plt.ylabel('인구수')
plt.plot(result)
plt.show()


import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 본 코드는 2020년 11월 기준 성남시 예하의 특정 지역을 입력받고, 해당 지역의 나이별 인구수 분포를 꺾은선 그래프로 나타내는 코드입니다.

f = open('2020년 11월 성남시 인구1살간격통계, 행정안전부, ANSI.csv', 'rt', encoding='euc-kr')
data = csv.reader(f)
# 사용자가 원하는 지역의 이름을 입력받기
area_name = input('나이별 인구수를 알고 싶은 지역 (동 단위) 의 이름을 입력하세요 : ')
result = []

for row in data:
    if area_name in row[0]:
        for i in row[3:]:
            result.append(int(i.replace(',' , '' )))#엑셀에서 100단위로 ',' 가 있는데 가시성을 위해 제거하는 부분

plt.style.use('ggplot')
plt.rc('font', family = 'Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False
plt.title(area_name + '의 나이별 인구 분포')
plt.xlabel('나이')
plt.ylabel('인구수')
plt.plot(result)
plt.show()

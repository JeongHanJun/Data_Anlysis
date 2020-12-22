import csv
import matplotlib.pyplot as plt
import os
import sys
def resource_path(relative):
    #print(os.environ)
    application_path = os.path.abspath(".")
    if getattr(sys, 'frozen', False):
        # If the application is run as a bundle, the pyInstaller bootloader
        # extends the sys module by a flag frozen=True and sets the app 
        # path into variable _MEIPASS'.
        application_path = sys._MEIPASS
    #print(application_path)
    return os.path.join(application_path, relative)

f = open(resource_path('age3.csv'), 'rt', encoding='euc-kr')
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

# 전체 데이터를 출력하는 코드
""" import csv
f = open('seoul.csv')
data = csv.reader(f)
header = next(data)
for row in data:
    print(row)
f.close() """
#
#2020년 12월의 평균기온, 평균최저기온, 평균최고기온은 아직 기록되지 않았으므로  ( 12월의 마지막날까지 기다려야 하므로 ) 현시점인 12월 7일에서는 아직 기록되지 않은 것이 정상, 이 부분의 빈칸을 Not yet recorded로 아직 기록되지 않았음을 알려주기 위해 정정하는 코드
""" import csv
f = open('seoul.csv')
data = csv.reader(f)
header = next(data)
for row in data:
    if row[3] == '':
        row[3] = 'Not yet recorded'
    if row[4] == '':
        row[4] = 'Not yet recorded'
    if row[7] == '':
        row[7] = 'Not yet recorded'
    print(row)
f.close() """
import csv
f = open('seoul.csv')
data = csv.reader(f)
header = next(data)
max_temp = -100.0
min_temp = 100.0
max_date = ''
min_date = ''
for row in data:
    if row[3] == '':
        row[3] = 'Not yet recorded'
    if row[4] == '':
        row[4] = 'Not yet recorded'
    if row[7] == '':
        row[7] = 'Not yet recorded'
    if float(max_temp) < float(row[5]):
        max_temp = row[5]
        max_date = row[-1]
    if float(min_temp) > float(row[-2]):
        min_temp = row[-2]
        min_date = row[-1]
f.close()
print("1996년부터 2020년 까지 서울에서 기온이 가장 높았던, 가장 더웠던 날은 {}이고, 그 날의 최고기온은 {}도였습니다.".format(max_date, max_temp))
print("또한, 1996년부터 2020년 까지 서울에서 기온이 가장 낮았던, 가장 추웠던 날은 {}이고, 그 날의 최저기온은 {}도였습니다.".format(min_date, min_temp))
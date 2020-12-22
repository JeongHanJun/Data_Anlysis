import csv
import matplotlib.pyplot as plt
f = open('age_gender.csv')
data =csv.reader(f)
men = []
women = []

# 인덱싱을 이용하는 방법1
for row in data:
    if '서현1동' in row[0]:
        for i in range(0, 101):# 0 ~ 100
            men.append(int(row[i+3]))# 3~ 103 지역명,총인구 를 제외하고 0세 ~ 100세
            women.append(int(row[-(i+1)]))# 맨뒤 ~ 맨뒤-100까지 즉 100세, 99세, 98세, .....1세, 0세 순으로 저장됨
women.reverse()
'''
# 인덱싱을 이용하는 방법2
for row in data:
    if '서현1동' in row[0]:
        for i in row[3, 104]:# 3~ 103  -> 0세 ~ 100세
            men.append(int(i))
        for i in row[106:]:
            women.append(int(i))
'''
# 위의 2가지 방법중 어떤것을 사용해도 상관없음
plt.style.use('ggplot')
plt.rc('font', family = 'Malgun Gothic')
plt.title('2020년 11월 서현1동 남녀 나이에 따른 인구 분포')
plt.bar(range(101), men, color = 'skyblue', label = '남자')
plt.bar(range(101), women, color = 'pink', label = '여자')
plt.xlabel('나이')
plt.ylabel('인구수')
plt.legend()
plt.show()



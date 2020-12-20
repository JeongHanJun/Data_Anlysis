import random
import matplotlib.pyplot as plt
dice = []
cnt = int(input('주사위를 몇번 굴릴까요??'))

for i in range(cnt):
    dice.append(random.randint(1, 6))
#print(dice)
plt.hist(dice, bins = 6)#bins 는 가로축의 구간 개수를 설정, 이것을 안하면 5-6 구간 그래프의 오른쪽 끝 부분이 보기 안좋음
plt.show()

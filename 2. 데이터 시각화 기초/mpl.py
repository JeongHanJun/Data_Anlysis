import matplotlib.pyplot as plt
# 위처럼 plt를 불러오고, plt 함수에 대해 데이터 입력하고 plt.show로 그래프 출력 하는 3단계
""" # 1. 1차원 기초 데이터 형태는 y값이 디폴트값으로 x값과 같은값으로 
plt.plot( [10, 20, 30, 20, 10])
plt.show() """
""" # 2 2차원 기초 데이터 형태는 plt.plot( [x datas], [y datas] )
plt.plot( [1, 2, 3, 4], [10, 39, 52, 23])
plt.show() """
# Value Error 조심
# x데이터와 y데이터의 개수가 맞지 않으면 ValueError 발생

""" # 3. 그래프의 제목 넣는 title 함수
plt.title('The Line')
plt.plot([10, 20, 30, 40])
plt.show()
 """

""" # 4. 그래프에 범례 추가 쉽게 말하면 다른 색깔의 데이터를 추가하는것
plt.title('a Legend')
plt.plot( [10, 20, 30, 40], [30, 10, 40, 20], label = "Data #1")
plt.plot( [10, 20, 30, 40], [20, 40, 10, 30], label = "Data #2")
plt.legend(loc = 'lower left')
plt.show()
# legend의 위치 저장 관련해서는 메모장에 자세히 설명
"""
""" # 5. 그래프의 색상 바꾸기
plt.title('color')
plt.plot([10, 20, 30, 40], color = 'skyblue', label = 'sky-blue')
plt.plot([40, 20, 10, 20], 'pink', label = 'pink')# color 속성을 생략해도 자동으로 색상이 결정된다.
plt.legend(loc = 0)
plt.show() """

""" # 6. 그래프의 선 모양 바꾸기
plt.title('linestyle')
plt.plot([10, 20, 30, 40], 'r', linestyle = '--', label = 'dashed')
plt.plot([40, 30, 20, 10], 'b', ls = ':', label = 'dotted')
plt.plot([20, 15, 20, 15], 'r--', label = 'code in short')
plt.legend()
plt.show()
"""
""" # 7. 마커(점) 모양 바꾸기
plt.title('marker')
plt.plot([10, 20, 30, 40], 'r.', label = 'circle')
plt.plot([40, 30, 20, 10], 'b^', label = 'triangle-up')
plt.plot([20, 25, 20, 15], 'g.--', label = 'Code in short')# 여기서 label = 'circle'은 붙이나 마나다. 왜냐하면 g.-- 에서 이미 green color, . marker , -- linestyle 을 한번에 선언했기 때문 
plt.legend()
plt.show() """
# 이상 그래프 서식 관련 끝

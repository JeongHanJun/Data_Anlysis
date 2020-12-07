import csv
f = open('seoul.csv', 'r', encoding = 'cp949')
#data = csv.reader(f, delimiter = '.')
data = csv.reader(f)# csv 파일의 데이터를 읽어오는 csv 모듈의 함수

#for row in data:    # 이 경우 row는 list type 으로 출력됨
#    print(row)
#print(data)        # data라는 객체가 존재하는지 여부에 대해 출력 만약 존재하면 <_csv.reader object at 0x000001495279E760> 와 같이 출력됨
header = next(data) # 추가적으로 이 부분에서, 기상자료개방포털에서 받은 기온 csv 파일은 첫 열이 \t\t이 된상태로 자료가 입력되어있어서, 메모장으로 연결한 후 모두 찾아 바꾸기를 해주어서 첫 열의 데이터에 탭이 두번 존재하는것을 없애고 맨 첫줄인 빈행도 제거
# next 라는 함수는 첫번째 데이터 행을 읽어오면서 데이터의 탐색 위치를 다음줄로 이동시키는 명령을 수행한다.

#print(header)
for row in header:
    print(row)
f.close()
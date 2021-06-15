# Kakao OpenAPI 를 이용한 다음검색에서의 이미지 검색 후 원하는 키워드에 대한 이미지들을 자동 다운로드

import requests
# 2021.06.15 수정내용
# 개인정보보호를 위해 RREST API키를  "REST_API_KEY"로 표시
'''
    GET /v2/search/image HTTP/1.1
    Host: dapi.kakao.com
    Authorization: KakaoAK {REST_API_KEY}
'''

url = "https://dapi.kakao.com/v2/search/image"
headers = {
    "Authorization" : "KakaoAK" + "REST_API_KEY"# REST_API_KEY는 개인정보이므로 Kakao Developers - 내 애플리케이션 - 앱 설정 - 요약정보 에 들어가면 앱 에 REST API키를 알 수 있다.
}
data = {
    "query" : "라이언"
}
# 기본적으로 다음 검색에서 시작
#
# query = 검색어 이름 ( 검색을 원하는 질의어)  type = str  
# 추가적으로 필요하다면 sort 정렬방식 - accuracy or recency 가능 type = str  
# page = 결과 페이지 번호  1 ~ 50 ,  기본값은 1  , type = int
# size = 한 페이지에 보여질 문제 수 1 ~ 80 , 기본값은 80  , type = int 
#
# Autorization = Kakao
response = requests.post(url, headers = headers, data = data)
#response.status_code# 가 200이어야 정상임
# response 의 meta에 포함된 내용들
# 1. total_count (int) = 검색된 문서 수
# 2. pageable_count (int) = total_count 중 노출 가능 문서 수
# is_end (Boolean) =  현재 페이지가 마지막 페이지인지 , 만약 False 이면 page를 증가시켜 다음 페이지 요청 가능
#
# documents 에는 collection, image_url, width, height, display_sitename(출처) , datetime 등이 포함되있음
image_url = response.json()['documents'][0]['image_url']
img_response = requests.get(image_url)
# responde.json()# 안의 documents 안에 list가 있는데 이 안에 image_url이 있고 이것을 사용하여 이미지 다운로드
'''

    'documents': [{'collection': 'blog',
   'datetime': '2020-03-09T19:26:00.000+09:00',
   'display_sitename': '네이버블로그',
   'doc_url': 'http://blog.naver.com/2012kiss/221845372207',
   'height': 773,
   'image_url': 'http://postfiles1.naver.net/MjAyMDAzMDlfMTM4/MDAxNTgzNzQ5NTk0Njkw.gvrYNHHvHfwrRUVu2xSCqE2kp_OLzg1Y2EFoafU3lEMg.spMelefH5nVyAsuH1SLbLarM4L1KHzR8oHHtdS0v1wUg.PNG.2012kiss/%ED%8E%AD%EC%88%98.png?type=w773',
   'thumbnail_url': 'https://search3.kakaocdn.net/argon/130x130_85_c/1uTVnFKcose',
   'width': 773},
  {'collection': 'etc',

  documents 라는 key 안에 value로 list가 들어가있다. list의 정보들은 특정 웹사이트에 대한 정보들

'''
# 실제로 type(response.json()['documents']) 를 하면 list가 출력됨
# 예시로 response.json()['documents'][0] 를 해보면 이에 대한 collection, datetime, display_sitename, doc_url, image_url, thumbnail_url, width 가 나옴, 이중에서 img_url을 사용
#
# response.json()['documents'][0]['image_url'] 을 하면 url주소가 나옴, 하지만 이를 통해 다운 받기 위해서는 byte로 단위로 구성된 contetn가 필요함
# img_response.content 를 하면 n'\어쩌구 저쩌구 나오는데 이걸 다운해야 이미지를 다운받게 되는 것
def save_image(image_url, file_name):
    img_response = requests.get(image_url)

    if img_response.status_code == 200:
        with open(file_name, "wb") as fp:
            fp.write(img_response.content)

cnt = 0
for image_info in response.json()['documents']:
    print(image_info['image_url'])
    cnt = cnt + 1
    file_name = "Ryan_%d.jpg" %(cnt)
    save_image(image_info['image_url'], file_name)

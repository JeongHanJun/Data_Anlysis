'''
 2020년 4월부터 kakao developers 사이트 개편을 통해

 기존에는 access token을 제공하였는데

 현재는 인증을 거쳐 code / access_token / refresh token 을 발급받도록 변경됨

 [ 인증토큰 받기 순서 ]

 1. Redirect URL 설정
 2. 인증 코드 받기
 3. 사용자 토큰 받기 ( access token / refresh token )
 4. 토큰 지정
 

 # REST API 앱 키 = 개인정보보호 때문에 "REST_API_KEY"로 표기
 # REST API 앱 키를 통해 코드 발급받는 방법 , 크롬의 새 시크릿창을 열고 아래의 과정을 따라한다.
    1. https://kauth.kakao.com/oauth/authorize?client_id={REST_API 앱키를 입력하세요}&response_type=code&redirect_uri=https://localhost.com 에 접속한다.( 주소 복사후 REST API 앱키를 넣고 url 이동)
    2. 카카오 이메일과 비밀번호를 입력해서 로그인을 시도한다.
    3. 시간이 좀 걸리고, 오류창이 뜬다. 이때 url 주소에 보면 code = "어쩌구저쩌구" 라고 뜬다.
    4. 이 "어쩌구저쩌구"가 34번째 줄에 해당하는 code이다.
 '''

import requests
import json
# 1번째 실행
""" 
url = "https://kauth.kakao.com/oauth/token"

data = {
    "grant_type" : "authorization_code",
    "client_id" : ""REST_API_KEY"",# REST_API 앱 키
    "redirect_url" : "https://localhost.com",
    "code" : "17~21 번째 줄 참고"# REST API 앱 키를 통해 발급받은 code
}

response = requests.post(url, data = data)

tokens = response.json()

print(tokens)
# 'access_token': '각자 고유의 access_token'
#토큰 저장하기
with open( "kakao_token.json", "w" ) as fp:# 파일 이름은 자유
    json.dump(tokens, fp)
"""

# 2번째 실행,   1번째 실행이 잘되었는지 확인하는 부분 ,  저장된 토큰을 불러와서 access_token이 잘 저장되었는지 확인, error가 뜨면 다시 code발급부터 시작해야함
""" 
# 토큰 저장
with open("kakao_token.json", 'r') as fp:
    ts = json.load(fp)
print(ts['access_token'])
"""

# -----------------------------------------------여기까지 1. get_token ( 2번의 실행으로 나눠져있음 , 각각 따로 실행할 것)---------------------------------------------------------------------------------
#
#------------------------------------------------아래부터 2. send Message---------------------------------------------------------------------------------

# 공통 부분이므로 실행할때 주석처리하지 말것.
# 나에게 메시지 보내기
with open("kakao_token.json", 'r') as fp:
    tokens = json.load(fp)

url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

headers = {
    "Authorization": "Bearer " + "각자의 access_token"
}
# 1번째 실행은 공통부분 + 1번째 부분 으로 실행 즉 2번째 부분(리스트 메시지 전송)은 주석처리하고 실행
# 간단한 텍스트 메시지 전송
'''
data = {
    "template_object" : json.dumps({ "object_type" : "text",
                                     "text" : "Hello HanJun",
                                     "link" : {
                                                 "web_url" : "www.naver.com"
                                              }
    })
}

response = requests.post(url, headers = headers, data = data) 

print(response.status_code)
# response.status_code 로 200이 출력되면 정상적으로 완료
'''
# 여기까지 1번째 실행
#
#
# 2번째 실행 리스트 형태의 메시지 전송  ,  실행하기 전에 1번째 실행부분은 주석처리하고 실행
'''
template = {
    "object_type" : "list",
    "header_title" : "초밥 사진",
    "header_link" : {
        "web_url" : "www.naver.com",
        "mobile_web_url" : "www.naver.com"
    },
    "contents" : [
        {
            "title" : "1. 광어초밥",
            "description" : "광어는 맛있다",
            "image_url" : "https://search1.kakaocdn.net/argon/0x200_85_hr/8x5qcdbcQwi",
            "image_width" : 50, "image_height" : 50,
            "link" : {
                "web_url" : "www.naver.com",
                "mobile_web_url" : "www.naver.com"
            }
        },
        {
            "title" : "2. 참치초밥",
            "description" : "참치는 맛있다",
            "image_url" : "https://search2.kakaocdn.net/argon/0x200_85_hr/IjIToH1S7J1",
            "image_width" : 50, "image_height" : 50,
            "link" : {
                "web_url" : "www.naver.com",
                "mobile_web_url" : "www.naver.com"
            }
        }
        
    ],
    "buttons" : [
        {
            "title" : "웹으로 이동",
            "link" : {
                "web_url" : "www.naver.com",
                "mobile_web_url" : "www.naver.com"
            }
        }
    ]
    
}

data = {
    "template_object" : json.dumps(template)
}

response = requests.post(url, data=data, headers=headers)
print(response.status_code)
if response.json().get('result_code') == 0:
    print('메시지를 성공적으로 보냈습니다.')
else:
    print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))
# response.status_code 로 200이 출력되면 정상적으로 완료
# 여기까지 2번째 실행 부분
'''
#------------------------------------------------여기까지 2. send Message---------------------------------------------------------------------------------
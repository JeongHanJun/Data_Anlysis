import json
import requests

with open("kakao_token.json", "r") as fp:
    tokens = json.load(fp)

print(tokens)
#  잘 나오는지 확인
#
# 토큰 재발급 받는 방법
app_key = "각자 고유의 REST API KEY 값"
url = "https://kauth.kakao.com/oauth/token"
data = {
    "grant_type" : "refresh_token",
    "client_id" : app_key,
    "refresh_token" : tokens['refresh_token']
}

response = requests.post(url, data = data)
print(response.status_code)# 200 출력시 정상적 완료
print(response.json())

tokens['access_token'] = response.json()['access_token']
tokens['app_key'] = app_key# 앞으로 많이 쓸거같으니 그냥 json 파일 안에 같이 저장

# 재발급받은 access_token 값을 json 파일에 저장
with open("kakao_token.json", "w") as fp:
    json.dump(tokens, fp)

print(tokens)
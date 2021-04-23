# Welcome to the 'datagokr'

### This is python toy project
* coded in 2020.10
* OS: Window
* Tools: PyCharm
* API Link: [공공데이터포털](https://data.go.kr)

### 1. 재난문자방송 발령상황 데이터(Disaster message sent history)
- Myinfo.py - API Key Information
  - API Key 정보 저장  
- disasterMsg.py - url 요청 및 응답 처리
  - 요청메시지 명세  
    * ServiceKey : 인증키
    * type : 호출 문서(xml, json)
    * page : 페이지 위치
    * numOfRows : 페이지당 요청숫자
    * flag : 신규 API

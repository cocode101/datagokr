import urllib.request as ul
from urllib.parse import urlencode, quote_plus, unquote
from Myinfo import Myinfo

# urllib : Python에서 Web과 관련된 데이터를 손쉽게 이용하도록 도와주는 라이브러리
# urllib.request : Web을 열어서 읽어오는 역할을 하는 모듈

myinfo = Myinfo()
endpoint = "http://apis.data.go.kr/1741000/DisasterMsg2/getDisasterMsgList"
queryParams = '?' + urlencode({ quote_plus('ServiceKey') : unquote(myinfo.myapikey), 
                                quote_plus('pageNo') : '1', 
                                quote_plus('numOfRows') : '10', 
                                quote_plus('type') : 'xml', 
                                quote_plus('flag') : 'Y' })

request = ul.Request(endpoint + queryParams)
request.get_method = lambda: 'GET'

# urlopen 함수는 웹에서 얻은 데이터의 객체를 반환
response = ul.urlopen(request)

if response.getcode() == 200:
    response_body = response.read()
    
    # print(response_body)
    result = response_body.decode("utf-8")
    print(result)







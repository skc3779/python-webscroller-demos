import requests

# requests 라이브러리를 이용한 파일 업로드 테스트
# 업로드된 파일 : http://pythonscraping.com/pages/uploads/200937431.jpg

files = {'uploadFile': open('./files/200937431.jpg', 'rb')}
r = requests.post("http://pythonscraping.com/pages/processing2.php",
                  files=files)
print(r.text)

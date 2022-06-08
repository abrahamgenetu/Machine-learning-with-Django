import requests
predict = [print(x) for x in requests.post("http://127.0.0.1:7777/?age=68&gender=0&bp=2&cholesterol=2&salt=27")]
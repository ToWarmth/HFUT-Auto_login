import requests

url_list = ['http://172.16.200.13/','http://172.16.200.11','http://172.16.200.12']
DDDDD = 'xxxxxxxxxx'    # username
upass = 'xxxxxx'        # password
OMKKey = '123'
# data = "DDDD={}&upass={}&0MKKey={}".format(DDDDD, upass, OMKKey)
data = {
    'DDDDD' : DDDDD,
    'upass' : upass,
    '0MKKey' : OMKKey
}

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "max-age=0",
    "Connectin": "keep-alive",
    "Cookies": "myusername={}".format(DDDDD),
    # "Content-Length": '50',
    "Content-Type": "application/x-www-form-urlencoded",
    # "Host": "172.16.200.13",
    # "Origin": "https://172.16.200.13",
    # "Referer": "https://172.16.200.13",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.33"
}

for url in url_list:
    response = requests.post(url, data, headers=header, timeout=30)  # POST 方式向 URL 发送表单，同时获取状态码
    # print("状态码{}".format(response.status_code))  # 打印状态码
    # try except可避免timeout导致的no response Error
    if "您已经成功登录" in response.text:
        print("成功登录！")
        break
    else:
        print("登录失败")
        continue


import requests
def post_json():
    url = "http://132.232.44.158:5000/userLogin/"

    date = "{\"username\":\"test\", \"password\":\"123456\", \"captcha\":\"123456\"}"

    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "2b74fec8-481d-458a-88cd-8c33ad194886"
        }
    r=requests.post(url=url,data=date,headers=headers)
    print("返回代码：",r.status_code)
    print(r.headers)

def json1():
    u="http://132.232.44.158:5000/userLogin/"
    d={"username":"test", "password":"test", "captcha":"123456"}
    r=requests.post(url=u,json=d)
    print("状态码：",r.status_code)

if __name__=="__main__":
    post_json()

    json1()

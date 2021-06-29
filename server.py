import requests
import re

client = requests.Session()

def login():
    url = "http://52.81.69.12:9000/admin/login/?next=/admin/"

    client.get(url)
    if "csrftoken" in client.cookies:
        csrftoken = client.cookies["csrftoken"]
    else:
        csrftoken = client.cookies["csrf"]

    # csrftoken = re.findall("name='csrfmiddlewaretoken' value='(.+?)'", response.text)
    # print("csrf_token",csrftoken)

    data = {
        "csrfmiddlewaretoken" : csrftoken,
        "username" : "jinjian",
        "password" : "kbjQTweV",
        "next" : "/admin/"
    }
    client.post(url,data=data)

def packagename():
    dict = {
        # 金刚
        "kingkong": "com.kingandroid.server.ctskong.defender",
        # ctstar
        "ctstar": "com.cleanandroid.server.ctstar",
        # 微清理
        "weiqingqi": "com.cleanapps.master",
        # 黑猫
        "blackcat": "com.cleanapps.super",
        # 蜂鸟
        "fengniao": "com.meet.cleanapps",
        # 流星
        "liuxing": "com.meteorandroid.server.ctsclean",
        # 天眼
        "tianyan": "com.cleandroid.server.ctskyeye",
        # 秀我
        "xiuwo": "com.imageandroid.server.ctsmatting",
        # 简变
        "jianbian": "com.mattingandroid.server.ctsimple",
        # 5G精灵
        "5Gjingling": "com.netandroid.server.ctselves",
        # 5G快连
        "5Gkuailian": "com.linkandroid.server.ctsmate",
        # SD清理专家
        "sdclean": "com.sdandroid.server.ctscard",
        # 雷神
        "leishen": "com.cleandroid.server.ctsthor",
        # wifi随意连
        "suiyilian": "com.connectandroid.server.ctseasy",
        # wifi随心连
        "suixinlian": "com.heartandroid.server.ctslink"
    }

    return dict

def url():
    url_dict = {
        # 流星url
        "liuxing_news_and_weather" : "http://52.81.69.12:9000/admin/advertisement/adspolicy/1348/change/?_changelist_filters=pkg_name%3Dcom.meteorandroid.server.ctsclean",
        "liuxing_lockscreen": "http://52.81.69.12:9000/admin/advertisement/adspolicy/1238/change/?_changelist_filters=pkg_name%3Dcom.meteorandroid.server.ctsclean",
        "liuxing_no_lockscreen" : "http://52.81.69.12:9000/admin/advertisement/adspolicy/1221/change/?_changelist_filters=pkg_name%3Dcom.meteorandroid.server.ctsclean",
        # wifi随心连url
        "suixinlian_news_and_weather" : "http://52.81.69.12:9000/admin/advertisement/adspolicy/1397/change/?_changelist_filters=pkg_name%3Dcom.heartandroid.server.ctslink",
        "suixinlian_lockscreen" : "http://52.81.69.12:9000/admin/advertisement/adspolicy/1393/change/?_changelist_filters=pkg_name%3Dcom.heartandroid.server.ctslink",
        "suixinlian_no_lockscreen" : "http://52.81.69.12:9000/admin/advertisement/adspolicy/1392/change/?_changelist_filters=pkg_name%3Dcom.heartandroid.server.ctslink",
        # 5Gjinglingurl
        "5Gjingling_news_and_weather" : "http://52.81.69.12:9000/admin/advertisement/adspolicy/1332/change/?_changelist_filters=pkg_name%3Dcom.netandroid.server.ctselves",
        "5Gjingling_lockscreen" : "http://52.81.69.12:9000/admin/advertisement/adspolicy/1254/change/?_changelist_filters=pkg_name%3Dcom.netandroid.server.ctselves",
        "5Gjingling_no_lockscreen" : "http://52.81.69.12:9000/admin/advertisement/adspolicy/1237/change/?_changelist_filters=pkg_name%3Dcom.netandroid.server.ctselves"
    }
    return url_dict

def news_and_weather(urls=url()["liuxing_news_and_weather"],
                     pkg_name="com.meteorandroid.server.ctsclean",
                     value_field="1",
                     ):
    login()
    urls = urls
    print(urls)
    client.get(urls)
    if "csrftoken" in client.cookies:
        csrf_token = client.cookies["csrftoken"]
    else:
        csrf_token = client.cookies["csrf"]

    body = {
        "csrfmiddlewaretoken" : csrf_token,
        "pkg_name" : pkg_name,
        "version_code" : "100",
        "page" : "page_default",
        "key" : "key_hybrid_popup_mask",
        "value_type" : "INT32",
        "value_field" : value_field,
        "value_verifier" : "0",
        "value_xunjian" : "0",
        "enable" : "on",
        "status" : "PUB",
        "description" : "",
        "_save" : "保存"
    }
    client.post(urls,data=body)

def lockscreen(urls=url()["liuxing_lockscreen"],
               pkg_name="com.meteorandroid.server.ctsclean",
               value_field="true"
               ):
    login()
    urls = urls
    client.get(urls)
    if "csrftoken" in client.cookies:
        csrf_token = client.cookies["csrftoken"]
    else:
        csrf_token = client.cookies["csrf"]

    body = {
        "csrfmiddlewaretoken" : csrf_token,
        "pkg_name" : pkg_name,
        "version_code" : "100",
        "page" : "page_default",
        "key" : "lockscreen_logo_show",
        "value_type" : "BOOL",
        "value_field" : value_field,
        "value_verifier" : "true",
        "value_xunjian" : "true",
        "enable" : "on",
        "status" : "PUB",
        "description" : "",
        "_save" : "保存"
    }
    client.post(urls,data=body)

def no_lockscreen(urls=url()["liuxing_no_lockscreen"],
                  pkg_name="com.meteorandroid.server.ctsclean",
                  value_field="false"
                  ):
    login()
    urls = urls
    client.get(urls)
    if "csrftoken" in client.cookies:
        csrf_token = client.cookies["csrftoken"]
    else:
        csrf_token = client.cookies["csrf"]

    body = {
        "csrfmiddlewaretoken" : csrf_token,
        "pkg_name" : pkg_name,
        "version_code" : "100",
        "page" : "page_default",
        "key" : "non_lockscreen_logo_show",
        "value_type" : "BOOL",
        "value_field" : value_field,
        "value_verifier" : "true",
        "value_xunjian" : "true",
        "enable" : "on",
        "status" : "PUB",
        "description" : "",
        "_save" : "保存"
    }
    client.post(urls,data=body)

if __name__ == '__main__':
    pkg_name = packagename()["5Gjingling"]
    print(pkg_name)

    news_and_weather(urls=url()["5Gjingling_news_and_weather"],pkg_name=pkg_name,value_field="3")
    lockscreen(urls=url()["5Gjingling_lockscreen"],pkg_name=pkg_name,value_field="true")
    no_lockscreen(urls=url()["5Gjingling_no_lockscreen"],pkg_name=pkg_name,value_field="false")

























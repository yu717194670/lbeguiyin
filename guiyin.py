import requests

def packagename():
        dict = {
            # 金刚
            "kingkong" : "com.kingandroid.server.ctskong.defender",
            # ctstar
            "ctstar" : "com.cleanandroid.server.ctstar",
            # 微清理
            "weiqingqi" : "com.cleanapps.master",
            # 黑猫
            "blackcat" : "com.cleanapps.super",
            # 蜂鸟
            "fengniao" : "com.meet.cleanapps",
            # 流星
            "liuxing" : "com.meteorandroid.server.ctsclean",
            # 天眼
            "tianyan" : "com.cleandroid.server.ctskyeye",
            # 秀我
            "xiuwo" : "com.imageandroid.server.ctsmatting",
            # 简变
            "jianbian" : "com.mattingandroid.server.ctsimple",
            # 5G精灵
            "5Gjingling" : "com.netandroid.server.ctselves",
            # 5G快连
            "5Gkuailian" : "com.linkandroid.server.ctsmate",
            # SD清理专家
            "sdclean" : "com.sdandroid.server.ctscard",
            # 雷神
            "leishen" : "com.cleandroid.server.ctsthor",
            # wifi随意连
            "suiyilian" : "com.connectandroid.server.ctseasy"
        }

        return dict

def guiyin(base_url="https://tycs.suapp.mobi",
        method="modify",
        pkg_name="com.meteorandroid.server.ctsclean",
        check_code="",
        channel="",
        device_id="6f79ef42dc439f5c",
        media_source="bytedance_int",
        ad_site_ad="10001",
        campaign_id="00"):

    url = base_url+"/cm/qa-tool/set-attribution"

    data = {
        "method": method,
        "pkg_name": pkg_name,
        "check_code": check_code,
        "channel": channel,
        "device_id": device_id,
        "media_source": media_source,
        "ad_site_ad": ad_site_ad,
        "campaign_id" : campaign_id
    }

    reponse = requests.post(url,data=data)
    print(reponse.text)

if __name__ == '__main__':
    text = input("输入生效地址(c 或者 z):")
    if text == "c":
        base_url="https://tycs.suapp.mobi"
        print("测试服地址")
    elif text=="z":
        base_url="http://161.189.70.26:9001"
        print("正式服地址")
    

    device_id="da0f3e8cadb247be"

    pkg_name=packagename()["suiyilian"]
    print(pkg_name)

    '''修改归因信息'''
    guiyin(
        base_url=base_url,
        pkg_name=pkg_name,
        device_id=device_id,
        media_source="bytedance_int",
        ad_site_ad="10001",
        campaign_id="test_ks"
        )

    '''移除黑名单'''
    guiyin(base_url=base_url,method="del-black-list",device_id=device_id,pkg_name=pkg_name)

    '''查看归因信息'''
    guiyin(base_url=base_url,method="query",device_id=device_id)

'''
https://tycs.suapp.mobi
http://161.189.70.26:9001

一. 归因来源, media_source: 1.organic (自然量) 2.bytedance_int (巨量) 3.ylh (优量汇)

二. AD SITE ID, 西瓜视频： 10001 -10099 火山小视频：30001-30099 抖音：40001-40099 穿山甲开屏广告： 800000000 穿山甲网盟非开屏广告：900000000 通投广告位：33013，38016

优量汇： 优量汇-微信 21 优量汇 15 其他的都算"优量汇-其它"

三. 测试环境修改 campaign_id 为 campaign_id_roi_test 下发巨量ROI策略

四 测试用户来源修改，归因为bytedance_int，将campain_id 改成 test_csj,test_dp,test_gdt,test_ks,test_ks_content,test_baidu，分别可以获取对应的策略
'''









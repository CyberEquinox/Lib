import time
from DrissionPage import WebPage
import json
import re
from datetime import datetime
import pytz

infs =  [
            {'ch_name': '包玉刚图书馆二楼二楼西北区（NW）', 'name': 'W2-NW', 'room_id': 973},
            {'ch_name': '包玉刚图书馆二楼二楼西南区（SW）', 'name': 'W2-SW', 'room_id': 1090},
            {'ch_name': '包玉刚图书馆三楼三楼西北区（NW）', 'name': 'W3-NW', 'room_id': 1219},
            {'ch_name': '包玉刚图书馆三楼三楼西南区（SW）', 'name': 'W3-SW', 'room_id': 1347},
            {'ch_name': '包玉刚图书馆三楼三楼东南区（SE）', 'name': 'W3-SE', 'room_id': 1543},
            {'ch_name': '包玉刚图书馆四楼四楼西北区（NW）', 'name': 'W4-NW', 'room_id': 1655},
            {'ch_name': '包玉刚图书馆四楼四楼西南区（SW）', 'name': 'W4-SW', 'room_id': 1715},
            {'ch_name': '包玉刚图书馆四楼四楼东北区（NE）', 'name': 'W4-NE', 'room_id': 1891},
            {'ch_name': '包玉刚图书馆四楼四楼东南区（SE）', 'name': 'W4-SE', 'room_id': 1915},
            {'ch_name': '包玉刚图书馆五楼五楼西北区（NW）', 'name': 'W5-NW', 'room_id': 2055},
            {'ch_name': '包玉刚图书馆五楼五楼东北区（NE）', 'name': 'W5-NE', 'room_id': 2085},
            {'ch_name': '包玉刚图书馆五楼五楼东南区（SE）', 'name': 'W5-SE', 'room_id': 2109},
            {'ch_name': '包玉刚图书馆六楼六楼西北区（NW）', 'name': 'W6-NW', 'room_id': 2149},
            {'ch_name': '包玉刚图书馆六楼六楼西南区（SW）', 'name': 'W6-SW', 'room_id': 2177},
            {'ch_name': '包玉刚图书馆六楼六楼东北区（NE）', 'name': 'W6-NE', 'room_id': 2325},
            {'ch_name': '包玉刚图书馆六楼六楼东南区（SE）', 'name': 'W6-SE', 'room_id': 2353},
            {'ch_name': '新上院一层东阅览室北区（N）', 'name': 'X1-N', 'room_id': 2391},
            {'ch_name': '新上院一层东阅览室南区（S）', 'name': 'X1-S', 'room_id': 2519},
            {'ch_name': '主馆二楼B200-东区（E）', 'name': 'LB2-E', 'room_id': 3373},
            {'ch_name': '主馆二楼B200-中区（M）', 'name': 'LB2-M', 'room_id': 3493},
            {'ch_name': '主馆二楼B200-西区（W）', 'name': 'LB2-W', 'room_id': 3633},
            {'ch_name': '主馆三楼B300-东区（E）', 'name': 'LB3-E', 'room_id': 4886},
            {'ch_name': '主馆三楼B300-中区（M）', 'name': 'LB3-M', 'room_id': 4986},
            {'ch_name': '主馆三楼B300-西区（W）', 'name': 'LB3-W', 'room_id': 5146},
            {'ch_name': '主馆四楼B400-东区（E）', 'name': 'LB4-E', 'room_id': 6103},
            {'ch_name': '主馆四楼B400-中区（M）', 'name': 'LB4-M', 'room_id': 6191},
            {'ch_name': '主馆四楼B400-西区（W）', 'name': 'LB4-W', 'room_id': 6329},
            {'ch_name': '李政道图书馆二楼二楼北区（N）', 'name': 'T2-N', 'room_id': 7092},
            {'ch_name': '李政道图书馆三楼三楼南区（S）', 'name': 'T3-S', 'room_id': 7298},
            {'ch_name': '李政道图书馆三楼三楼北区（N）', 'name': 'T3-N', 'room_id': 7340},
            {'ch_name': '李政道图书馆一楼李馆临时入馆预约', 'name': 'TLS', 'room_id': 7378},
            {'ch_name': '李政道图书馆四楼四楼北区（N）', 'name': 'T4-410', 'room_id': 7728},
            {'ch_name': '包玉刚图书馆联楼四楼联楼四楼东区（E）', 'name': 'WL4-E', 'room_id': 7758},
            {'ch_name': '包玉刚图书馆联楼四楼联楼四楼西区（W）', 'name': 'WL4-W', 'room_id': 7800},
            {'ch_name': '包玉刚图书馆联楼四楼联楼四楼移动座位（M）', 'name': 'WL4-M', 'room_id': 7864}
]



def wait(h, m, s):
    # print("Debug")# Debug
    beijing_tz = pytz.timezone('Asia/Shanghai')
    now = datetime.now(tz=beijing_tz)
    target_time = now.replace(hour=h, minute=m, second=s, microsecond=0)

    if target_time <= now:
        print("目标时间已经过了")
        return

    while now < target_time:
        total_seconds = (target_time - now).total_seconds()

        if total_seconds <= 10:
            print(f"现在时间{now}，还需等待{total_seconds}秒（最后10秒，每秒倒计时）")
            time.sleep(1)
        elif total_seconds <= 20:
            print(f"现在时间{now}，还需等待{total_seconds}秒")
            time.sleep(total_seconds - 10)
        elif total_seconds <= 60:
            print(f"现在时间{now}，还需等待{total_seconds}秒")
            time.sleep(10)
        elif total_seconds <= 120:
            print(f"现在时间{now}，还需等待{total_seconds}秒")
            time.sleep(total_seconds - 60)
        elif total_seconds <= 300:
            print(f"现在时间{now}，还需等待{total_seconds}秒")
            time.sleep(60)
        elif total_seconds <= 600:
            print(f"现在时间{now}，还需等待{total_seconds}秒")
            time.sleep(total_seconds - 300)
        else:
            print(f"现在时间{now}，还需等待{total_seconds}秒")
            time.sleep(300)

        now = datetime.now(tz=beijing_tz)

    print("时间到")

def lib_sit(book_info:dict):
    sit_id=book_info["sit_id"]
    data = book_info['data']
    start = book_info['start']
    end = book_info['end']
    room_id = -1
    for inf in infs:
        if inf['name'] == book_info['room']:
            room_id =inf['room_id']
    if room_id == -1:
        print('请检查room是否错误')
        return
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
        "Content-Type":"application/json;charset=UTF-8"}
    url = "https://libseat.sjtu.edu.cn/ic-web/reserve"
    log_in_url = "https://libseat.sjtu.edu.cn/#/ic/home"
    page = WebPage('d')
    # 登录并获取cookies和accNo
    wait(21, 57, 0)
    page.get(log_in_url)
    page.refresh()
    page.wait(5)
    if re.search('jaccount.sjtu.edu.cn',page.url):
        print("请登录")
    page.wait.url_change(text='/#/ic/home')
    cookies = page.cookies
    accNo = json.loads(page.get_session_storage("userInfo"))['accNo']
    data = {"sysKind": 8, "appAccNo": accNo, "memberKind": 1, "resvMember": [accNo],
            "resvBeginTime": f"{data} {start}",
            "resvEndTime": f"{data} {end}",
            "testName": "", "captcha": "", "resvProperty": 0, "resvDev": [room_id + sit_id], "memo": ""}
    data_json = json.dumps(data)

    # 抢座位
    page.change_mode()
    wait(22,00,0)
    try:
        print("请求发送,等待响应")
        page.post(url=url, data=data_json,headers=headers,cookies=cookies,timeout=120)
        print(f"响应:{page.json['message']}\n晚上10点系统繁忙，响应信息可能出错，实际情况以网页为准")
        # return page.json['data']['uuid'],page
    except Exception as e:
        print(e.__cause__)

if __name__ == "__main__":
    book_info={"room":"W6-SE","sit_id":30,'data': "2024-01-09", 'start': "10:00:00", 'end': "11:00:00"}
    lib_sit(book_info)

    # [
    #     {'ch_name': '包玉刚图书馆二楼二楼西北区（NW）', 'name': 'W2-NW', 'room_id': 973},
    #     {'ch_name': '包玉刚图书馆二楼二楼西南区（SW）', 'name': 'W2-SW', 'room_id': 1090},
    #     {'ch_name': '包玉刚图书馆三楼三楼西北区（NW）', 'name': 'W3-NW', 'room_id': 1219},
    #     {'ch_name': '包玉刚图书馆三楼三楼西南区（SW）', 'name': 'W3-SW', 'room_id': 1347},
    #     {'ch_name': '包玉刚图书馆三楼三楼东南区（SE）', 'name': 'W3-SE', 'room_id': 1543},
    #     {'ch_name': '包玉刚图书馆四楼四楼西北区（NW）', 'name': 'W4-NW', 'room_id': 1655},
    #     {'ch_name': '包玉刚图书馆四楼四楼西南区（SW）', 'name': 'W4-SW', 'room_id': 1715},
    #     {'ch_name': '包玉刚图书馆四楼四楼东北区（NE）', 'name': 'W4-NE', 'room_id': 1891},
    #     {'ch_name': '包玉刚图书馆四楼四楼东南区（SE）', 'name': 'W4-SE', 'room_id': 1915},
    #     {'ch_name': '包玉刚图书馆五楼五楼西北区（NW）', 'name': 'W5-NW', 'room_id': 2055},
    #     {'ch_name': '包玉刚图书馆五楼五楼东北区（NE）', 'name': 'W5-NE', 'room_id': 2085},
    #     {'ch_name': '包玉刚图书馆五楼五楼东南区（SE）', 'name': 'W5-SE', 'room_id': 2109},
    #     {'ch_name': '包玉刚图书馆六楼六楼西北区（NW）', 'name': 'W6-NW', 'room_id': 2149},
    #     {'ch_name': '包玉刚图书馆六楼六楼西南区（SW）', 'name': 'W6-SW', 'room_id': 2177},
    #     {'ch_name': '包玉刚图书馆六楼六楼东北区（NE）', 'name': 'W6-NE', 'room_id': 2325},
    #     {'ch_name': '包玉刚图书馆六楼六楼东南区（SE）', 'name': 'W6-SE', 'room_id': 2353},
    #     {'ch_name': '新上院一层东阅览室北区（N）', 'name': 'X1-N', 'room_id': 2391},
    #     {'ch_name': '新上院一层东阅览室南区（S）', 'name': 'X1-S', 'room_id': 2519},
    #     {'ch_name': '主馆二楼B200-东区（E）', 'name': 'LB2-E', 'room_id': 3373},
    #     {'ch_name': '主馆二楼B200-中区（M）', 'name': 'LB2-M', 'room_id': 3493},
    #     {'ch_name': '主馆二楼B200-西区（W）', 'name': 'LB2-W', 'room_id': 3633},
    #     {'ch_name': '主馆三楼B300-东区（E）', 'name': 'LB3-E', 'room_id': 4886},
    #     {'ch_name': '主馆三楼B300-中区（M）', 'name': 'LB3-M', 'room_id': 4986},
    #     {'ch_name': '主馆三楼B300-西区（W）', 'name': 'LB3-W', 'room_id': 5146},
    #     {'ch_name': '主馆四楼B400-东区（E）', 'name': 'LB4-E', 'room_id': 6103},
    #     {'ch_name': '主馆四楼B400-中区（M）', 'name': 'LB4-M', 'room_id': 6191},
    #     {'ch_name': '主馆四楼B400-西区（W）', 'name': 'LB4-W', 'room_id': 6329},
    #     {'ch_name': '李政道图书馆二楼二楼北区（N）', 'name': 'T2-N', 'room_id': 7092},
    #     {'ch_name': '李政道图书馆三楼三楼南区（S）', 'name': 'T3-S', 'room_id': 7298},
    #     {'ch_name': '李政道图书馆三楼三楼北区（N）', 'name': 'T3-N', 'room_id': 7340},
    #     {'ch_name': '李政道图书馆一楼李馆临时入馆预约', 'name': 'TLS', 'room_id': 7378},
    #     {'ch_name': '李政道图书馆四楼四楼北区（N）', 'name': 'T4-410', 'room_id': 7728},
    #     {'ch_name': '包玉刚图书馆联楼四楼联楼四楼东区（E）', 'name': 'WL4-E', 'room_id': 7758},
    #     {'ch_name': '包玉刚图书馆联楼四楼联楼四楼西区（W）', 'name': 'WL4-W', 'room_id': 7800},
    #     {'ch_name': '包玉刚图书馆联楼四楼联楼四楼移动座位（M）', 'name': 'WL4-M', 'room_id': 7864}
    # ]
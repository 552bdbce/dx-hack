#!/usr/bin/python
# _*_ coding: utf-8 _*_
import collections
import requests

URL = "https://hnwiglk0toqa.cybozu.com/k/v1/records.json?app=6"
API_TOKEN = "9HYvgsZ7JqlOpoppVQtaLIBiiPACL43YOeIVT9Lv"


def get_kintone(url, api_token):
    """kintoneのレコードを全件取得する関数"""
    headers = {"X-Cybozu-API-Token": api_token}
    resp = requests.get(url, headers=headers)

    return resp

def get_ranking():
    RESP = get_kintone(URL, API_TOKEN)

    # print(RESP.text)

    import json

    json_dict = json.loads(RESP.text)
    # print(json_dict.keys())
    # print(json_dict["records"])

    sports = []
    holiday = []
    food = []
    where = []
    travel = []

    for i in range(len(json_dict["records"]) - 1):
        sports.append(json_dict['records'][i]['sports']["value"])
        holiday.append(json_dict['records'][i]['holiday']["value"])
        food.append(json_dict['records'][i]['food']["value"])
        where.append(json_dict['records'][i]['from']["value"])
        travel.append(json_dict['records'][i]['travel']["value"])

    s = collections.Counter(sports)
    h = collections.Counter(holiday)
    f = collections.Counter(food)
    w = collections.Counter(where)
    t = collections.Counter(travel)
    s = s.most_common()
    h = h.most_common()
    f = f.most_common()
    w = w.most_common()
    t = t.most_common()
    ans = []
    # print(s[0])
    ans.append(list(s[0]))
    # print(h[0])  # ('ドライブ', 2)
    ans.append(list(h[0]))
    # print(f[0])
    ans.append(list(f[0]))
    # print(w[0])
    ans.append(list(w[0]))
    # print(type(t[0]))
    ans.append(list(t[0]))
    ans = sorted(ans, reverse=True, key=lambda x: x[1])
    # print(ans)
    return ans





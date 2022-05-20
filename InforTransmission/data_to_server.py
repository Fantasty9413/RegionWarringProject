#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2022/5/19 13:57
# @Author: Fantasty9413
# @File  : data_to_server.py

import requests
import sqlite3
import json
import Log

db_name = "TriggerInfo.db"
path = "./Data/"
db_path = path + db_name

db_table_name = "TriggerInfo"
db_table_keywords = ("EquipmentId", "TriggerDate", "TriggerTime", "TriggerNum", "PostFlag")

# URL = "http://a6f7dd6002dd.ngrok.io"
URL = "http://www.baidu.com"


# 发送一次triggerinfo
def post_triggerinfo(triggerinfo):
    body = json.dumps(triggerinfo)
    res = requests.post(url=URL, data=body, timeout=1)
    if res.status_code==200:
        post_flag = True
    else:
        post_flag = False
        Log.logger_report.info("Response error. Status code is %s." % res.status_code)
    return post_flag


# 记录post本条triggerinfo数据的信息至数据库
def record_postinfo(triggerinfo, postflag):
    # 利用日期和编号定位信息
    TriggerDate = triggerinfo.get("TriggerDate")    # 触发日期
    TriggerNum = triggerinfo.get("TriggerNum")      # 当日触发编号
    # 连接数据库
    con = sqlite3.connect(db_path)
    # 插入数据
    cur = con.cursor()
    sql_update = "update " + db_table_name + " set PostFlag = ? where TriggerDate = ? and TriggerNum = ?;"
    sql_values = (postflag, TriggerDate, TriggerNum)
    cur.execute(sql_update, sql_values)
    # 关闭数据库
    con.commit()
    con.close()


def Post(triggerinfo, retiescount=3):
    post_flag = False           # 发送标志置为False
    for index in range(0, retiescount):
        try:
            post_flag = post_triggerinfo(triggerinfo)
        except Exception as exc:                        # 发送info一次失败
            print(exc)
            Log.logger_exception.exception(exc)
            Log.logger_report.warning("Failed to post trigger information! Tried %s time." % index)
        else:
            if post_flag==True: break
    if post_flag == True: record_postinfo(triggerinfo, "True")    # 发送成功，改写数据库post_flag标志为True
    else: record_postinfo(triggerinfo, "False")


if __name__ == "__main__":
    test_info_dict = {"EquipmentId": "1", "TriggerDate": "xxx", "TriggerTime": "xxx", "TriggerNum": "1", "PostFlag": "False"}
    # res = post_triggerinfo(test_info_dict)
    # print(res)
    print(test_info_dict.get("TriggerTime"))
    record_postinfo(test_info_dict, "True")
    Post(test_info_dict)
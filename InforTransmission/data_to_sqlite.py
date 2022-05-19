#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2022/5/17 20:12
# @Author: Fantasty9413
# @File  : data_to_sqlite.py

import sqlite3
import os

db_name = "TriggerInfo.db"
path = "./Data/"
db_path = path + db_name

db_table_name = "TriggerInfo"
db_table_keywords = ("EquipmentId", "TriggerDate", "TriggerTime", "TriggerNum", "PostFlag")

# 数据库初始化
def db_initial():
    # 判断数据库是否存在，存在则删除
    if os.path.exists(db_path):
        os.remove(db_path)
    # 创建数据库文件
    con = sqlite3.connect(db_path)
    # 创建表单
    cur = con.cursor()
    keyword = str(db_table_keywords)
    keyword = keyword.replace(' ', '')
    keyword = keyword.replace('\'', '')
    sql = "CREATE TABLE IF NOT EXISTS " + db_table_name + keyword
    cur.execute(sql)
    con.commit()
    con.close()

# 插入至数据库
# triggerinfo以dict的形式
def db_insert_info(triggerinfo):
    # 构造values--存储要写入数据库的value
    info = ()
    for index in range(0, 5):
        info = info + (triggerinfo.get(db_table_keywords[index]),)
    # 连接数据库
    con = sqlite3.connect(db_path)
    # 插入数据
    cur = con.cursor()
    sql_ins = "insert into " + db_table_name + " values(?,?,?,?,?);"
    sql_values = info
    cur.execute(sql_ins, sql_values)
    # 关闭数据库
    con.commit()
    con.close()


if __name__ == "__main__":
    db_initial()
    test_info_dict = {"EquipmentId": "1", "TriggerDate": "xxx", "TriggerTime": "xxx", "TriggerNum": "1", "PostFlag": "False"}
    for index in range(0, 5):
        print(test_info_dict.get(db_table_keywords[index]))
    db_insert_info(test_info_dict)
    db_insert_info(test_info_dict)
    db_insert_info(test_info_dict)
#!/usr/bin/env Python
# coding=utf-8

from db import *

def select_table(table, column, condition, value):
    sql = "select " + column + " from " + table + " where " + condition + "='" + value + "'"
    cur.execute(sql)
    lines = cur.fetchall()
    return lines

def select_columns(table, column):
    sql = "select " + column + " from " + table
    cur.execute(sql)
    lines = cur.fetchall()
    return lines

def insert_user(table, value):
	sql = "insert into" + table + "(username,password,email) values (%s,%s,%s)" + value + "'"
	cur.execute(sql)
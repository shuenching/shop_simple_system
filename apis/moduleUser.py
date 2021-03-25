import sys
import time
import json
import requests
sys.path.append("..")
import db.user

def login(name, password):
  result = db.user.searchUserByNameAndPassword(name, password)
  if len(result) >= 1:
    token = result[0]['id'] + time.time()
    return {'success': True, 'msg': '登入成功', 'token': token}

def register(name, password, email):
  result = db.user.searchUserByName(name)
  if len(result) <= 0:
    db.user.setUser(name, password, email)
    result = db.user.searchUserByName(name)
    token = result[0]['id'] + time.time()
    return {'success': True, 'msg': '註冊成功', 'token':token}
  else:
    return {'success': False, 'msg': '帳號已使用'}
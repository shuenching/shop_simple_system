import sys
import time
import json
import requests
sys.path.append("..")
import db.user

currentToken = {}

def login(name, password):
  result = db.user.searchUserByNameAndPassword(name, password)
  if len(result) >= 1:
    token = result[0]['id'] + time.time()
    currentToken[name] = (token)
    return {'message': '登入成功', 'token': token, 'userInfo': {'name':result[0]['name'], 'id':result[0]['id'], 'email':result[0]['email']}}
  else:
    raise Exception()


def register(name, password, email):
  result = db.user.searchUserByName(name)
  if len(result) <= 0:
    db.user.setUser(name, password, email)
    result = db.user.searchUserByName(name)
    token = result[0]['id'] + time.time()
    currentToken[name] = (token)
    return {'message': '註冊成功', 'token':token}
  else:
    raise Exception()

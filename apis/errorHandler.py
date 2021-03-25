from flask import abort, jsonify

# code 1000 未登入
# code 1001 登入失敗
# code 1002 註冊失敗

def noToken(e):
  return abort(jsonify(message="請先登入", code=1000))

def loginFail(e):
  return abort(jsonify(message="登入失敗", code=1001))

def registerFail(e):
  return abort(jsonify(message="註冊失敗", code=1002))

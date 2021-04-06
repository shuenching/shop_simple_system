from flask import Flask, jsonify, request, abort
from .whiteList import NO_TOKEN_LIST
# from . import errorHandler

from . import moduleCommon
from . import moduleUser

app = Flask(__name__)
app.config["DEBUG"] = True

@app.errorhandler(410)
def loginFail(e):
  response=jsonify({'message':e.description['message'], 'code':e.description['code']})
  return response, 410

@app.before_request
def before_request():
  if request.path not in NO_TOKEN_LIST:
    try:
      token = request.headers.token
      moduleCommon.checkToken(token)
    except Exception as e:
      if len(e.args) <= 0:
        abort(410, {'message':"請先登入", 'code':1000})
      else:
        abort(410, {'message':e.args[0], 'code':e.args[1]})

@app.route('/api/user/login', methods=['POST'])
def userLogin():
  try:
    data = request.get_json()
    name = data['name']
    password = data['password']
    result = moduleUser.login(name, password)
    return jsonify(result)
  except Exception as e:
    print(e.args)
    if len(e.args) <= 0:
      abort(410, {'message':"登入失敗", 'code':1001})
    else:
      abort(410, {'message':e.args[0], 'code':e.args[1]})

@app.route('/api/user/register', methods=['POST'])
def userRegister():
  try:
    data = request.get_json()
    name = data['name']
    password = data['password']
    email = data['email']
    result = moduleUser.register(name, password, email)
    print(result)
    return jsonify(result)
  except Exception as e:
    if len(e.args) <= 0 :
      abort(410, {'message':"註冊失敗", 'code':1002})
    else:
      abort(410, {'message':e.args[0], 'code':e.args[1]})

def init():
  app.run()

if __name__ == '__main__':
  app.run()
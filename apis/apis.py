from flask import Flask, jsonify, request
from .whiteList import NO_TOKEN_LIST
from . import errorHandler

from . import moduleCommon
from . import moduleUser

app = Flask(__name__)
app.config["DEBUG"] = True

@app.before_request
def before_request():
  if request.path not in NO_TOKEN_LIST:
    try:
      token = request.headers.token
      moduleCommon.checkToken(token)
    except Exception as e:
      errorHandler.noToken(e)

@app.route('/api/user/login', methods=['POST'])
def userLogin():
  try:
    data = request.get_json()
    name = data['name']
    password = data['password']
    result = moduleUser.login(name, password)
    return jsonify(result)
  except Exception as e:
    errorHandler.loginFail(e)

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
    errorHandler.registerFail(e)

def init():
  app.run()

if __name__ == '__main__':
  app.run()
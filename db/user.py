from . import db

def searchUserByNameAndPassword(name, password):
  sql = "SELECT * FROM User WHERE name=%s AND password=%s"
  return db.get(sql, (name, password))

def searchUserByName(name):
  sql = "SELECT * FROM User WHERE name=%s"
  return db.get(sql, (name,))

def setUser(name, password, email):
  sql = "INSERT INTO User(name, password, email) values(%s, %s, %s)"
  return db.set(sql, (name, password, email))

if __name__ == "__main__" :
  db.connect('localhost', 'root', '', 'shop_simple')
  searchUserByNameAndPassword('oo0001', '123qwe')
import mysql.connector

def connect(host, user, password, db):
  global mydb 
  mydb = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=db
  )
  print(mydb)

def get(command):
  mycursor = mydb.cursor()
  mycursor.execute(command)
  return mycursor.fetchall()

def set(command, values):
  mycurosr = mydb.cursor()
  mycurosr.execute(command, val)
  mydb.commit()

if __name__ == '__main__':
  connect('localhost', 'root', '', 'shop_simple')
  result = get('SELECT * FROM User')
  print(result)
  # sql = 'INSERT INTO User (name, password, email) VALUES (%s,%s,%s)'
  # values = ('ooo0002', '123qwe', 'aaa@bbb.cc')
  # set(sql, values)
import db.db
import apis.apis


if __name__ == "__main__":
  db.db.connect('localhost', 'root', '', 'shop_simple')
  apis.apis.init()
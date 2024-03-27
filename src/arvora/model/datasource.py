# #this is a test
# import requests
# from tinydb import TinyDB, Query
#
# db = TinyDB('db.json')
#
# j = db.all()
#
# URL = 'http://anbubus.pythonanywhere.com/data'
# #response = requests.get(URL)
# response = requests.post(URL, json=j)
#
# if response.status_code == 200:
#     print(f"Yupiii{response.text}")
# elif response.status_code == 201:
#     print("Data created successfully")
# elif response.status_code == 404:
#     print("deu rui")
import requests
from tinydb import TinyDB, Query
import os
from base64 import decodebytes as dcd

TIMESTAMP_FORMAT = '@{:%Y%-m%-d% H%:M%}'
LOCAL_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), '../model'))
URL = "http://anbubus.pythonanywhere.com/data"
#PASSWORD = dcd(str.encode(os.environ["ANBUBUS_PASSWORD"])).decode("utf-8")

db = TinyDB(os.path.join(LOCAL_FOLDER, 'db.json'))

print("AAAAAAAAAA1")
def spike():
    print("AAAAAAAAAA")
    response = requests.get(URL, headers={'Authorization': "token1"})
    if response.status_code == 200:
        try:
            print(response.json())
            if db:
                db.drop_tables()
            db.insert(response.json())
        except:
            print("Server Error. Contact the administrator.")

    else:
        print(f"Error while connecting to server - {response.text} - {response.status_code}")


spike()


class DataSource:

    def __init__(self):
        pass
    def get_data(self):
        #return db.get()
        pass
    def create_data(self):
        pass
    def delete_data(self):
        pass

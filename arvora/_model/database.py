import os
import requests
from tinydb import TinyDB, Query


TIMESTAMP_FORMAT = '@{:%Y%-m%-d% H%:M%}'
LOCAL_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), '../_model'))
URL = "http://0.0.0.0:8888"
#PASSWORD = dcd(str.encode(os.environ["ANBUBUS_PASSWORD"])).decode("utf-8")

db = TinyDB(os.path.join(LOCAL_FOLDER, 'db.json'))
class Database:
    @classmethod
    def get_data(cls):
        return db.all()

    @classmethod
    def post_data(cls):
        response = requests.get(URL)
        if response.status_code == 200:
            return {"status": "yupiii"}
        return None

    @classmethod
    def delete_data(self):
        pass
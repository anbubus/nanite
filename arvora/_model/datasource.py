from tinydb import TinyDB, Query

db = TinyDB('db.json')
def get_datasource(ev):
    db.insert(ev)
    return print("All good")























# #this is a test
# import os
# import requests
# from tinydb import TinyDB, Query
# import tornado.web
# from tornado.ioloop import IOLoop
# from tornado.options import define, options
# from tornado.escape import xhtml_escape
# from base64 import decodebytes as dcd
#
#
#
#
#
# # URL = 'http://anbubus.pythonanywhere.com/data'
# # #response = requests.get(URL)
# # response = requests.post(URL, json=j)
# #
# # if response.status_code == 200:
# #     print(f"Yupiii{response.text}")
# # elif response.status_code == 201:
# #     print("Data created successfully")
# # elif response.status_code == 404:
# #     print("deu rui")
#
#
#
# TIMESTAMP_FORMAT = '@{:%Y%-m%-d% H%:M%}'
# LOCAL_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), '../_model'))
# URL = "http://anbubus.pythonanywhere.com/data"
# #PASSWORD = dcd(str.encode(os.environ["ANBUBUS_PASSWORD"])).decode("utf-8")
#
# db = TinyDB(os.path.join(LOCAL_FOLDER, 'db.json'))
#
# class MainHandler(tornado.web.RequestHandler):
#     def initialize(self):
#         self.render("index.html")
# class DataHandler(tornado.web.RequestHandler):
#     def get(self):
#         data = db.all()
#         self.write({"data":data})
#     def post(self):
#         new_data = tornado.escape.json_decode(self.request.body)
#         db.insert(new_data)
#         self.write({"status": "success"})
#
# application = tornado.web.Application([
#     #(r'/', MainHandler),
#     (r'/data', DataHandler),
# ], view_path="src/arvora/view")
#
# if __name__ == "__main__":
#     application.listen(8880)
#     print("Tornado server started and listening on port 8888")
#     tornado.ioloop.IOLoop.current().start()
#
#
#
#
#
#
#



# print("AAAAAAAAAA1")
# def spike():
#     print("AAAAAAAAAA")
#     response = requests.get(URL, headers={'Authorization': "token1"})
#     if response.status_code == 200:
#         try:
#             print(response.json())
#             if db:
#                 db.drop_tables()
#             db.insert(response.json())
#         except:
#             print("Server Error. Contact the administrator.")
#
#     else:
#         print(f"Error while connecting to server - {response.text} - {response.status_code}")
#
#
# spike()
#
#
# class DataSource:
#
#     def __init__(self):
#         pass
#     def get_data(self):
#         return db.all()
#     def create_data(self, article):
#         return db.insert(article) if article is not None else None
#     def delete_data(self):
#         pass

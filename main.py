from flask import Flask
from flask_restful import Resource, Api
from random import choice
from requests import get 
from datetime import datetime as dt 
from pymongo import MongoClient
import os 

app = Flask(__name__)
api = Api(app)

endpoint_db = os.getenv('MONGODB_URL')

client = MongoClient(endpoint_db)
db = client['firma_database']
tabela_pub = db['tbl_pub_clients']
tabela_solo = db['tbl_iot_solo']
tabela_blood = db['tbl_sangue']
tabela_address  = db['tbl_endereco']

class coffe(Resource):
    def get(self):
        endpoint = "https://random-data-api.com/api/coffee/random_coffee"
        data = {"size":50}
        r = get(endpoint,data).json()
        try: 
          tabela_solo.insert_many(r)
          status = "Done !"
        except:
          status = "Falha"
        return {"tabela":"coffe","data": status, "total_insert": len(r), "dt":str(dt.now())}

class food(Resource):
    def get(self):
        endpoint = "https://random-data-api.com/api/food/random_food"
        data = {"size":20}
        r = get(endpoint,data).json()
        try: 
          tabela_pub.insert_many(r)
          status = "Done !"
        except:
          status = "Falha"
        return {"tabela":"food","data": status, "total_insert": len(r), "dt":str(dt.now())}


class blood(Resource):
    def get(self):
        endpoint = "https://random-data-api.com/api/blood/random_blood"
        data = {"size":20}
        r = get(endpoint,data).json()
        try: 
          tabela_blood.insert_many(r)
          status = "Done !"
        except:
          status = "Falha"
        return {"tabela":"food","data": status, "total_insert": len(r), "dt":str(dt.now())}

class address (Resource):
    def get(self):
        endpoint = "https://random-data-api.com/api/address/random_address"
        data = {"size":20}
        r = get(endpoint,data).json()
        try: 
          tabela_address.insert_many(r)
          status = "Done !"
        except:
          status = "Falha"
        return {"tabela":"food","data": status, "total_insert": len(r), "dt":str(dt.now())}



class alive(Resource):
    def get(self):
        return {'data': str(dt.now())}


api.add_resource(coffe, '/api/v1/coffe/ativos')
api.add_resource(food, '/api/v1/food/ativos')
api.add_resource(blood, '/api/v1/blood/ativos')

api.add_resource(address, '/api/v1/address/ativos')


api.add_resource(alive, '/')
# https://api-gt-services.juanengml.repl.co/api/v1/coffe/ativos

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8082, debug=True)
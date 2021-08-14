from flask import Flask
from flask_restful import Resource, Api
from random import choice
from faker import Faker
from datetime import datetime as dt 
from pymongo import MongoClient
import os 
fake = Faker()

app = Flask(__name__)
api = Api(app)

endpoint_db = os.getenv('MONGODB_URL')

client = MongoClient(endpoint_db)
db = client['users_database']

def data_users(): # usuarios vindo de publicidade
   tabela = db['tbl_pub_clients']
   nome  = fake.name()
   value = {
     "nome": nome,
     "idade": choice(range(18,54)), 
     "sexo": choice(["masculino","feminino"]),
     "numero": fake.phone_number(),
     "endereco": fake.address(),
     "ipv4":fake.ipv4_private(),
     "navegador":choice(["Mozilla","IE","Chrome","Opera","EDGE"]),
     "site":choice(["www.g1.com.br","www.facebook.com","www.twitter.com","www.tiktok.com","www.oestadao.com.br","www.g1.globo.com.br"]),
     "email":nome.split()[1].lower() + choice(["@gmail.com","@outlook.com","@net.com"]),
     "dt":str(dt.now())
   }
   tabela.insert_one(value)
   return value

def data_iot(): # dados de iot solo
  tabela = db['tbl_iot_solo']
  value = {
    "temperatura":choice(range(10,60)),
    "umidade": choice(range(0,100)),
    "ph_solo": choice(range(100)),
    "controlador_agua":choice([1,0]), 
    "id_device": choice(range(60)),
    "dt":str(dt.now()),
    "falha":choice([1,0])
  }
  tabela.insert_one(value)
  return value



class Client(Resource):
    def get(self):
        return {"data":[ data_users() for _ in  range(choice(range(1000,5000))) ]}

class FarmIot(Resource):
    def get(self):
        return {"data":[ data_iot() for _ in range(choice(range(1000,5000)))]}

class alive(Resource):
    def get(self):
        return {'data': str(dt.now())}


api.add_resource(Client, '/api/v1/users/ativos')
api.add_resource(FarmIot, '/api/v1/iot/ativos')

api.add_resource(alive, '/')


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8082, debug=True)
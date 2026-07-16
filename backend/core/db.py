import os
from mongoengine import connect
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv(
    "MONGO_URI",
    "mongodb://obaid:Obaid123@ac-gvnhooj-shard-00-00.phjyq4l.mongodb.net:27017,ac-gvnhooj-shard-00-01.phjyq4l.mongodb.net:27017,ac-gvnhooj-shard-00-02.phjyq4l.mongodb.net:27017/devflow?authSource=admin&replicaSet=atlas-13zada-shard-0&tls=true&retryWrites=true&w=majority&appName=Cluster0"
)

connect(host=MONGO_URI)
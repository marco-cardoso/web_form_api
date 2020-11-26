import os

from pymongo import MongoClient


class Database:

    def __init__(self) -> None:
        super().__init__()

        mongo_database = os.environ.get("MONGO_DATABASE")
        mongo_host = os.environ.get("MONGO_HOST")
        mongo_port = int(os.environ.get("MONGO_PORT"))
        mongo_root_username = os.environ.get("MONGO_USERNAME")
        mongo_root_passwd = os.environ.get("MONGO_PASSWORD")

        if (mongo_root_username is not None) and (mongo_root_passwd is not None):
            mongo_url = f"mongodb://{mongo_root_username}:{mongo_root_passwd}@{mongo_host}:{mongo_port}"
        else:
            mongo_url = f"mongodb://{mongo_host}:{mongo_port}"

        client = MongoClient(
            mongo_url,
            maxPoolSize=20
        )

        self.db = client[mongo_database]


db = Database()

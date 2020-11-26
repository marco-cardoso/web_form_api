import uuid

from pymongo import MongoClient
from pymongo.cursor import Cursor
from pymongo.results import InsertOneResult

COLLECTION = "forms"


def insert(client: MongoClient, document: dict) -> InsertOneResult:
    return client[COLLECTION].insert_one(document)


def find_all(client: MongoClient) -> Cursor:
    return client[COLLECTION].find({})


def find_by_id(client: MongoClient, id: uuid):
    return client[COLLECTION].find({'_id': id})[0]

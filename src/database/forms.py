"""
    Module with the methods related to the 'forms' database collection
"""

from bson.objectid import ObjectId

from pymongo import MongoClient
from pymongo.cursor import Cursor
from pymongo.results import InsertOneResult
import logging

COLLECTION = "forms"

_logger = logging.getLogger(__name__)


def insert(client: MongoClient, document: dict) -> InsertOneResult:
    _logger.info("Inserting new form into the database")
    return client[COLLECTION].insert_one(document)


def find_all(client: MongoClient) -> Cursor:
    _logger.info("Getting all the forms in the database")
    return client[COLLECTION].find({})


def find_by_id(client: MongoClient, id):
    _logger.info("Search for the Form ID " + id )
    return client[COLLECTION].find({'_id': ObjectId(id)}, {'_id' : False})[0]

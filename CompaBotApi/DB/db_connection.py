from bson import json_util
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()


class ChatBotRepository():
    ATLAS_URI = os.getenv('ATLAS_URI')
    DB_NAME = os.getenv('DB_NAME')
    DATASET_COLLECTION_NAME = os.getenv('DATASET_COLLECTION_NAME')
    QUESTIONS_COLLECTION_NAME = os.getenv('QUESTIONS_COLLECTION_NAME')
    COUNTRIES_INFO_DATASET = os.getenv('COUNTRIES_INFO_DATASET')

    def __init__(self):
        self.mongodb_client = MongoClient(self.ATLAS_URI)
        self.database = self.mongodb_client[self.DB_NAME]

    def ping(self):
        self.mongodb_client.admin.command('ping')
        print('Connected to Atlas instance! We are good to go!')

    def get_collection(self, collection_name):
        collection = self.database[collection_name]
        return collection

    def find_dataset(self):
        keywords = self.find(self.DATASET_COLLECTION_NAME)
        return keywords[0]

    def find_questions(self):
        questions_collection = self.database.get_collection('questions')
        questions = questions_collection.find({}, projection={'_id': False})
        return questions

    def find_country(self, country):
        countries_info = self.find(self.COUNTRIES_INFO_DATASET, {"country": country})
        if countries_info:
            return countries_info[0]
        else:
            raise Exception("The country was not found")

    def find_all_countries(self):
        countries = self.find(self.COUNTRIES_INFO_DATASET)
        if countries:
            return countries
        else:
            raise Exception("Error trying to retrieve the countries")

    def find(self, collection_name, filter={}, limit=0):
        collection = self.database[collection_name]
        items = list(collection.find(filter=filter, limit=limit, projection={'_id': False}))
        return items

    def get_answer(self, intent):
        questions = self.find(self.QUESTIONS_COLLECTION_NAME, {"intent": intent})
        if questions:
            return questions[0]["respuesta"]
        else:
            raise Exception("Error trying to retrieve the questions")

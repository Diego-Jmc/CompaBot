from pymongo.mongo_client import MongoClient
class ChatBotRepository():
    ATLAS_URI = "mongodb+srv://diegojmoravia:planahead12345@cluster0.rkgclhv.mongodb.net/?appName=Cluster0"
    DB_NAME = 'CompaBot'
    DATASET_COLLECTION_NAME = 'keywords'
    QUESTIONS_COLLECTION_NAME = 'questions'
    COUNTRIES_INFO_DATASET = 'countries'

    def __init__(self):
        self.mongodb_client = MongoClient(self.ATLAS_URI)
        self.database = self.mongodb_client[self.DB_NAME]

    ## A quick way to test if we can connect to Atlas instance
    def ping(self):
        self.mongodb_client.admin.command('ping')
        print('Connected to Atlas instance! We are good to go!')

    def get_collection(self, collection_name):
        collection = self.database[collection_name]
        return collection

    def find_dataset(self):
        keywords = self.find(self.DATASET_COLLECTION_NAME)
        if '_id' in keywords[0]:
            keywords[0].pop('_id')
            return keywords[0]
        else:
            raise Exception("Error trying to retrieve the dataset")

    def find_questions(self):
        questions = self.find(self.QUESTIONS_COLLECTION_NAME)
        if '_id' in questions:
            questions.pop('_id')
            return questions
        else:
            raise Exception("Error trying to retrieve the questions")

    def find_country(self, country):
        countries_info = self.find(self.COUNTRIES_INFO_DATASET,{"country":country})
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
        items = list(collection.find(filter=filter, limit=limit))
        return items

    def get_answer(self, intent):
        questions = self.find(self.QUESTIONS_COLLECTION_NAME,{"intent":intent})
        if questions:
            return questions[0]["respuesta"]
        else:
            raise Exception("Error trying to retrieve the questions")


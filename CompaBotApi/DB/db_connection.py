from pymongo.mongo_client import MongoClient
class ChatBotRepository():
    ATLAS_URI = "mongodb+srv://diegojmoravia:planahead12345@cluster0.rkgclhv.mongodb.net/?appName=Cluster0"
    DB_NAME = 'CompaBot'
    DATASET_COLLECTION_NAME = 'keywords'

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
            return keywords
        else:
            raise Exception("Error trying to retrieve the dataset")

    def find(self, collection_name, filter={}, limit=0):
        collection = self.database[collection_name]
        items = list(collection.find(filter=filter, limit=limit))
        return items

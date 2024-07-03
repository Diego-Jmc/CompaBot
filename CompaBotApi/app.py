from flask import Flask

from DB.db_connection import ChatBotRepository

app = Flask(__name__)

atlas_client = ChatBotRepository()
atlas_client.ping()

try:
    dataset = atlas_client.find_dataset()
    print(dataset)
except Exception as error:
    print(error)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

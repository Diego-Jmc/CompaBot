from flask import Flask
from flask import Flask, json, jsonify, request

from Bot.compa_bot import CompaBot
from DB.db_connection import ChatBotRepository

app = Flask(__name__)

compaBot = CompaBot()


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/questions')
def get_questions():
    questions = compaBot.get_questions()
    return jsonify(questions)


@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get("question")
    answer = compaBot.get_answer(question)
    return jsonify(answer)


if __name__ == '__main__':
    app.run()

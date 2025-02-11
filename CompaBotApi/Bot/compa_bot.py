import re
import unicodedata
from Bot.answers_generator import AnswerGenerator
from DB.db_connection import ChatBotRepository


class CompaBot():
    chatBotRepository = ChatBotRepository()

    def __init__(self):
        self.dataset = self.chatBotRepository.find_dataset()

    # cleans all the text to converting to lowercase and removes especial characters
    def normalize_question(self, question):
        question = question.lower()
        question = unicodedata.normalize('NFKD', question).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        question = re.sub(r'[^a-z0-9\s]', '', question)
        question = re.sub(r'\s+', ' ', question).strip()
        return question.split()

    def classifyQuestion(self, question):
        categories = {category: 0 for category in self.dataset}

        for word in question:
            for category, keywords in self.dataset.items():
                if word in keywords:
                    categories[category] += 1

        max_category = max(categories, key=categories.get)

        return {"category": max_category, "matches": categories[max_category], "question": question}

    def get_answer(self, question):
        if "".join(question.split()) is "":
            return "Parece que tu mensaje esta en blanco , porfavor suministra una pregunta valida."
        else:
            question = self.normalize_question(question)  #normalize question before clasification
            result = self.classifyQuestion(question)
            return self.generate_answer(result)

    def generate_answer(self, result):
        generator = AnswerGenerator(result)
        return generator.generate_answer()

    def get_questions(self):
        return self.chatBotRepository.find_questions()

from abc import abstractmethod
from unittest import result

from DB.db_connection import ChatBotRepository


class Generator():
    chatBotRepository = ChatBotRepository()

    def __init__(self, crit):
        self.crit = crit

    @abstractmethod
    def do_operation(self, crit=""):
        pass


class DevInfoGenerator(Generator):
    def do_operation(self, crit=""):
        return "El desarrollador se llama Diego Jiménez C , Nacido en 2001 en San Jose Costa Rica."


class CountryCapitalInfoGenerator(Generator):

    def do_operation(self, crit=""):
        try:

            countries = [e["country"] for e in self.chatBotRepository.find_all_countries()]
            found_country = ""
            joined_countries = "".join(crit).lower()
            joined_countries = joined_countries.replace(" ", "")

            for country in countries:
                original = country
                country = country.lower()
                country = country.replace(" ", "")
                if country in joined_countries:
                    found_country = original
                    break

            country = self.chatBotRepository.find_country(found_country)
            return f"La capital de {found_country} es {country["city"]}"

        except Exception as e:
            return f"Lo siento , porfavor escribe un país válido "


class SecurityInfoGenerator(Generator):
    def do_operation(self, crit=""):
        return "Esta aplicacion usa varios metodos de seguridad como el uso de variables de ambiente"


class FunctionalityInfoGenerator(Generator):
    def do_operation(self, crit=""):
        return """
            El algoritmo consiste en hacer una limpieza del input (osea de la pregunta) y comparar el numero
            de aciertos de palabras con el conjunto de datos que se tienen de entrenamiento , este modelo
            funciona mejor dependiendo del numero de datos que existan.
        """


class AnswerGenerator():

    def __init__(self, result):

        self.result = result
        self.generators = {
            "DevInfo": DevInfoGenerator(result["category"]),
            "CountryCapitalInfo": CountryCapitalInfoGenerator(result["category"]),
            "SecurityInfo": SecurityInfoGenerator(result["category"]),
            "FunctionalityInfo": FunctionalityInfoGenerator(result["category"])
        }

    def generate_answer(self):

        if 2 > self.result["matches"] > 0:
            return (f"Creo que tu pregunta esta relacionada con: {self.result["category"]} , pero no tengo información "
                    f"suficiente para responder , porfavor formula tu pregunta con un poco mas de contexto.")
        else:
            return self.generators[self.result["category"]].do_operation(self.result["question"])

from abc import abstractmethod

from DB.db_connection import ChatBotRepository


class Generator():
    chatBotRepository = ChatBotRepository()

    def __init__(self, attributes):
        self.crit = attributes

    @abstractmethod
    def do_operation(self, attributes={}):
        try:
            answer = self.chatBotRepository.get_answer(attributes.intent)
            return answer
        except Exception as e:
            return "No se pudo procesar la pregunta"


class DevInfoGenerator(Generator):
    def __init__(self, attributes):
        super().__init__(attributes)
        self.crit = attributes


class FunctionalityInfoGenerator(Generator):
    def __init__(self, attributes):
        super().__init__(attributes)
        self.crit = attributes


class LanguagesFunctionalityInfoGenerator(Generator):
    def __init__(self, attributes):
        super().__init__(attributes)
        self.crit = attributes


class PlanetsFunctionalityInfoGenerator(Generator):
    def __init__(self, attributes):
        super().__init__(attributes)
        self.crit = attributes


class WorldPlacesGenerator(Generator):
    def __init__(self, attributes):
        super().__init__(attributes)
        self.crit = attributes


class CountryCapitalInfoGenerator(Generator):
    def __init__(self, attributes):
        super().__init__(attributes)
        self.crit = attributes


class SecurityInfoGenerator(Generator):
    def __init__(self, attributes):
        super().__init__(attributes)
        self.crit = attributes


class CuriosityInfoGenerator(Generator):
    def __init__(self, attributes):
        super().__init__(attributes)
        self.crit = attributes


class OceanInfoGenerator(Generator):
    def __init__(self, attributes):
        super().__init__(attributes)
        self.crit = attributes


class MusicInfoGenerator(Generator):
    def __init__(self, attributes):
        super().__init__(attributes)
        self.crit = attributes


class WeatherInfoGenerator(Generator):
    def __init__(self, attributes):
        super().__init__(attributes)
        self.crit = attributes


class CountryCapitalInfoGenerator(Generator):
    def __init__(self, attributes):
        super().__init__(attributes)
        self.crit = attributes

    def do_operation(self, attributes=""):
        try:

            countries = [e["country"] for e in self.chatBotRepository.find_all_countries()]
            found_country = ""
            joined_countries = "".join(attributes).lower()
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


class AnswerGenerator():

    def __init__(self, result):

        self.result = result
        self.generators = {
            "DevInfo": DevInfoGenerator(result["category"]),
            "CountryCapitalInfo": CountryCapitalInfoGenerator(result["category"]),
            "SecurityInfo": SecurityInfoGenerator(result["category"]),
            "FunctionalityInfo": FunctionalityInfoGenerator(result["category"]),
            "Languages": LanguagesFunctionalityInfoGenerator(result["category"]),
            "Planets": PlanetsFunctionalityInfoGenerator(result["category"]),
        }

    def generate_answer(self):

        if 2 > self.result["matches"] > 0:
            return (f"Creo que tu pregunta esta relacionada con: {self.result["category"]} , pero no tengo información "
                    f"suficiente para responder , porfavor formula tu pregunta con un poco mas de contexto.")
        else:
            return self.generators[self.result["category"]].do_operation(self.result["attributes"])

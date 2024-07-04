from abc import abstractmethod

from DB.db_connection import ChatBotRepository


#application of the strategy pattern for the implementation of each question
class Generator():
    chatBotRepository = ChatBotRepository()

    def __init__(self, attributes):
        self.attributes = attributes

    @abstractmethod
    def do_operation(self):
        try:
            answer = self.chatBotRepository.get_answer(self.attributes["category"])
            return answer
        except Exception as e:
            return "No se pudo procesar la pregunta"

class DevInfoGenerator(Generator):
    def __init__(self, attributes):
        super().__init__(attributes)
        self.attributes = attributes

    def do_operation(self):
        base_result = super().do_operation()
        return base_result

class FunctionalityInfoGenerator(Generator):
    def __init__(self, attributes):
        super().__init__(attributes)
        self.attributes = attributes

class LanguagesFunctionalityInfoGenerator(Generator):
    def __init__(self, attributes):
        super().__init__(attributes)
        self.crit = attributes

class PlanetsFunctionalityInfoGenerator(Generator):
    def __init__(self, attributes):
        super().__init__(attributes)
        self.attributes = attributes

class WorldPlacesGenerator(Generator):
    def __init__(self, attributes):
        super().__init__(attributes)
        self.attributes = attributes

class CountryCapitalInfoGenerator(Generator):
    def __init__(self, attributes):
        super().__init__(attributes)
        self.attributes = attributes

class SecurityInfoGenerator(Generator):
    def __init__(self, attributes):
        super().__init__(attributes)
        self.attributes = attributes

class CuriosityInfoGenerator(Generator):
    def __init__(self, attributes):
        super().__init__(attributes)
        self.attributes = attributes

class OceanInfoGenerator(Generator):
    def __init__(self, attributes):
        super().__init__(attributes)
        self.attributes = attributes

class MusicInfoGenerator(Generator):
    def __init__(self, attributes):
        super().__init__(attributes)
        self.attributes = attributes

class WeatherInfoGenerator(Generator):
    def __init__(self, attributes):
        super().__init__(attributes)
        self.attributes = attributes

class CountryCapitalInfoGenerator(Generator):
    def __init__(self, attributes):
        super().__init__(attributes)
        self.attributes = attributes

    def do_operation(self):
        try:

            countries = [e["country"] for e in self.chatBotRepository.find_all_countries()]
            found_country = ""
            joined_countries = "".join(self.attributes["question"]).lower()
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
        # function dictionary that stores all the strategies for every available question
        self.result = result
        self.generators = {

            "Desarrollador": DevInfoGenerator(result),
            "Capitales": CountryCapitalInfoGenerator(result),
            "Seguridad": SecurityInfoGenerator(result),
            "Funcionalidad": FunctionalityInfoGenerator(result),
            "Lenguajes": LanguagesFunctionalityInfoGenerator(result),
            "Planetas": PlanetsFunctionalityInfoGenerator(result),
            "Maravillas": PlanetsFunctionalityInfoGenerator(result),
            "Curiosidad": CuriosityInfoGenerator(result),
            "Geografia": OceanInfoGenerator(result),
            "Musica": MusicInfoGenerator(result),
        }
    def generate_answer(self):

        if 2 > self.result["matches"] > 0:
            return (f"Creo que tu pregunta esta relacionada con: {self.result["category"]} , pero no tengo información "
                    f"suficiente para responder , porfavor formula tu pregunta con un poco mas de contexto.")
        else:
            return self.generators[self.result["category"]].do_operation()

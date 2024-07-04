from abc import abstractmethod

from DB.db_connection import ChatBotRepository


class Generator():
    chatBotRepository = ChatBotRepository()

    def __init__(self, question):
        self.crit = question

    @abstractmethod
    def do_operation(self, question=""):
        pass


class DevInfoGenerator(Generator):
    def do_operation(self, question=""):
        return "El desarrollador se llama Diego Jiménez C , Nacido en 2001 en San Jose Costa Rica."


class CountryCapitalInfoGenerator(Generator):

    def do_operation(self, question=""):
        try:

            countries = [e["country"] for e in self.chatBotRepository.find_all_countries()]
            found_country = ""
            joined_countries = "".join(question).lower()
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
    def do_operation(self, question=""):
        return "Esta aplicacion usa varios metodos de seguridad como el uso de variables de ambiente"


class FunctionalityInfoGenerator(Generator):
    def do_operation(self, question=""):
        return """
        El algoritmo consiste en hacer una limpieza del input (es decir, de la pregunta) y comparar el número de aciertos 
        de palabras con el conjunto de datos que se tienen de entrenamiento. Este modelo funciona mejor dependiendo del número
        de datos que existan.
        """


class LanguagesFunctionalityInfoGenerator(Generator):
    def do_operation(self, question=""):
        return """
        1.Python
        2.JavaScript
        3.Java
        4.C++
        5.C#
        6.PHP
        7.TypeScript
        8.Ruby
        9.Swift
        10.Go       
        """
class PlanetsFunctionalityInfoGenerator(Generator):
    def do_operation(self, question=""):
        return """
        1. Mercurio
        2. Venus
        3. Tierra
        4. Marte
        5. Júpiter
        6. Saturno
        7. Urano
        8. Neptuno
        9. Plutón
        """
class WorldPlacesGenerator(Generator):
    def do_operation(self, question=""):
        return """
1. Gran Pirámide de Guiza
   - Ubicación: Guiza, Egipto

2. Jardines Colgantes de Babilonia
   - Ubicación: Babilonia, Irak (ubicación exacta no confirmada)

3. Estatua de Zeus en Olimpia
   - Ubicación: Olimpia, Grecia

4. Templo de Artemisa en Éfeso
   - Ubicación: Éfeso, Turquía

5. Mausoleo de Halicarnaso
   - Ubicación: Bodrum, Turquía

6. Coloso de Rodas
   - Ubicación: Isla de Rodas, Grecia

7. Faro de Alejandría
   - Ubicación: Alejandría, Egipto

Maravillas del Mundo Moderno:
1. Chichén Itzá
   - Ubicación: Yucatán, México

2. Cristo Redentor
   - Ubicación: Río de Janeiro, Brasil

3. Gran Muralla China
   - Ubicación: China

4. Machu Picchu
   - Ubicación: Cuzco, Perú

5. Petra
   - Ubicación: Ma'an, Jordania

6. El Coliseo
   - Ubicación: Roma, Italia

7. Taj Mahal
   - Ubicación: Agra, India

"""


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
            return self.generators[self.result["category"]].do_operation(self.result["question"])


#Pour avoir la missing key
from collections import defaultdict
import json


class Question():
    def __init__(self, id, position, title, text, image, responses):
        self.id = id
        self.position = position
        self.title = title
        self.text = text
        self.image = image
        self.responses = responses

        #La méthode __dict__ est utilisée pour obtenir un dictionnaire contenant les attributs de l'instance de la classe Question
        #Ce dictionnaire est ensuite sérialisé en JSON à l'aide de la fonction json.dumps()
        #json.loads() est utilisée pour convertir une chaîne JSON en un dictionnaire Python
    
    def questionToJSON(self, reponsesData):
        print("reponses questions to json")
        print(reponsesData)
        dict_reponses = []
        for reponse in reponsesData :
            if (reponse[3].lower() == 'true'):
                dict_reponses.append({'text': str(reponse[2]),'isCorrect': True})
            else:
                dict_reponses.append({'text': str(reponse[2]),'isCorrect': False})
        dict_data = {
            'id' : self.id,
            'position' : self.position,
            'text' : self.text,
            'title' : self.title,
            'image': self.image,
            'possibleAnswers' : dict_reponses,
        }
        my_json = json.dumps(dict_data)
        return my_json
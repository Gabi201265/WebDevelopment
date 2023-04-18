import json



class Question():
    def __init__(self, id : int, position : int, title : str, text : str, image : str, responses):
        self.id = id
        self.position = position
        self.title = title
        self.text = text
        self.image = image
        self.responses = responses

    def questionToJSON(self):
        #La méthode __dict__ est utilisée pour obtenir un dictionnaire contenant les attributs de l'instance de la classe Question
        #Ce dictionnaire est ensuite sérialisé en JSON à l'aide de la fonction json.dumps()
        question_json = json.dumps(self.__dict__)
        return question_json
    
    def questionToPython(self):
        #json.loads() est utilisée pour convertir une chaîne JSON en un dictionnaire Python
        question_dict = json.loads(self)
        #Ce dictionnaire est ensuite utilisé pour initialiser une instance de la classe Question à l'aide de l'opérateur **, qui permet de déballer un dictionnaire en arguments nommés.
        return Question(**question_dict)
    
    def addResponses(self, responses):
        print("reponses questions to json")
        print(responses)
        dict_reponses = []
        for reponse in responses :
            if (reponse[1].lower() == 'true'):
                dict_reponses.append({'text': str(reponse[0]),'isCorrect': True})
            else:
                dict_reponses.append({'text': str(reponse[0]),'isCorrect': False})
        dict = {
            'id' : self.id,
            'position' : self.position,
            'text' : self.text,
            'title' : self.title,
            'image': self.image,
            'possibleAnswers' : dict_reponses,
        }
        return Question(dict)
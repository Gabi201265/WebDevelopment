from flask import Flask, request
from flask_cors import CORS
import hashlib
from jwt_utils import build_token, decode_token
import question, participation, generateDb

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
	x = 'world'
	return f"Hello, {x} !!"

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	#return {"size": 0, "scores": []}, 200
	return question.GetQuizInfo()

@app.route('/login', methods=['POST'])
def GetQuizLogin():
	payload = request.get_json()
	tried_password = payload['password'].encode('UTF-8')
	hashed = hashlib.md5(tried_password).digest()
	if hashed == b'\xd8\x17\x06PG\x92\x93\xc1.\x02\x01\xe5\xfd\xf4_@':
		monToken = build_token()
		print(monToken)
		return {"token": monToken}, 200
	else:
		return 'Unauthorized', 401

def checkAuth():
     # Récupérer le token envoyé en paramètre
     token = request.headers.get('Authorization')
     if (token):
          try : 
               decode_token(token.replace("Bearer ", ""))
               return True
          except Exception as e:
               print(e)
               return False
     else:
          return False
     
@app.route('/questions', methods=['POST'])
def Question():
     if (checkAuth()):
          return question.CreateNewQuestion(request)
     else:
          return 'Unauthorized', 401

#################Fin de la partie guidée
@app.route('/rebuild-db', methods=['POST'])
def rebuildDB():
     if (checkAuth()):
          return generateDb.create_database()
     else:
          return 'Unauthorized', 401

@app.route('/questions/<index>', methods=['GET'])
def getQuestionByID(index):
     return question.getQuestionByID(index)

@app.route('/questions', methods=['GET'])
def getQuestionByPosition():     
     #If key doesn't exist, return None
     position = request.args.get('position')
     if (position == None):
          return 'Position is missing', 400
     else:
          return question.getQuestionByPosition(position)
     
@app.route('/questions/<index>', methods=['PUT'])
def updateQuestion(index):
     if (checkAuth()):
          return question.updateQuestion(request, index)
     else:
          return 'Unauthorized', 401
@app.route('/questions/<index>', methods=['DELETE'])
def deleteQuestion(index):
     if (checkAuth()):
          return question.deleteQuestion(request, index)
     else:
          return 'Unauthorized', 401
     
@app.route('/questions/all', methods=['DELETE'])
def deleteAllQuestion():
     if (checkAuth()):
          return question.deleteAllQuestion()
     else:
          return 'Unauthorized', 401

@app.route('/participations', methods=['POST'])
def addParticipation():
	return participation.addParticipation(request)

@app.route('/participations/all', methods=['DELETE'])
def deleteAllParticipation():
     if (checkAuth()):
          return participation.deleteAllParticipation(request)
     else:
          return 'Unauthorized', 401

@app.route('/classement', methods=['GET'])
def getAllParticipations():
    return participation.getAllParticipations()

if __name__ == "__main__":
    app.run()

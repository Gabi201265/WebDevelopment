from flask import Flask, request
from flask_cors import CORS
import hashlib
from jwt_utils import build_token, decode_token
import question, participation

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
	x = 'world'
	return f"Hello, {x} !!"

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	return {"size": 0, "scores": []}, 200

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

@app.route('/questions', methods=['POST'])
def Question():
    return question.CreateNewQuestion(request)


#################Fin de la partie guidée
@app.route('/questions/<index>', methods=['GET'])
def getQuestion(index):
	return question.getQuestion(request, index)

@app.route('/questions/<index>', methods=['PUT'])
def updateQuestion(index):
	return question.updateQuestion(request, index)

@app.route('/questions/<index>', methods=['DELETE'])
def deleteQuestion(index):
	return question.deleteQuestion(request, index)

# @app.route('/participations', methods=['POST'])
# def addParticipation():
# 	return participation.addParticipation(request)

# @app.route('/participations', methods=['DELETE'])
# def deleteParticipation():
# 	return participation.deleteParticipation(request)

if __name__ == "__main__":
    app.run()

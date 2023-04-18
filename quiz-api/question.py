
import dbController as db
import classQuestion
import json
import random
#from asyncio.windows_events import NULL

def CreateNewQuestion(request):
    #Récupérer le token envoyé en paramètre
    token = request.headers.get('Authorization')
    #print(tokenDecode)
    #récupèrer un l'objet json envoyé dans le body de la requète
    objJson = request.get_json()
    if token:
        print("saveQuestion")
        print(getNumberOfQuestion())
        saveQuestion(request)
        print(deserialize_question(objJson))
        return {"ok": token , "id": objJson}, 200
    else:
        return 'Unauthorized', 401

def serialize_question(question):
    #La question est sérialisée en JSON à l'aide de la fonction json.dumps()
    return json.dumps({
        'id': question.id,
        'title': question.title,
        'position': question.position,
        'text': question.text,
        'image': question.image
    })

def deserialize_question(data):
    json_data = data
    return classQuestion.Question(
        #Pour éviter les None dans les ids
        id=json_data['id'] if 'id' in json_data else random.randint(1,100),
        position=json_data['position'],
        title=json_data['title'],
        text=json_data['text'],
        image=json_data['image'],
        responses=json_data['possibleAnswers']
    )

#Enregistre la question
def saveQuestion(request):
    #récupèrer un l'objet json envoyé dans le body de la requète
	objJson = request.get_json()
	try:
		question = deserialize_question(objJson)
		#Ajout d'une question
		if (question.position > (getNumberOfQuestion())-1):
			addQuestion(request, question)
		else:
			insertQuestion(request, question)
	except Exception as e: 
		return 'Unauthorized', 401

#Ajout d'une question
def addQuestion(request, question):
    print("addQuestion")
    title = str(question.title).replace("'","''")
    print(title)
    text = str(question.text).replace("'","''")
    print(text)
    print(question.id)
    print(question.position)
    print(question.image)
    cur = db.dBConnection()
    query = (
        f"INSERT INTO questions VALUES"
        f"({question.id},{question.position},'{title}','{text}','{question.image}')"
        )
    try:
        cur.execute("begin")
        cur.execute(query)
        cur.execute("commit")
    except Exception as e :
        print(e)
        cur.execute('rollback')
        return 'Unauthorized',401

    #reponses in DB
    #Ma variable pour savoir où placer la réponse
    # i = 1
    # for reponse in question.reponses :
    #     reponse['text'] = reponse['text'].replace("'","''")
    #     query = (
    #     f"INSERT INTO reponses (text, isCorrect, posQuestion, position) VALUES"
    #     f"('{reponse['text']}','{reponse['isCorrect']}', {question.position}, {i})"
    #     )
    #     try:
    #         cur.execute("begin")
    #         cur.execute(query)
    #         cur.execute("commit")
    #     except Exception as e :
    #         print(e)
    #         cur.execute('rollback')
    #         return '',401
    #     i= i+1
    #in case of exception, rollback the transaction
    #cur.execute('rollback')


def insertQuestion(request, question):
    print("insertQuestion")
    indexCurrQuestion = question.position
    totalCount = getNumberOfQuestion()

    try:
        #ajout d'une question vide
        createQuestion = classQuestion.Question(0, totalCount, "title", "text", "img",[])
        createQuestion.position += 1
        addQuestion(request, createQuestion)

        for i in range(totalCount+1, indexCurrQuestion, -1):
            #classQuestion.questionToJSON(classQuestion.addResponses(question))
            questionJSON = deserialize_question(question)
            createQuestion = classQuestion.Question(questionJSON['id'], questionJSON['position'], questionJSON['title'], questionJSON['text'], questionJSON['image'],questionJSON['possibleAnswers'])
            updateDB(createQuestion, i)
            
        updateDB(question, indexCurrQuestion)
        return 'Ok', 200
    except Exception as e:
        print(e)
        return 'Error', 404

def updateDB(question, index):
    cur = db.dbConnection()
    
    title = str(question.title).replace("'","''")
    text = str(question.texte).replace("'","''")
    query = (
    f"UPDATE questions "
    f"SET Title = '{title}',"
    f" Texte = '{text}',"
    f" Image = '{question.image}',"
    f" Position = '{index}',"
    f" ID = '{question.id}'"
    f"WHERE Position = "
    f"{index};"
    )
    try:
        cur.execute("begin")
        cur.execute(query)
        cur.execute("commit")
    except Exception as e:
        print(e)
        return 'Error', 404
    
    #update reponses
    # query = (
    #     f"DELETE FROM REPONSES "
    #     f"WHERE posQuestion = {index}"
    #     )
    # try:
    #     cur.execute("begin")
    #     cur.execute(query)
    #     cur.execute("commit")
    # except Exception as e :
    #     print(e)
    # i=1
    # for reponse in question.reponses:
    #     reponse['text'] = reponse['text'].replace("'","''")
    #     query = (
    #         f"INSERT INTO REPONSES (text, isCorrect, posQuestion, position) VALUES"
    #         f"('{reponse['text']}','{reponse['isCorrect']}', {index},{i})"
    #         )
    #     i = i+1
    #     try:
    #         cur.execute("begin")
    #         cur.execute(query)
    #         cur.execute("commit")
    #     except Exception as e :
    #         print(e)


def getNumberOfQuestion():
	try: 
		cur = db.dBConnection()
		cur.execute("begin")
		maQuery = cur.execute(f"SELECT count(*) FROM questions")
		nb = maQuery.fetchall()[0][0]
		cur.execute("commit")
		return nb
	except Exception as e:
		return 'Error', 404
        
        
        
        
        
# def addQuestion(request, question):
    

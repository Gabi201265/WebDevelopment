
import dbController as db
import classQuestion
import json
import random
from asyncio.windows_events import NULL

def CreateNewQuestion(request):
    #Récupérer le token envoyé en paramètre
    token = request.headers.get('Authorization')
    #print(tokenDecode)
    #récupèrer un l'objet json envoyé dans le body de la requète
    objJson = request.get_json()
    if token:
        print("saveQuestion")
        print("NbOfQuestions : " + str(getNumberOfQuestion()))
        saveQuestion(request)
        return {"ok": token , "id": objJson}, 200
    else:
        return 'Unauthorized', 401

def serialize_question(question):
    #LPour convertir la liste en question [(36, 1, 'Dummy Question', "Quelle est la couleur du cheval blanc d'Henry IV ?", 'falseb64imagecontent')]
    #ID
    id = (question[0][0])
    #position
    position = (question[0][1])
    #title
    title = (question[0][2])
    #texte
    text = (question[0][3])
    #reponses
    image = (question[0][4])
    
    return classQuestion.Question(id, position, title,text, image, NULL)

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
		if (question.position > (getNumberOfQuestion())):
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

#Permet d'update les questions !
#def updateQuestion(request, index):
    # objJson = request.get_json()
    # try:
    #     #ajout question vide
    #     index= int(index)
    #     createQuestion = deserialize_question(objJson)
    #     a = 0
    #     b = 0
    #     parcours = 0
    #     if ( index > createQuestion.position):
    #         b = createQuestion.position
    #         a = index
    #         parcours = -1
    #     else:
    #        a = index 
    #        b = createQuestion.position
    #        parcours = 1
    #     for i in range(a, b, parcours):
    #         questionJSON = json.loads(getQuestionsinfos(i+ parcours))
    #         question = classQuestion.Question(questionJSON['id'], questionJSON['position'], questionJSON['title'], questionJSON['text'], questionJSON['image'],questionJSON['possibleAnswers'])
    #         try:
    #             updateDB(question, i)
    #         except Exception as e:
    #             print(e)
    #             return '', 404
    #     updateDB(createQuestion, createQuestion.position)
    #     return '', 200
    # except Exception as e:
    #         print(e)
    #         return '', 404


#Insertion d'une question (ne fonctionne pas)
def insertQuestion(request, question):
    print("insertQuestion")
    indexCurrQuestion = question.position
    totalCount = getNumberOfQuestion()
    
    title = str(question.title).replace("'","''")
    text = str(question.text).replace("'","''")
    try:
        #ajout d'une question vide
        createQuestion = classQuestion.Question(0, totalCount+1, "title", "text", "img",[])
        addQuestion(request, createQuestion)
        
        lastQuestion = serialize_question(getQuestion(totalCount))
        
        for i in range(indexCurrQuestion+1, totalCount+1):
            print("i :" +str(i))
            #classQuestion.questionToJSON(classQuestion.addResponses(question))
            print("je passe par la bas")
            #On doit récupérer la question associé à sa position
            nextQuestion = serialize_question(getQuestion(i-1))
            print(str(nextQuestion))
            
            #On actualise en remplaçant la question par la notre
            print("je passe par ici")
            createQuestion = classQuestion.Question(nextQuestion.id, nextQuestion.position + 1, nextQuestion.title, nextQuestion.text, nextQuestion.image, nextQuestion.responses)
            print("je passe par la")
            #On update
            updateDB(createQuestion, i)
        
        #On update la question en question mtn que tout est décalé     
        updateDB(question, indexCurrQuestion)
        
        #On update la dernière question
        updateDB(lastQuestion, totalCount+1)
        return 'Ok', 200
    except Exception as e:
        print(e)
        return 'Error', 404

def updateDB(question, index):
    print("updateDB")
    cur = db.dBConnection()
    title = str(question.title).replace("'","''")
    text = str(question.text).replace("'","''")
    query = (
    f"UPDATE questions "
    f"SET title = '{title}',"
    f" text = '{text}',"
    f" image = '{question.image}',"
    f" position = '{index}',"
    f" id = '{question.id}'"
    f"WHERE position = {index}; "
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
        
def getQuestion(index):
    cur = db.dBConnection()
    cur.execute("begin")
    #serializing(req)
    maQuery = cur.execute(
        f"SELECT * FROM questions where position == {index};"
    )
    quest = maQuery.fetchall()
    cur.execute("commit")
    print("ok")
    return quest
    

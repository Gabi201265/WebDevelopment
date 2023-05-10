
import dbController as db
import classQuestion
import json
import random
from asyncio.windows_events import NULL

def GetQuizInfo():
    try:
        # Récupération de la taille
        cur = db.dBConnection()
        cur.execute("begin")
        query = cur.execute(f"SELECT COUNT(*) FROM questions")
        size = query.fetchall()[0][0]
        cur.execute("commit")
        
        # Récupération des scores de chaque joueur
        cur = db.dBConnection()
        cur.execute("begin")
        query = cur.execute(f"SELECT * FROM participations ORDER BY score DESC")
        scores = query.fetchall()
        cur.execute("commit")
        
        # On crée la liste à partir du fetchall que l'on a récupéré
        list_scores = []
        for score in scores :
            list_scores.append({'playerName': str(score[0]),'score': score[2]})
    
        return {"size": size, "scores": list_scores}, 200
    except Exception as e: 
        print(e)
        return '',401

def CreateNewQuestion(request):
    # Récupérer le token envoyé en paramètre
    token = request.headers.get('Authorization')
    # print(tokenDecode)
    # récupèrer un l'objet json envoyé dans le body de la requète
    objJson = request.get_json()
    if token:
        print("saveQuestion")
        print("NbOfQuestions : " + str(getNumberOfQuestion()))
        return saveQuestion(request)
    else:
        return 'Unauthorized', 401


def serialize_question(question):
    # Pour convertir la liste en question [(36, 1, 'Dummy Question', "Quelle est la couleur du cheval blanc d'Henry IV ?", 'falseb64imagecontent')]
    # ID
    id = (question[0][0])
    # position
    position = (question[0][1])
    # title
    title = (question[0][2])
    # texte
    text = (question[0][3])
    # reponses
    image = (question[0][4])

    return classQuestion.Question(id, position, title, text, image, None)

def deserialize_question(data):
    json_data = data
    return classQuestion.Question(
        # Pour éviter les None dans les ids
        None,
        position=json_data['position'],
        title=json_data['title'],
        text=json_data['text'],
        image=json_data['image'],
        responses=json_data['possibleAnswers']
    )

def retrieve_last_autoincremented_ID():
    try:
        cur = db.dBConnection()
        cur.execute("begin")
        query = cur.execute(f"SELECT seq FROM sqlite_sequence WHERE name=\"questions\"")
        last_id = query.fetchall()[0][0]
        cur.execute("commit")
        return last_id
    except Exception as e:
        print(e)
        cur.execute('rollback')
        return 'Unauthorized', 401
    
    
    
# Enregistre la question
def saveQuestion(request):
    # récupèrer un l'objet json envoyé dans le body de la requète
    objJson = request.get_json()
    question = deserialize_question(objJson)
    # Ajout d'une question
    # if (question.position > (getNumberOfQuestion())):
    if(addQuestion(request, question)):
        print(retrieve_last_autoincremented_ID())
        return {'id' : retrieve_last_autoincremented_ID() }, 200
    else:
        return 'Unauthorized', 401
    # else:
    #     if(insertQuestion(request, question)):
    #         return {'id' : retrieve_last_autoincremented_ID }, 200
    #     else:
    #         return 'Unauthorized', 401


# Ajout d'une question


def addQuestion(request, question):
    print("addQuestion")
    try:
        title = str(question.title).replace("'", "''")
        text = str(question.text).replace("'", "''")
        cur = db.dBConnection()
        query = (
            f"INSERT INTO questions (position, title, text, image) VALUES"
            f"({question.position},'{title}','{text}','{question.image}')"
        )
        try:
            cur.execute("begin")
            cur.execute(query)
            cur.execute("commit")
        except Exception as e:
            print(e)
            cur.execute('rollback')
            return 'Unauthorized', 401

        # Insertion des réponses dans la DB
        # Ma variable pour savoir où placer la réponse
        i = 1
        print("question.responses " + str(question.responses))
        for reponse in question.responses:
            print(str(reponse['text']))
            reponse['text'] = reponse['text'].replace("'", "''")
            query = (
                f"INSERT INTO reponses VALUES ({i}, {question.position}, '{reponse['text']}', '{reponse['isCorrect']}' )"
            )
            try:
                cur.execute("begin")
                cur.execute(query)
                cur.execute("commit")
            except Exception as e:
                cur.execute('rollback')
                return 'Unauthorized', 401
            i = i+1
        return True
    except Exception as e:
        return False
# Insertion d'une question (ne fonctionne pas)


def insertQuestion(request, question):
    print("insertQuestion")
    indexCurrQuestion = question.position
    totalCount = getNumberOfQuestion()
    print("indexCurrQuestion : " + str(indexCurrQuestion))
    try:
        # ajout d'une question vide
        createQuestion = classQuestion.Question(
            0, totalCount+1, "title", "text", "img", [])
        addQuestion(request, createQuestion)
        print("getQuestion(totalCount)[0] : " +
              str(getQuestion(totalCount)[0]))

        lastQuestion = serialize_question(getQuestion(totalCount)[0])

        for i in range(indexCurrQuestion+1, totalCount+1):
            # classQuestion.questionToJSON(classQuestion.addResponses(question))
            # On doit récupérer la question associé à sa position
            nextQuestion = serialize_question(getQuestion(i-1)[0])
            print(str(nextQuestion))

            # On actualise en remplaçant la question par la notre
            createQuestion = classQuestion.Question(
                nextQuestion.id, nextQuestion.position + 1, nextQuestion.title, nextQuestion.text, nextQuestion.image, nextQuestion.responses)
            print("je passe par la")
            # On update
            updateDB(createQuestion, i)

        # On update la question en question mtn que tout est décalé
        updateDB(question, indexCurrQuestion)

        # On update la dernière question
        updateDB(lastQuestion, totalCount+1)
        return True
    except Exception as e:
        print(e)
        return False

# GETbyID
def getQuestionByID(index):
    print("getQuestionByID")
    quest = NULL
    try:
        print("index " + str(index))
        cur = db.dBConnection()
        cur.execute("begin")
        query = cur.execute(
            f"SELECT * FROM questions where id == {index};"
        )
        #fetchall renvoit une liste donc il faut créer une question à partir de cette dernière
        quest = query.fetchall()
        cur.execute("commit")
        if not quest:
            return 'Error', 404
        
        myQuestion = classQuestion.Question(quest[0][0], quest[0][1], quest[0][2], quest[0][3], quest[0][4], NULL)
        print("Question : ok")

        # Partie réponses
        cur = db.dBConnection()
        cur.execute("begin")
        query = cur.execute(
            f"SELECT * FROM reponses where positionQuestion == {quest[0][1]};"
        )
        getReponses = query.fetchall()
        #print(getReponses)
        myQuestion = myQuestion.questionToJSON(getReponses)
        cur.execute("commit")
        print("Question et réponses : ok")
        return myQuestion, 200
    except Exception as e:
        return 'Error', 404


# GETbyPosition
def getQuestionByPosition(position):
    print("getQuestionByPosition")
    quest = NULL
    try:
        cur = db.dBConnection()
        cur.execute("begin")
        query = cur.execute(
            f"SELECT * FROM questions where position == {position};"
        )
        #fetchall renvoit une liste donc il faut créer une question à partir de cette dernière
        quest = query.fetchall()
        cur.execute("commit")
        if not quest:
            return 'Error', 404
        
        myQuestion = classQuestion.Question(quest[0][0], quest[0][1], quest[0][2], quest[0][3], quest[0][4], NULL)
        print("Question : ok")

        # Partie réponses
        cur = db.dBConnection()
        cur.execute("begin")
        query = cur.execute(
            f"SELECT * FROM reponses where positionQuestion == {quest[0][1]};"
        )
        getReponses = query.fetchall()
        print(getReponses)
        myQuestion = myQuestion.questionToJSON(getReponses)
        cur.execute("commit")
        print("Question et réponses : ok")
        return myQuestion, 200
    except Exception as e:
        return 'Error', 404
    
# UPDATE
def updateQuestion(request, index):
    print("UpdateQuestion")
    #On récupère l'ancienne question pour avoir l'ancienne position pour update les réponses associés
    oldQuestion = getQuestionByID(index)[0]
    oldQuestion = json.loads(oldQuestion)
    print("oldQuestion['position'] : " +str(oldQuestion['position']))
    oldPosition = oldQuestion['position']
    objJson = request.get_json()
    question = deserialize_question(objJson)
    try:
        title = str(question.title).replace("'", "''")
        text = str(question.text).replace("'", "''")
        cur = db.dBConnection()
        query = (
            f"UPDATE questions "
            f"SET title = '{title}',"
            f" text = '{text}',"
            f" image = '{question.image}',"
            f" position = '{question.position}',"
            f" id = '{index}'"
            f"WHERE id = {index}; "
        )
        try:
            cur.execute("begin")
            cur.execute(query)
            cur.execute("commit")
        except Exception as e:
            print(e)
            cur.execute('rollback')
            return 'Unauthorized', 401

        # Actualisation des réponses dans la DB
        i = 1
        print("question.responses " + str(question.responses))
        for reponse in question.responses:
            print(str(reponse['text']))
            reponse['text'] = reponse['text'].replace("'", "''")
            query = (
                f"UPDATE reponses "
                f"SET position = '{i}',"
                f" positionQuestion = '{question.position}',"
                f" text = '{reponse['text']}',"
                f" isCorrect = '{reponse['isCorrect']}'"
                f"WHERE positionQuestion = {oldPosition}; "
            )
            try:
                cur.execute("begin")
                cur.execute(query)
                cur.execute("commit")
            except Exception as e:
                cur.execute('rollback')
                return 'Unauthorized', 401
            i = i+1
        return '', 204
    except Exception as e:
        return 'Error', 404
# DELETE
def deleteQuestion(request, index):
    # Récupérer le token envoyé en paramètre
    token = request.headers.get('Authorization')
    nbQuestion = getNumberOfQuestion()
    if (token):
        try:
            deleteQuestionInDB(request, index)

            return 'OK', 204

        except Exception as e:
            return 'Error', 404
    else:
        return 'Unauthorized', 401


def deleteAllQuestion(request):
    # Récupérer le token envoyé en paramètre
    token = request.headers.get('Authorization')
    nbQuestion = getNumberOfQuestion()
    if (token):
        try:
            for i in range(1, nbQuestion+1):
                deleteQuestionInDB(request, i)
            return '', 204
        except Exception as e:
            return 'Error', 404
    else:
        return 'Unauthorized', 401


# Permet d'update la db
def updateDB(question, pos):
    print("updateDB")
    cur = db.dBConnection()
    title = str(question.title).replace("'", "''")
    text = str(question.text).replace("'", "''")
    query = (
        f"UPDATE questions "
        f"SET title = '{title}',"
        f" text = '{text}',"
        f" image = '{question.image}',"
        f" position = '{pos}',"
        f" id = '{question.id}'"
        f"WHERE position = {pos}; "
    )
    try:
        cur.execute("begin")
        cur.execute(query)
        cur.execute("commit")
    except Exception as e:
        print(e)
        return 'Error', 404


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


def deleteQuestionInDB(request, index):
    cur = db.dBConnection()
    maQuery = (
        f"DELETE FROM questions WHERE id = {index}")
    try:
        cur.execute("begin")
        cur.execute(maQuery)
        cur.execute("commit")
    except Exception as e:
        return '', 401

    # delete reponses associées
    maQuery = (
        f"DELETE FROM reponses WHERE positionQuestion = {index}"
    )
    try:
        cur.execute("begin")
        cur.execute(maQuery)
        cur.execute("commit")
    except Exception as e:
        cur.execute('rollback')
        return '', 401

def rebuildDB():
    queryParticipation = ("DELETE FROM PARTICIPATIONS;")
    queryQuestions=("DELETE FROM QUESTIONS;")
    querySQL=("DELETE FROM SQLITE_SEQUENCE;")
    queryResponses=("DELETE FROM REPONSES;")
    
    try:
        cur = db.dBConnection()
        cur.execute("begin")
        cur.execute(queryParticipation)
        cur.execute(queryQuestions)
        cur.execute(querySQL)
        cur.execute(queryResponses)
        cur.execute("commit")
        return 'Ok', 200
    except Exception as e:
        print(e)
        return 'Unauthorized', 401

def getRightAnswer(index):
    print("getRightAnswer")
    try:
        cur = db.dBConnection()
        cur.execute("begin")
        result = cur.execute(
            f"SELECT position FROM reponses WHERE isCorrect = 'True' AND positionQuestion = {index};"
            )
        score = result.fetchall()
        cur.execute("commit")
        print("Score : " + str(score))
        return score[0][0]
    except Exception as e:
        print(e)
        return '', 401
# def getRightAnswer(index):
#     print("getRightAnswer")
#     try:
#         cur = db.dBConnection()
#         cur.execute("begin")
#         result = cur.execute("SELECT position FROM reponses WHERE isCorrect = \"True\" AND positionQuestion = ?",(index))
#         score = result.fetchall()
#         cur.execute("commit")
#         print("Score : " + str(score))
#         return score
#     except Exception as e:
#         print(e)
#         return '', 401
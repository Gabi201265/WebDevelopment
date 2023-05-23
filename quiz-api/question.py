
import dbController as db
import classQuestion
import json
import random


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
            list_scores.append({'playerName': str(score[1]),'score': score[2]})
    
        return {"size": size, "scores": list_scores}, 200
    except Exception as e: 
        print(e)
        return '',401

def CreateNewQuestion(request):
    print("saveQuestion")
    print("NbOfQuestions : " + str(getNumberOfQuestion()))
    return saveQuestion(request)



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
    print("Qestion.position : " + str(question.position))
    if ( int(question.position) > (getNumberOfQuestion())):
        if(addQuestion(question)):
            print(retrieve_last_autoincremented_ID())
            return {'id' : retrieve_last_autoincremented_ID() }, 200
        else:
            return 'Unauthorized', 401
    else:
        if(insertQuestion(question)):
            return {'id' : retrieve_last_autoincremented_ID() }, 200
        else:
            return 'Unauthorized', 401


# Ajout d'une question
def addQuestion(question):
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
    
    
    
# Insertion d'une question 
def insertQuestion(question):
    print("insertQuestion")
    # Décaler les questions existantes à partir de la position spécifiée
    try:
        cur = db.dBConnection()
        # Décale toutes les questions
        queryQuestion = (
            f"UPDATE questions "
            f"SET position = position + 1 "
            f"WHERE position >= {question.position}; "
        )
        # Décale toutes les réponses associées 
        queryReponse = (
            f"UPDATE reponses "
            f"SET positionQuestion = positionQuestion + 1 "
            f"WHERE positionQuestion >= {question.position}; "
        )
        # Insère la nouvelle question
        title = str(question.title).replace("'", "''")
        text = str(question.text).replace("'", "''")
        queryNewQuestion= (
            f"INSERT INTO questions (position, title, text, image) VALUES"
            f"({question.position},'{title}','{text}','{question.image}');"
        )
        cur.execute("begin")
        cur.execute(queryQuestion)
        cur.execute(queryReponse)
        cur.execute(queryNewQuestion)
        cur.execute("commit")
        
        # Insertion des réponses dans la DB
        i = 1
        for reponse in question.responses:
            reponse['text'] = reponse['text'].replace("'", "''")
            query = (
                f"INSERT INTO reponses VALUES ({i}, {question.position}, '{reponse['text']}', '{reponse['isCorrect']}' )"
            )
            cur.execute("begin")
            cur.execute(query)
            cur.execute("commit")
            i = i+1
        return True
    
    except Exception as e:
        print(e)
        return False

# GETbyID
def getQuestionByID(index):
    print("getQuestionByID")
    quest = None
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
        
        myQuestion = classQuestion.Question(quest[0][0], quest[0][1], quest[0][2], quest[0][3], quest[0][4], None)
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
    quest = None
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
        
        myQuestion = classQuestion.Question(quest[0][0], quest[0][1], quest[0][2], quest[0][3], quest[0][4], None)
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
    objJson = request.get_json()
    question = deserialize_question(objJson)
    try:
        title = str(question.title).replace("'", "''")
        text = str(question.text).replace("'", "''")
        cur = db.dBConnection()
        
        # On vérifie que la question existe bien
        cur.execute("begin")
        query = cur.execute(
            f"SELECT * FROM questions where id == {index};"
        )
        quest = query.fetchall()
        cur.execute("commit")
        if not quest:
            return 'Error, question doesnt exist', 404
        
        # Supprime, décale tout et insère ! 
        # Mathématiquement : 
        # +1 des positions dans l'intervalle >=dest et <source QUAND positionSource > positionDestination
        # -1 des positions dans l'intervalle >source et <=dest QUAND positionSource < positionDestination
        
        
        positionDest = question.position
        positionSource = quest[0][1]
        
        
        if positionDest==positionSource:
            query = (
                f"UPDATE questions "
                f"SET title = '{title}',"
                f" text = '{text}',"
                f" image = '{question.image}',"
                f" position = '{question.position}',"
                f" id = '{index}'"
                f"WHERE id = {index}; "
            )
            cur.execute("begin")
            cur.execute(query)
            cur.execute("commit")
            
            # Insertion des nouvelles réponses dans la DB
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
                    f" isCorrect = '{reponse['isCorrect']}' "
                    f"WHERE positionQuestion = {question.position} AND position = {i};"
                )
                cur.execute("begin")
                cur.execute(query)
                cur.execute("commit")
                i = i+1
            return '', 204
        else :
            # SUPPRESSION
            # delete reponses associées à la question marche pas il faut delete les anciennes reponses, donc il faut récuperer l'ancienne position question
            query = (
                f"DELETE FROM reponses WHERE positionQuestion = {positionSource};"
            )
            cur.execute("begin")
            cur.execute(query)
            cur.execute("commit")
            
            # delete de la question
            query = (
                f"DELETE FROM questions WHERE id = {index};")
            cur.execute("begin")
            cur.execute(query)
            cur.execute("commit")
            
            # REORDONANCEMENT 
            if positionDest < positionSource :
                # Décale toutes les questions
                queryQuestion = (
                    f"UPDATE questions "
                    f"SET position = position + 1 "
                    f"WHERE position >= {positionDest} AND position < {positionSource};"
                )
                # Décale toutes les réponses associées 
                queryReponse = (
                    f"UPDATE reponses "
                    f"SET positionQuestion = positionQuestion + 1 "
                    f"WHERE positionQuestion >= {positionDest} AND positionQuestion < {positionSource};"
                )
            else :
                # Décale toutes les questions
                queryQuestion = (
                    f"UPDATE questions "
                    f"SET position = position - 1 "
                    f"WHERE position <= {positionDest} AND position > {positionSource};"
                )
                # Décale toutes les réponses associées 
                queryReponse = (
                    f"UPDATE reponses "
                    f"SET positionQuestion = positionQuestion - 1 "
                    f"WHERE positionQuestion <= {positionDest} AND positionQuestion > {positionSource};"
                )
            cur.execute("begin")
            cur.execute(queryQuestion)
            cur.execute(queryReponse)
            cur.execute("commit")
            
            
            # INSERTION
            # Insère la nouvelle question
            title = str(question.title).replace("'", "''")
            text = str(question.text).replace("'", "''")
            query= (
                f"INSERT INTO questions (id, position, title, text, image) VALUES"
                f"({index}, {question.position},'{title}','{text}','{question.image}');"
            )
            cur.execute("begin")
            cur.execute(query)
            cur.execute("commit")
            
            # Insertion des nouvelles réponses dans la DB
            i = 1
            print("question.responses " + str(question.responses))
            for reponse in question.responses:
                print("i : " + (str(i)))
                print(str(reponse['text']))
                reponse['text'] = reponse['text'].replace("'", "''")
                query = (
                    f"INSERT INTO reponses VALUES ({i}, {question.position}, '{reponse['text']}', '{reponse['isCorrect']}' )"
                )
                cur.execute("begin")
                cur.execute(query)
                cur.execute("commit")
                i = i+1
            return '', 204
    except Exception as e:
        return 'Error', 404
    
    
# DELETE
def deleteQuestion(request, index):
    cur = db.dBConnection()
    # verifie si l'index est correct 
    cur.execute("begin")
    query = cur.execute(
        f"SELECT * FROM questions where id == {index};"
    )
    quest = query.fetchall()
    cur.execute("commit")
    if not quest:
        return 'Error', 404
    
    # delete reponses associées à la question
    query = (
        f"DELETE FROM reponses WHERE positionQuestion = (SELECT position FROM questions WHERE id = {index})"
    )
    cur.execute("begin")
    cur.execute(query)
    cur.execute("commit")
    
    # delete de la question
    query = (
        f"DELETE FROM questions WHERE id = {index}")
    cur.execute("begin")
    cur.execute(query)
    cur.execute("commit")
    
    # réordonnancement de la BDD
    # Décale toutes les questions
    queryQuestion = (
        f"UPDATE questions "
        f"SET position = position - 1 "
        f"WHERE position > {quest[0][1]}; "
    )
    # Décale toutes les réponses associées 
    queryReponse = (
        f"UPDATE reponses "
        f"SET positionQuestion = positionQuestion - 1 "
        f"WHERE positionQuestion > {quest[0][1]}; "
    )
    cur.execute("begin")
    cur.execute(queryQuestion)
    cur.execute(queryReponse)
    cur.execute("commit")
    
    return 'Ok', 204


def deleteAllQuestion():
    try:
        cur = db.dBConnection()
        queryQuestion=("DELETE FROM QUESTIONS;")
        queryReponse=("DELETE FROM REPONSES;")
        queryParticipations=("DELETE FROM PARTICIPATIONS;")
        querySQL=("DELETE FROM SQLITE_SEQUENCE;")
        cur.execute("begin")
        cur.execute(queryQuestion)
        cur.execute(queryReponse)
        cur.execute(queryParticipations)
        cur.execute(querySQL)
        cur.execute("commit")
        return '', 204
    except Exception as e:
        return 'Error', 404

def getNumberOfQuestion():
    try:
        cur = db.dBConnection()
        cur.execute("begin")
        query = cur.execute(f"SELECT count(*) FROM questions")
        nb = query.fetchall()[0][0]
        cur.execute("commit")
        return nb
    except Exception as e:
        return 'Error', 404
    
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
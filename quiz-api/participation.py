import dbController as db
import random
import json
import question as quest
from asyncio.windows_events import NULL

def addParticipation(request):
     participationJSON = request.get_json()
     try:
          playerName = participationJSON["playerName"]
          score = getScore(participationJSON["answers"])
          print("Score : " + str(score))
          cur = db.dBConnection()
          query = (
            f"INSERT INTO participations (playerName, score) VALUES"
            f"('{playerName}',{score})"
        )
          if (score != -1):
               cur.execute("begin")
               cur.execute(query)
               cur.execute("commit")
               print("dedans")
               return {"playerName": playerName, "score": score}, 200
          else:
               return 'Bad Request', 400
     except Exception as e:
          print(e)
          return 'Unauthorized', 401

def deleteAllParticipation(request):
     query = ("DELETE FROM PARTICIPATIONS;")
     try:
          cur = db.dBConnection()
          cur.execute("begin")
          query = cur.execute(query)
          cur.execute("commit")
          return '', 204
     except Exception as e:
          print(e)
          return 'Unauthorized', 401

def getScore(data):
     score = 0
     print("calculate score")
     print(data)
     try:
          totalCount = quest.getNumberOfQuestion()
          print("totalCount : " + str(totalCount))
          if (len(data) != (totalCount)):
               return -1
          #update here
          else:
               for i in range (1,totalCount+1):
                    print("Data[i] : " + str(data[i-1]))
                    if (data[i-1] == int(quest.getRightAnswer(i))):
                         score += 1
          return score
     except Exception as e:
          print(e)
import sqlite3

def create_database():
    try:
        # Création d'une connexion à la base de données (le fichier sera créé s'il n'existe pas)
        conn = sqlite3.connect('quiz.db')
        cursor = conn.cursor()

        # Suppression des tables existantes si elles existent déjà
        cursor.execute('DROP TABLE IF EXISTS questions')
        cursor.execute('DROP TABLE IF EXISTS reponses')
        cursor.execute('DROP TABLE IF EXISTS participations')
        # Création de la table questions
        cursor.execute('''CREATE TABLE "questions" (
                            "id"	INTEGER NOT NULL,
                            "position"	INTEGER,
                            "title"	TEXT,
                            "text"	TEXT,
                            "image"	TEXT,
                            PRIMARY KEY("id" AUTOINCREMENT)
                        )''')

        # Création de la table participations
        cursor.execute('''CREATE TABLE "participations" (
                            "id"	INTEGER NOT NULL,
                            "playerName"	TEXT,
                            "score"	INTEGER,
                            PRIMARY KEY("id" AUTOINCREMENT)
                        )''')

        # Création de la table reponses
        cursor.execute('''CREATE TABLE "reponses" (
                            "position"	INTEGER,
                            "positionQuestion"	INTEGER,
                            "text"	TEXT,
                            "isCorrect"	INTEGER
                        )''')
        
        # Commit des modifications et fermeture de la connexion
        conn.commit()
        return 'Ok', 200
    except Exception as e:
        print(e)
        return 'Error', 404
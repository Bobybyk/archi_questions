import DB
import random
import threading
import time
import re
import requests

def send_question(question, reponse, image):
    img_path = 'img/' + image
    if image != "NULL":
        file = {'file': ('image', open(img_path, 'rb'), 'image/png')}
    else:
        file = "null"
    requests.post("http://localhost:3000/api/cours/architecture/questionEvent", {"question": question, "reponse": reponse, "image": file})

def question_manager():
    while True:
        random_question = random.choice(DB.DataBase.BASE)
        # Afficher la question
        print("Question : " + random_question.question + "\nRéponse : " + random_question.reponse + "\nImage : " + random_question.imgQuestion)
        print("=" * 30)  # Ajoute une ligne de séparation

        send_question(random_question.question, random_question.reponse, random_question.imgQuestion)

        # Attente avant de tirer la question suivante
        time.sleep(60 * 60 * 2)  # Attendre 2 heures entre chaque question

def display_database_content():
    for question in DB.DataBase.BASE:
        print(question.toString())
        print("=" * 30)  # Ajoute une ligne de séparation entre chaque question

def main():
    # ----- Init database
    parser = DB.Parser()
    print("Nombre de questions dans la base de données : " + str(len(DB.DataBase.BASE)))

    # ----- Afficher le contenu de la base de données
    #display_database_content()

    # ----- Tirer une question aléatoire toutes les 2 heures
    # ----- Créer un thread pour exécuter daily_question
    question_thread = threading.Thread(target=question_manager)

    # ----- Démarrer le thread
    question_thread.start()

if __name__ == "__main__":
    main()

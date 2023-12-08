import DB
import random
import threading
import time
import re
import requests

def send_question(question, reponse, image):
    img_path = 'img/' + image if image != "NULL" else None

    files = None
    if img_path:
        return
        files = {'image': open(img_path, 'rb')}
    data = {"question": question, "reponse": reponse}

    requests.post("http://localhost:3000/api/cours/architecture/questionEvent", data=data)

def question_manager():
    while True:
        random_question = random.choice(DB.DataBase.BASE)

        print("Question : " + random_question.question + "\nRéponse : " + random_question.reponse + "\nImage : " + random_question.imgQuestion)
        print("=" * 30)

        send_question(random_question.question, random_question.reponse, random_question.imgQuestion)
        time.sleep(60 * 60)

def display_database_content():
    for question in DB.DataBase.BASE:
        print(question.toString())
        print("=" * 30)

def main():

    parser = DB.Parser()
    print("Nombre de questions dans la base de données : " + str(len(DB.DataBase.BASE)))

    question_thread = threading.Thread(target=question_manager)

    question_thread.start()

if __name__ == "__main__":
    main()

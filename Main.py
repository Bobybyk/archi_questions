import DB
import random
import threading
import time
import requests

def send_question(question, reponse, file):
    print(file)
    if file == "NULL":
        response = requests.post("http://localhost:3000/api/cours/architecture/questionEvent", data = {"question": question, "reponse": reponse})
    else:
        with open("sys/img/"+file, "rb") as file:
            files = {'image': file}
            response = requests.post("http://localhost:3000/api/cours/architecture/questionEvent", files=files, data = {"question": question, "reponse": reponse})

def question_manager():
    while True:

        random_question = random.choice(DB.DataBase.BASE)

        print("Question : " + random_question.question + "\nRéponse : " + random_question.reponse)
        print("=" * 30)

        send_question(random_question.question, random_question.reponse, random_question.imgQuestion)

        time.sleep(60 * 10)


def display_database_content():
    for question in DB.DataBase.BASE:
        print(question.toString())
        print("=" * 30)


def main():
    DB.Parser()

    question_thread = threading.Thread(target=question_manager)

    question_thread.start()

if __name__ == "__main__":
    main()

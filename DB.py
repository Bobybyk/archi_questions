# -*- coding: utf-8 -*-

import os

'''
QUESTION
'''
class Question:
    def __init__(self, ID, question, imgQuestion, reponse):
        self.ID = ID
        self.question = question
        self.imgQuestion = imgQuestion
        self.reponse = reponse

    def toString(self):
        return "*SQ*" + self.question + "*EQ**SI*" + self.imgQuestion + "*EI*" + "*SR*" + self.reponse + "*ER*"
        
'''
PARSER
'''
class Parser:
    QRPATH = os.path.join("Data", "QR.txt") #"QR.txt"
    
    def __init__(self):
        # Init base de données de questions [q, r, imgQ, imgR]
        try:
            fichier = open(Parser.QRPATH, "r", encoding='utf-8')
            lines = fichier.readlines()
            
            Count = 0
            for line in lines:
                line = line.replace('\n', "")
                if len(line) > 6:
                    try:
                        content = line.split(sep=",")
                        question = Question(Count, content[0], content[2], content[1])
                        DataBase.BASE.append(question)
                        Count += 1
                    except:
                        continue
                
            fichier.close()
        except:
            print("Error during QR.txt reading")


'''
DATABASE (automatiquement remplie quand un Parser est créé)
'''
class DataBase:
    BASE = []
        
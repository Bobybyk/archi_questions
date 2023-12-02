import DB

def display_database_content():
    for question in DB.DataBase.BASE:
        print(question.toString())
        print("=" * 30)  # Ajoute une ligne de séparation entre chaque question

def main():
    # ----- Init database
    parser = DB.Parser()
    print("Nombre de questions dans la base de données : " + str(len(DB.DataBase.BASE)))

    # ----- Afficher le contenu de la base de données
    display_database_content()

if __name__ == "__main__":
    main()

import json
import os

schedule = []

# Charger les données depuis data.json
def load_data():
    global schedule
    if os.path.exists("data.json"):
        with open("data.json", "r") as file:
            schedule = json.load(file)
    else:
        schedule = []

# Sauvegarder les données
def save_data():
    with open("data.json", "w") as file:
        json.dump(schedule, file, indent=4)

# Ajouter un cours
def add_course():
    subject = input("Matière : ")
    day = input("Jour : ")
    start = input("Heure début : ")
    end = input("Heure fin : ")
    room = input("Salle : ")

    course = {
        "subject": subject,
        "day": day,
        "start": start,
        "end": end,
        "room": room
    }

    schedule.append(course)
    save_data()
    print("Cours ajouté avec succès !")

# Afficher emploi du temps
def show_schedule():
    if not schedule:
        print("Aucun cours enregistré.")
        return

    for i, course in enumerate(schedule, 1):
        print(f"{i}. {course['day']} | {course['start']}-{course['end']} | {course['subject']} | Salle {course['room']}")

# Supprimer un cours
def delete_course():
    show_schedule()
    try:
        index = int(input("Numéro du cours à supprimer : ")) - 1
        if 0 <= index < len(schedule):
            schedule.pop(index)
            save_data()
            print("Cours supprimé.")
        else:
            print("Numéro invalide.")
    except ValueError:
        print("Entrée invalide.")

# Menu principal
def menu():
    while True:
        print("\n===== EMPLOI DU TEMPS =====")
        print("1. Ajouter un cours")
        print("2. Afficher emploi du temps")
        print("3. Supprimer un cours")
        print("4. Quitter")

        choice = input("Choix : ")

        if choice == "1":
            add_course()
        elif choice == "2":
            show_schedule()
        elif choice == "3":
            delete_course()
        elif choice == "4":
            print("Au revoir !")
            break
        else:
            print("Choix invalide.")

# Lancer programme
load_data()
menu()
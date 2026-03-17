import json
import os
from datetime import datetime
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
def has_conflict(day, start, end, ignore_index=None):

    start_time = datetime.strptime(start, "%H:%M")
    end_time = datetime.strptime(end, "%H:%M")

    for i, course in enumerate(schedule):

        # Ignorer le cours qu'on modifie
        if i == ignore_index:
            continue

        if day.lower() == course["day"].lower():

            course_start = datetime.strptime(course["start"], "%H:%M")
            course_end = datetime.strptime(course["end"], "%H:%M")

            # Vérifier chevauchement
            if not (end_time <= course_start or start_time >= course_end):
                return True

    return False

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
    if has_conflict(day, start, end):
        print("Conflit d'horaire détecté. Cours non ajouté.")
        return
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
        if index >= 0 and index < len(schedule):
            schedule.pop(index)
            save_data()
            print("Cours supprimé.")
        else:
            print("Numéro invalide.")
    except ValueError:
        print("Entrée invalide.")

# Rechercher les cours par jour #
def searchCoursesByDay():
    day = input("Entrez le jour pour rechercher les cours : ")
    found = False
    for course in schedule:
        if course['day'].lower() == day.lower():
            print(f"{course['day']} | {course['start']}-{course['end']} | {course['subject']} | Salle {course['room']}")
            found = True
    if not found :
        print("Aucun cours trouvé pour ce jour.")

# modifier un cours
def modify_course():
    show_schedule()
    try:
        index = int(input("Numéro de cours à modifier : ")) - 1
        if index>= 0 and index < len(schedule):
            old_course = schedule[index]
            subject = input(f"entrer la nouvelle matière (actuelle : {old_course['subject']}): ")
            day = input(f"entrer le nouveau jour (actuel : {old_course['day']}): ")
            start = input(f"entrer la nouvelle heure de début (actuelle : {old_course['start']}): ")
            end = input(f"entrer la nouvelle heure de fin (actuelle : {old_course['end']}): ")
            room = input(f"entrer la nouvelle salle (actuelle : {old_course['room']}): ")
            new_course = {
                "subject": subject if subject else old_course['subject'],
                "day": day if day else old_course['day'],
                "start": start if start else old_course['start'],
                "end": end if end else old_course['end'],
                "room": room if room else old_course['room']
            }
            if has_conflict(new_course['day'], new_course['start'], new_course['end'], index):
                print("Conflit d'horaire détecté. Cours non modifié.")
                return
            schedule[index] = new_course
            save_data()
            print("Cours modifié avec succès !")
        else:
            print("Numéro invalide.")
    except ValueError:
        print("Entrée invalide.")
        
# Menu principal
def menu():
    while True:
        print("\n" + "="*40)
        print("        EMPLOI DU TEMPS")
        print("="*40)

        print(" 1) Ajouter un cours")
        print(" 2) Afficher l'emploi du temps")
        print(" 3) Supprimer un cours")
        print(" 4) Rechercher par jour")
        print(" 5) Modifier un cours")
        print(" 0) Quitter")

        print("-"*40)

        choice = input("Entrez votre choix : ")

        if choice == "1":
            add_course()
        elif choice == "2":
            show_schedule()
        elif choice == "3":
            delete_course()
        elif choice == "4":
            searchCoursesByDay()
        elif choice == "5":
            modify_course()
        elif choice == "0":
            print("Au revoir !")
            break
        else:
            print("❌ Choix invalide.")
# Lancer programme
load_data()
menu()

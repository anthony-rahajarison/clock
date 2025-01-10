import time
import datetime
import winsound
import keyboard

def regler_heure():  # Régler l'heure
    h = int(input("Quelle heure est-il (hh) ? "))
    m = int(input("Quelle minute est-il (mm) ? "))
    s = int(input("Quelle seconde est-il (ss) ? "))
    return datetime.datetime(2000, 1, 1, h, m, s)

def demande_format():  # Sélectionner le format 12/12 ou 24/24
    rep = input("Quel format voulez-vous ? (1 ou 2): \n 1. Format 24/24 \n 2. Format 12/12 \n ")
    if rep == "1":
        return True
    elif rep == "2":
        return False
    else:
        print("Réessayez.")
        return demande_format()

def regler_alarme():  # Réglage de l'alarme
    print("Paramètres de l'alarme : ")
    hA = int(input("Saisie de l'alarme (hh): "))
    mA = int(input("Saisie de l'alarme (mm): "))
    sA = int(input("Saisie de l'alarme (ss): "))
    return (hA, mA, sA)

def verifier_alarme(heure, alarme):  # Vérifie si l'heure actuelle correspond à l'heure de l'alarme.
    if alarme == (heure.hour, heure.minute, heure.second):  
        print("Alarme ! Il est l'heure !")
        for i in range(5):
            winsound.Beep(1000, 1000)  # Émet un bip sonore à 1000 Hz pendant 1 seconde

def controle_clavier(heure, alarme):  
    if keyboard.is_pressed("espace"):  
        print("Programme arrêté.")
        exit()
    if keyboard.is_pressed("p"):  # Met le programme en pause
        print("Horloge en pause, appuyez sur P pour reprendre", end="\r")
        keyboard.read_key("p")
        print(" " * 50, end="\r")  # Efface le message
    if keyboard.is_pressed("a"):  
        print("\nOuverture des paramètres de l'alarme...")
        alarme = regler_alarme()
        print("Nouvelle alarme définie :", alarme)
    return alarme  

#####################################
# Programme principal
heure = regler_heure()  
alarme = None  
format_24 = demande_format()  

# Boucle principale : affichage de l'heure
while True:
    if format_24:
        print(heure.strftime("%H:%M:%S"), end="\r")  # Affiche l'heure en format 24h
    else:
        print(heure.strftime("%I:%M:%S %p"), end="\r")  # Affiche l'heure en format 12h

    verifier_alarme(heure, alarme)  
    alarme = controle_clavier(heure, alarme)  # Gère les entrées clavier, met à jour l'alarme si nécessaire
    heure += datetime.timedelta(seconds=1)  # Incrémente l'heure
    time.sleep(1)

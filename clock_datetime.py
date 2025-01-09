import time
import datetime
import winsound
import keyboard
from datetime import timedelta

def regler_heure(h, m, s) : #Régler l'heure
    global heure
    heure = datetime.datetime(2000, 1, 1, h, m, s)

def demande_format() : #Séléctionner le format 12/12 ou 24/24
    rep = input("Format 24h ? (O/N): ")
    if (rep == "O" or rep == "o"):
        return True
    elif (rep == "N" or rep == "n"):
        return False
    else :
        print("Réessayer")
        demande_format()

def regler_alarme(h, m, s) :
    global alarme
    alarme = (h, m, s)

def verifier_alarme() : #Vérifie si l'heure actuelle correspond à l'heure de l'alarme.
    if alarme == (heure.hour, heure.minute, heure.second) :
        print("Alarme ! Il est l'heure !")
        for i in range(5):
            winsound.Beep(1000, 1000)  # Émet un bip sonore à 1000 Hz pendant 1 seconde

def controle_claver() :
    if keyboard.is_pressed("espace") : # Arrete le programme si espace maintenu
        print("Programme arrété.")
        exit()
    if keyboard.is_pressed("p") :
        print("Horloge en pause, P pour remmettre en marche", end="\r")
        time.sleep(1)
        keyboard.read_key("p")
        print(" " * 50, end="\r") #Efface le message


#####################################
regler_heure(18, 59, 55)
regler_alarme(19, 0, 0)


#Format 24/24
if demande_format() == True : 
    while True :
        print(heure.strftime("%H:%M:%S"), end="\r")  # Affiche l'heure
        verifier_alarme()
        heure += datetime.timedelta(seconds=1)
        time.sleep(1)
        controle_claver()
#Format 12/12
else :
    while True :
        print(heure.strftime("%I:%M:%S %p"), end="\r") # Affiche l'heure
        verifier_alarme()
        heure += datetime.timedelta(seconds=1)
        time.sleep(1)
        controle_claver()
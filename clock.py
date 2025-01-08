import time
import winsound

def afficher_heure(heure, minute, seconde): #Affiche l'heure sous le format hh:mm:ss
    print(f"{heure:02}:{minute:02}:{seconde:02}", end="\r")


def regler_alarme(heure_alarme): #Règle l'alarme et affiche un message lorsque l'heure actuelle correspond à l'alarme.
    global alarme
    alarme = heure_alarme

def verifier_alarme(): #Vérifie si l'heure actuelle correspond à l'heure de l'alarme.
    if alarme == (heure, minute, seconde) :
        print( "Alarme ! Il est l'heure !")
        for i in range(5):
            winsound.Beep(1000, 1000)  # Émet un bip sonore à 1000 Hz pendant 1 seconde

# Variables globales pour l'heure et l'alarme
heure, minute, seconde = 12, 55, 0
regler_alarme((12, 55, 5))  # Régle l'alarme

# Programme principal

while True:
    afficher_heure(heure, minute, seconde)
    verifier_alarme()
    seconde = seconde + 1
    time.sleep(1)
    if seconde == 60:
        minute = minute + 1
        seconde = 0
    if minute == 60:
        heure = heure + 1
        minute = 0
    if heure == 60:
        heure = 0


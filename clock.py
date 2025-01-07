import time
import winsound

def afficher_heure(heures, minutes, secondes):
    """Affiche l'heure sous le format hh:mm:ss."""
    print(f"{heures:02}:{minutes:02}:{secondes:02}", end="\r")

def regler_heure(nouvelle_heure):
    """Met à jour l'heure courante à partir d'un tuple (heures, minutes, secondes)."""
    global heures, minutes, secondes
    heures, minutes, secondes = nouvelle_heure

def regler_alarme(heure_alarme):
    """Règle l'alarme et affiche un message lorsque l'heure actuelle correspond à l'alarme."""
    global alarme
    alarme = heure_alarme

def verifier_alarme():
    """Vérifie si l'heure actuelle correspond à l'heure de l'alarme."""
    if alarme == (heures, minutes, secondes) :
        print( "Alarme ! Il est l'heure !")
        for i in range(5):
            winsound.Beep(1000, 1000)  # Émet un bip sonore à 1000 Hz pendant 1 seconde

# Variables globales pour l'heure et l'alarme
heures, minutes, secondes = 12, 55, 0
regler_alarme((12, 55, 5))  # Régle l'alarme

# Programme principal

while True:
    afficher_heure(heures, minutes, secondes)
    verifier_alarme()

        # Incrémenter l'heure
    secondes += 1
    if secondes == 60:
        secondes = 0
        minutes += 1
    if minutes == 60:
        minutes = 0
        heures += 1
    if heures == 24:
        heures = 0
    time.sleep(1)


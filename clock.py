import time
heure = 0
minute = 0
seconde = 0
def afficher_heure():
    print(f"{heure:02} : {minute:02} : {seconde:02}",end="\r")
while (True):
    afficher_heure()
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
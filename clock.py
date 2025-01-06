import time
heure = 0
minute = 0
seconde = 0
def afficher_heure():
    print(str(heure) + ":" + str(minute) + ":" + str(seconde),end="\r")
while (True):
    seconde= seconde + 1
    time.sleep(1)
    if seconde == 60:
        minute= minute + 1
        seconde=0
    if minute == 60:
        heure= heure + 1
        minute =0
    afficher_heure()

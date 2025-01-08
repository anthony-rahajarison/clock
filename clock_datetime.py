import time
import datetime
from datetime import timedelta

def regler_heure(h, m, s) :
    global heure
    heure = datetime.datetime(2024, 8, 1, h, m, s)

def demande_format() :
    rep = input("Format 24h ? (O/N): ")
    if rep == "O" :
        return True
    else :
        return False

#####################################
regler_heure(18, 59, 55)

if demande_format() == False :
    while True :
        print(heure.strftime("%I:%M:%S %p"), end="\r")
        heure += datetime.timedelta(seconds=1)
        time.sleep(1)
else :
    while True :
        print(heure.strftime("%H:%M:%S"), end="\r")
        heure += datetime.timedelta(seconds=1)
        time.sleep(1)
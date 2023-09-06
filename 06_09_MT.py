import random

minima=1
maxima=100
code = random.randint(minima,maxima)

aps = True

while (aps):
    c = int(input('entrer un code entre '+str(minima) +' et '+str(maxima+' : '))
    if c == code:
        print("le code est bon")
        break
    else :
        print("le jeu continu") 

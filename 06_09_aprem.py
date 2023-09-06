import random

minima= 1
maxima= 100
code = random.randint(minima,maxima)
print(code)
aps = True

while (aps):
    c = int(input('entrer un code entre ' + str(minima) + ' et ' + str(maxima) + ' : '))
    if c == code:
        print("le code est bon")
        break
    else:
        if code < c:
            print("le code est plus petit ") 
        elif code > c:
            print("le code est plus grand")
        print("vous pouvez rejouer")
        

with open("Nombre de parties.txt", "x") as fichier:
    fichier.write("Ceci est le contenu de mon fichier.")


import random

minima= 1
maxima= 100

score = 0
nbr_de_partie = 0


parties = True
while parties :  #cette boucle while c'est pour demander a l'utilisateur est ce que il veut joue 
    go = input("vueillez ecrire start pour rejouer une autre partie : ") 
    if str(go) == "start": # si l'utilasateur ecrit start le jeu va ce lancer 
        nbr_de_partie += 1  # c'est pour rajouter les parties 
        code = random.randint(minima,maxima) 
        print(code) 
        
        
        aps = True
        while (aps): 
            score+=1    # les tentives
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
                    
        
    else :#si l'utilisateur n'ecrit rien ou n'import quoi, dans ce cas le jeu s'arret 
        print("à bientot")
        break
        
    
with open ("le score",'w') as fi: # ouvrire un fichier et sommer les score de toutes les parties
        fi.write(str(score) )
        fi.close()
with open ("Nombre de parties", "w") as f:   #ouvrir un fichier et ecrire le nbr des parties  
        f.write(str(nbr_de_partie) )        
        f.close()





    
with open ("Nombre de parties", "r") as f: # lire le fichier f
    contenu = f.read()   
    print("le nbr de partie joue : "+ contenu)
    f.close()
    
with open("le score",'r') as fi: #lire le fichier fi
    contenu_2 = fi.read()
    print("le score dans chaque partie : " + contenu_2 )
    fi.close()
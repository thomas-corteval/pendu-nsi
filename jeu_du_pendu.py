import os
import time



while 1>0:
    tentatives = 0
    dico_mot = []
    # on demande le mot à montrer puis on le met en minuscule.
    solution = input("Enter le mot qui permetra de jouer au pendu: ")
    solution_minuscule= x=solution.lower()
    os.system("cls")
    time.sleep(0.5)
    dico_fautes = ["\n \n \n \n \n \n \n _|_","\n  | \n  |\n  | \n  |\n  |\n _|_ "," ________ \n  | \n  |\n  | \n  |\n  |\n _|_ "," ________ \n  |     | \n  |     0\n  | \n  |\n  |\n _|_ "," ________ \n  |     | \n  |     0\n  |    /\ \n  |\n  |\n _|_ "," ________ \n  |     | \n  |     0\n  |    /|\ \n  |     |\n  |\n _|_ "," ________ \n  |     | \n  |     0\n  |    /|\ \n  |     |\n  |    / \ \n _|_         You Lost"]
    tiret_bas = []
    
    # on va tester si les caractères correspondent à la liste acceptée.
    # ensuite on imprime le nombre de tirets bas correspondant au nombre
    # de lettres dans le mot.
    
    for i in range(len(solution_minuscule)):
        dico_mot.append(solution_minuscule[i])
        tiret_bas.append("_")
        nb_caractere = len(solution)
        nb_lettre = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","ç","é","è","â","ä","ù"]
        
        if dico_mot[i] not in nb_lettre:
            print("Erreur dans le mot que vous avez donné (rentré seulement des lettres svp !)")
            solution = input('Entrez le mot à deviner: ')
            
    print("le mot a deviner est : "+ len(solution_minuscule)*"_ ")
    
    time.sleep(0.25)
    
    # le joueur commence à deviner et on lui dit si il a vrai ou si il a faux
    # en lui redonnant son nombre de tentatives

    while tentatives < 7 and "_" in tiret_bas :
        proposition = input("Proposez une lettre : ")
        lettres_trouvees = ""
        
        if proposition in solution and len(proposition) == 1:
            lettres_trouvees = lettres_trouvees + proposition
            print("Bonne lettre!")
            
            for i in range(len(solution_minuscule)):
                l=[i for i in range(len(solution_minuscule)) if solution_minuscule[i]== proposition]
                
                for i in range(len(l)):
                    tiret_bas[l[i]] = proposition
            print(" ".join(tiret_bas))
    
        else:
            print("Raté, il vous reste ", 7 - tentatives, " tentatives")
            print(dico_fautes[tentatives])
            tentatives = tentatives + 1
    print(" _  _ __  _  _    _  _ __ __ _ \n( \/ )  \/ )( \  / )( (  |  ( \ \n )  (  O ) \/ (  \ /\ /)(/    / \n(__/ \__/\____/  (_/\_|__)_)__) \n ")    
    cond_recommencer = input("voulez vous recommencer ? o/n ")
    cond_dict = ["o","n"]
    
    if cond_recommencer in cond_dict:
        break
    
    else:
        os.system("cls")
print("Au revoir.")
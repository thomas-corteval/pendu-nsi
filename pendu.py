import os

tentatives = 0
dico_mot = []
# on demande le mot à montrer puis on le met en minuscule.
solution = input("Enter le mot qui permetra de jouer au pendu: ")
solution_minuscule= x=solution.lower()
os.system("cls")
dico_fautes = ["\n \n \n \n \n \n \n _|_","\n  | \n  |\n  | \n  |\n  |\n _|_ "," ________ \n  | \n  |\n  | \n  |\n  |\n _|_ "," ________ \n  |     | \n  |     0\n  | \n  |\n  |\n _|_ "," ________ \n  |     | \n  |     0\n  |    /\ \n  |\n  |\n _|_ "," ________ \n  |     | \n  |     0\n  |    /|\ \n  |     |\n  |\n _|_ "," ________ \n  |     | \n  |     0\n  |    /|\ \n  |     |\n  |    / \ \n _|_         Loose LOL"]

# on va tester si les caractères correspondent à la liste acceptée.
# ensuite on imprime le nombre de tirets bas correspondant au nombre de lettres dans le mot.
for i in range(len(solution_minuscule)):
    tiret_bas = []
    dico_mot.append(solution_minuscule[i])
    tiret_bas.append("_")
    nb_caractere = len(solution)
    nb_lettre = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","ç","é","è","â","ä","ù"]
    if dico_mot[i] not in nb_lettre:
        print("Veuillez entrer une lettre!")
        solution = input('Entrez le mot à deviner: ')
print(len(solution_minuscule)*"_ ")

# le joueur commence à deviner et on lui dit si il a vrai ou si il a faux en lui redonnant son nombre de tentatives
while tentatives < 7:
    proposition = input("Proposez une lettre : ")
    lettres_trouvees = ""
    if proposition in solution:
        lettres_trouvees = lettres_trouvees + proposition
        print("Bonne lettre!")
    else:
        print("Raté, il vous reste ", 7 - tentatives, " tentatives")
        print(dico_fautes[tentatives])
        tentatives = tentatives + 1
print(tiret_bas, "tiret_bas")
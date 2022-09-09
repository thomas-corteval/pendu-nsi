tentatives = 7
dico_mot = []
# on demande le mot à montrer puis on le mets en minuscule.
def demande_mot():
    solution = input("Enter le mot qui permetra de jouer au pendu (il ne s'affichera pas ne vous inquiétez pas): ")
    solution_minus= x=solution.lower()

# on va tester si les caractères correspondent à la liste acceptée.
# ensuite on imprime le nombre de tirets bas correspondant au nombre de lettres dans le mot.
for i in range(len(solution_minus)):
    tiret_bas = []
    dico_mot.append(solution_minus[i])
    nb_caractere = len(solution)
    nb_lettre = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","ç","é","è","â","ä","ù"]
    if dico_mot[i] not in nb_lettre:
        print("Il ne faut pas d'espace, de tiré, de chiffre ou de nimporte quel autre caractère autre que des lettres ")
        solution = input('Entrer le mot qui permetra de jouer au pendu (il sera cacher ne vous inquiétez pas): ')
print(len(solution)*"_ ")
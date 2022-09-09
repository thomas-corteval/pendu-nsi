tentatives = 7
dico_mot = []
# on demande le mot à montrer mais il n'apparait pas dans le terminal (pour ne pas tricher)
solution = input("Enter le mot qui permetra de jouer au pendu (il ne s'affichera pas ne vous inquiétez pas): ")

modif_solution= x=solution.lower()

# on va comparer le nombre de lettre du mot choisi (grace à counter) avec le nombre de caractère saisie plustot 
# sa permtra d'exclure tous caractère spéciaux ou chiffre saisie par le mj
for i in range(len(modif_solution)):
    tiret_bas = []
    dico_mot.append(modif_solution[i])
    nb_caractere = len(solution)
    nb_lettre = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","ç","é","è","â","ä","ù"]
    if dico_mot[i] not in nb_lettre:
        print("Il ne faut pas d'espace, de tiré, de chiffre ou de nimporte quel autre caractère autre que des lettres ")
        solution = input('Entrer le mot qui permetra de jouer au pendu (il sera cacher ne vous inquiétez pas): ')
print(len(solution)*"_ ")
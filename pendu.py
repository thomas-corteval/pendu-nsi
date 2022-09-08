import getpass
from collections import Counter

tentatives = 7

# on demande le mot à montrer mais il n'apparait pas dans le terminal (pour ne pas tricher)
solution = getpass.getpass(prompt = "Enter le mot qui permetra de jouer au pendu (il ne s'affichera pas ne vous inquiétez pas): ")


# on va comparer le nombre de lettre du mot choisi (grace à counter) avec le nombre de caractère saisie plustot 
# sa permtra d'exclure tous caractère spéciaux ou chiffre saisie par le mj
nb_caractère = len(solution)
c = Counter(solution)
nb_lettre = c['a'] + c['z'] + c['e'] + c['r'] + c['t'] + c['y'] + c['u'] + c['i'] + c['o'] + c['p'] + c['q'] + c['s'] + c['d'] + c['f'] + c['g'] + c['h'] + c['j'] + c['k'] + c['l'] + c['m'] + c['w'] + c['x'] + c['c'] + c['v'] + c['b'] + c['n']
if nb_caractère != nb_lettre:
    print("Il ne faut pas d'espace, de tiré, de chiffre ou de nimporte quel autre caractère autre que des lettres ")
    solution = getpass.getpass(prompt = 'Enter le mot qui permetra de jouer au pendu (il sera cacher ne vous inquiétez pas): ')


# on montre maintenant le nombre de lettre à trouver
print("Le mot à trouver est le suivant")
affichage = ""
for l in solution:
    affichage = affichage + "_ "
print(affichage)


# le joueur commence à jouer et on lui dit si il a vrai ou si il a faux en lui redonnant son nombre de tentatives
proposition = input("proposez une lettre : ")
lettres_trouvees = ""
if proposition in solution:
    lettres_trouvees = lettres_trouvees + proposition
    print("Bravo !")
else:
    tentatives = tentatives - 1
    print("Rater il vous reste ", tentatives, " tentatives")
 

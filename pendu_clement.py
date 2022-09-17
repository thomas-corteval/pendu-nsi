mot_decouper=("t","e","s","t")
lettre=("t")
underscore="_ _ _ _"

def lettre_dans_mot():
    nb_lettre=0
    position_lettre=[]
    position=0
    for i in mot_decouper:
        if lettre == mot_decouper[position]:
            position_lettre.append(position)
            nb_lettre=nb_lettre +1
        position=position+1
    return position_lettre
liste=lettre_dans_mot()
nb_lettre=len(mot_decouper)

def replace_():
    compteur=0
    compteur_list=0
    mot=""
    print("test")
    while compteur < nb_lettre :
        print("90")
        if compteur == liste[compteur_list]:
            mot=mot+lettre
            compteur_list=compteur_list+1
            print ("test0")
        else:
            compteur=compteur+1
            mot=mot+"_"
        mot=mot+" "
        print (mot)
    return mot
faute_1 ="\n \n \n \n \n \n \n _|_"
faute_2 ="\n  | \n  |\n  | \n  |\n  |\n _|_ "
faute_3 =" ________ \n  | \n  |\n  | \n  |\n  |\n _|_ "
faute_4 =" ________ \n  |     | \n  |     0\n  | \n  |\n  |\n _|_ "
faute_5 =" ________ \n  |     | \n  |     0\n  |    /\ \n  |\n  |\n _|_ "
faute_6 =" ________ \n  |     | \n  |     0\n  |    /|\ \n  |     |\n  |\n _|_ "
faute_7 =" ________ \n  |     | \n  |     0\n  |    /|\ \n  |     |\n  |    / \ \n _|_         Loose LOL"



def propsition():
    proposition = input("proposez une lettre : ")
    lettres_trouvees = ""
    if proposition in solution:
        lettres_trouvees = lettres_trouvees + proposition
        print("Bravo !")
    else:
        tentatives = tentatives - 1
        print("Rater il vous reste ", tentatives, " tentatives")
        
    if tentatives == 6 :
        print(faute_1)
    if tentatives == 5 :
        print(faute_2)
    if tentatives == 4 :
        print(faute_3)
    if tentatives == 3 :
        print(faute_4)
    if tentatives == 2 :
        print(faute_5)
    if tentatives == 1 :
        print(faute_6)
    if tentatives == 0 :
        print(faute_7)
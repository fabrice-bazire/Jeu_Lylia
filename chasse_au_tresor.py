import sys
import string

print("\nBienvenue Lylia !!\n")
choix = 0
indice = 0
print("Tu es ici dans le but de trouver le cadeau que tes amis t'ont offert pour ton anniversaire.\n")
print("Mon role va etre de t'aider dans cette tache.\n")
print("Cela va se derouler sous forme de chasse au tresor collaborative.")
print("Je m'explique, tu va avoir 3 indices a decouvrir.")
print("Tes amis vont se charger de te donner chacun les elements pour que tu puisse trouver un indice.")
print("A noter que si tu as du mal a trouver tes amis pourront t'aider car il leur a ete fourni des indices a te communiquer en cas de blocage de ta part dans la recherche d'un indice\n")
print("A chaque decouverte d'indice, tu pourra me partager l'indice en question et je te confirmerai si il est bon\n\n")

print("MENU\n---------------")
print("1 - Tu veut trouver le premier indice")
print("2 - Tu veut trouver le deuxieme indice")
print("3 - Tu veut trouver le troisieme indice")
print("4 - Tu pense avoir trouver un indice")
print("5 - Tu as trouve tout les indices")
print("6 - Quitter l'application\n")

choix = input('\nTape ton choix ici : ')
while choix < 1 or choix > 5 : 
    choix = input('Erreur\nTape ton choix ici : ')
if choix == 1 :
    print("\nC'est Justin qui est en charge de cet indice\nA toi de le contacter et de lui demander comment trouver cet indice\n")
if choix == 2 :
    print("\nC'est Yohann qui est en charge de cet indice\nA toi de le contacter et de lui demander comment trouver cet indice\n")
if choix == 3 :
    print("\nC'est Perrine qui est en charge de cet indice\nA toi de la contacter et de lui demander comment trouver cet indice\n")
if choix == 4 :
    indice = input("\nQuel indice veut tu valider ? (1, 2 ou 3) ")
    while indice < 1 or indice > 3 :
        indice = input("Erreur\nQuel indice veut tu valider ? (1, 2 ou 3) ")
    contenu_indice = input ("Entre l'indice que tu as trouve\nATTENTION : il faut mettre l'indice entre guillemets comme ceci : \"indice\"\n A toi : ")
    if indice == 1 :
        if contenu_indice == "parc d'attraction" or contenu_indice == "parc attraction" or contenu_indice == "attraction" or contenu_indice == "parc d'attractions" or contenu_indice == "parc attractions" or contenu_indice == "attractions":
            print("\nGood Job, l'indice est valide !!\nVoici un code qui te sera utile plus tard : 7 654 321 (note le)\nTu peut passer au suivant\n")
        else : 
            print("\nEncore un effort !!\n")
    if indice == 2 :
        if contenu_indice == "parc animalier" :
            print("\nBravo jeune padawan, l'indice est valide !!\nVoici un code qui te sera utile plus tard : 123 456 (note le)\nTu peut passer au suivant\n")
        else : 
            print("\nEncore un effort !!\n")
    if indice == 3 :
        if contenu_indice == "Moulins" or contenu_indice == "moulins":
            print("\nSuper, l'indice est valide !!\nVoici un code qui te sera utile plus tard : 7 264 221 (note le)\nTu peut acceder au menu 5 du programme\n")
        else : 
            print("\nTu touche au but !!\n")
if choix == 5 :
    print("\nA chaque decouverte d'indice, tu as recu des codes\nPour valider ta chasse au tresor, tu dois envoyer la somme de ces codes a Fabrice qui te confirmera ta quete")
if choix == 6 :
        sys.exit()

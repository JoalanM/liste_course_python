def menu():
    print("Choississez un chiffre parmi les 5 option suivantes :")
    print("1:   Ajouter un élément à la liste de courses")
    print("2:   Retirer un élément de la liste de courses")
    print("3:   Afficher la liste de courses")
    print("4:   Vider la liste de courses")
    print("5:   Quitter")


liste_course =list()#création d'une liste vide

choix= 0
while choix != 5:
    menu()
    choix= input("Votre choix : ")
    print("")
    try:
        choix=int(choix)
    except:
        print("vous n'avez pas entrez une valeur numérique \n")
    else:
        

        if choix==1:
            entrer=input("Elements à ajouter : ")
            print()
            liste_course.append(entrer)   
              
        elif choix==2:
            num_choix=int(input("Quelle éléments souhaiter vous supprimer : "))
            del liste_course[num_choix]

        elif choix==3:
            for element in liste_course: 
                print(element)
                
        elif choix==4:
            liste_course.clear()
            print("Votre liste à bien été vidée !")



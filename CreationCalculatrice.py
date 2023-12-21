

choix = 1


while choix!=5:
    choix= int(input("Que voulez-vous faire?\n\n1-Addition \n2-Soustraction\n3-Multiplication\n4-Division\n5-Finir:"))
    while choix<0 or choix>5:
        choix= int(input("Que voulez-vous faire?\n\n1-Addition \n2-Soustraction\n3-Multiplication\n4-Division\n5-Finir:"))
    if choix==1:
        i=0
        cal=1
        while cal!="0":
            cal= input("Entrez un chiffre 0 pour sortir):")        #Il peut y avoir une erreur car qd on tape à la machine, en mettand la virgule le code plante   
            i = i + float(cal)
        print("Addition vos",i)
        
    elif choix==2:
        i=0
        cal=1
        while cal!=0:
            cal= float(input("Entrez un chiffre (0 (ou plusieurs 0) pour sortir):"))
            i = i - cal
        print("Soustration vos",i)
        
    elif choix==3:
        choisir=1

        choisir= float(input("Entrez la table de multiplication que vous voulez faire entre 0 et 10:"))
        while choisir<0 or choisir>10:
            choisir = float(input("Erreur, entrez la table de multiplication que vous voulez faire entre 0 et 10:"))

        if choisir==1:
            cal= float(input("Entrez un chiffre dans la table de multiplication de 1:"))
            cal = cal * 1
            print("La multiplication est de:",cal)
        elif choisir==2:
            cal= float(input("Entrez un chiffre dans la table de multiplication de 2:"))
            cal = cal *2
            print("La multiplication est de:",cal)
        elif choisir==3:
            cal= float(input("Entrez un chiffre dans la table de multiplication de 3:"))
            cal = cal * 3
            print("La multiplication est de:",cal)
        elif choisir==4:
            cal= float(input("Entrez un chiffre dans la table de multiplication de 4:"))
            cal = cal * 4
            print("La multiplication est de:",cal)
        elif choisir==5:
            cal= float(input("Entrez un chiffre dans la table de multiplication de 5:"))
            cal = cal * 5
            print("La multiplication est de:",cal)
        elif choisir==6:
            cal= float(input("Entrez un chiffre dans la table de multiplication de 6:"))
            cal = cal * 6
            print("La multiplication est de:",cal)
        elif choisir==7:
            cal= float(input("Entrez un chiffre dans la table de multiplication de 7:"))
            cal = cal * 7
            print("La multiplication est de:",cal)
        elif choisir==8:
            cal= float(input("Entrez un chiffre dans la table de multiplication de 8:"))
            cal = cal * 8
            print("La multiplication est de:",cal)
        elif choisir==9:
            cal= float(input("Entrez un chiffre dans la table de multiplication de 9:"))
            cal = cal * 9
            print("La multiplication est de:",cal)
        elif choisir==10:
            cal= float(input("Entrez un chiffre dans la table de multiplication de 10:"))
            cal = cal * 10
            print("La multiplication est de:",cal)
    elif choix==4:
        choice=1
        choice= float(input("Entrez la table de division que vous-voulez faire entre 0 et 10:"))
        while choice<0 or choice>10:
            choix = float(input("Erreur, entrez la table de divsion que vous voulez entre de 0 et 10:"))
            
        if choice==1:
            cal= float(input("Entrez un chiffre dans la table de division de 1:"))
            cal = 1 / cal
            print("La division est de:",cal)
        elif choice==2:
            cal= float(input("Entrez un chiffre dans la table de division de 2:"))
            cal = 2 / cal
            print("La division est de:",cal)
        elif choice==3:
            cal= float(input("Entrez un chiffre dans la table de division de 3:"))
            cal = 3 / cal
            print("La division est de:",cal)
        elif choice==4:
            cal= float(input("Entrez un chiffre dans la table de division de 4:"))
            cal = 4 / cal
            print("La division est de:",cal)
        elif choice==5:
            cal= float(input("Entrez un chiffre dans la table de sivision de 5:"))
            cal = 5 / cal
            print("La divsion est de:",cal)
        elif choice==6:
            cal= float(input("Entrez un chiffre dans la table de division de 6:"))
            cal = 6 / cal
            print("La divsion est de:",cal)
        elif choice==7:
            cal= float(input("Entrez un chiffre dans la table de division de 7:"))
            cal = 7 / cal
            print("La divsion est de:",cal)
        elif choice==8:
            cal= float(input("Entrez un chiffre dans la table de division de 8:"))
            cal = 8 / cal
            print("La divsion est de:",cal)
        elif choice==9:
            cal= float(input("Entrez un chiffre dans la table de division de 9:"))
            cal = 9 / cal
            print("La divsion est de:",cal)
        elif choice==10:
            cal= float(input("Entrez un chiffre dans la table de division de 10:"))
            cal = 10 / cal
            print("La divsion est de:",cal)

    elif choix==5:
        print("Fini...")

""" #A revoir (mais code marche en multipliant par 2 chiffres)
        i=1
        c=0
        cal=1
        while cal!=0 and i!=0:
            cal= int(input("Entrez un chiffre (0 pour sortir)"))
            i = int(input("Entrez un chiffre (0 pour sortir)"))
            c = (cal * i) + c
            print("Le resultat de 2 nombre est de:",c,"(avec les sommes qui vont avec")
        print("Multiplication vos",c)"""
        
"""
x=float(input("Nombre 1="))
y=float(input("Nombre 2="))

print("Le resultat de la division est", x/y)"""

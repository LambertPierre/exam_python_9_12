
from colorama import init
init()
from colorama import Fore, Back, Style
#print(Fore.RED + 'some red text', end=" ")
#print(Back.GREEN + 'and with a green background')
#print(Style.DIM + 'and in dim text')
#print(Style.RESET_ALL)
#print('back to normal now')

ligne=["_","_","_","_","_","_"]

essais = 8
Victoire=False

def afficheLigne():
    print (ligne)

def proposerMot ():
    Reponse1="jungle"
    Reponse2="fluide"
    Reponse3="hyrule"
    Reponse4="profit"
    for i in range(0,6):
        if (motPropose[i] == Reponse1[i]):
            print (Fore.RED + motPropose[i], end=" ")
            print(Style.RESET_ALL)
            print ("Bonne lettre et bon emplacement!")
            print(Style.RESET_ALL)
            position = i+1
            print ("la position est:",position)
        else :
            for j in range(0,6):
                if motPropose[i] == Reponse1[j]:
                    print (Fore.YELLOW + motPropose[i], end=" ")
                    print(Style.RESET_ALL)
                    print ("Bonne lettre, mais mauvaise emplacement")
    for i in range(0,6):
        ligne[i]= motPropose[i]

def testVictoire():
    Reponse1="jungle"
    Reponse2="fluide"
    Reponse3="hyrule"
    Reponse4="profit"
    bonneLettre = 0
    for i in range(0,6):
        if (ligne[i]==Reponse1[i]):
            bonneLettre+=1
    if (bonneLettre==6):
        Victoire=True
        print("Bravo ! Vous avez trouvé le bon mot !")

# V Ne marche pas ¯\_(ツ)_/¯
def plusieursLettre():
    mot=["_","_","_","_","_","_"]
    premierDouble
    deuxiemeDouble
    for i in range(0,6):
        for j in range(i+1,6)
            if (motPropose[i]==mot[j])
                if (motPropose!=premireDouble and motPropose!=deuxiemeDouble)
                    premiereDouble=motPropose[i]
                    print ("Il y a deux ",motPropose[i]," !")
                else:
                    print ("Il y a trois ",motPropose[i]," !")
            else:
                mot[i]=motPropose[i]
    
    



print ("Bienvenue au Motus Python !")
while (essais>0 or Victoire==False):
    afficheLigne()
    motPropose = input("Veillez choisir une réponse...")
    proposerMot()
    testVictoire()
    essais-=1
    print ("il vous reste ",essais," essais !")
print ("Vous avez plus d'autre essaie :'(")
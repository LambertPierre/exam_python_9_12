
from colorama import init
init()
from colorama import Fore, Back, Style
#print(Fore.RED + 'some red text', end=" ")
#print(Back.GREEN + 'and with a green background')
#print(Style.DIM + 'and in dim text')
#print(Style.RESET_ALL)
#print('back to normal now')

ligne=["_","_","_","_","_","_"]

essais = 0
Victoire=False

def afficheLigne():
    print (ligne)
    
def proposerMot ():
    LigneEssais()
    Reponse1="jungle"
    Reponse2="fluide"
    Reponse3="hyrule"
    Reponse4="profit"
    motPropose = input("Veillez choisir une réponse...")
    for i in range(0,6):
        if (motPropose[i] == Reponse1[i]):
            print (Fore.RED + motPropose[i], end=" ")
            print(Style.RESET_ALL)
            print ("Bonne lettre et bon emplacement!")
            ligneReponse[i]= motPropose[i]
            position = i+1
            print ("la position est:",position)
        else :
            for j in range(0,6):
                if motPropose[i] == Reponse1[j]:
                    print (Fore.YELLOW + motPropose[i], end=" ")
                    print(Style.RESET_ALL)
                    print ("Bonne lettre, mais mauvaise emplacement")

def testVictoire():
    bonneLettre = 0
    for i in range(0,5):
        if (ligne1[i]==Reponse1[i]):
            bonneLettre+=1
    if (bonneLettre==6):
        Victoire=True
        print("Bravo ! Vous avez trouvé le bon mot !")



print ("Bienvenue au Motus Python !")
while (essais<8 or Victoire==False):
    afficheGrille()
    proposerMot()
    testVictoire()
    essais+=1
print ("Vous avez plus d'autre essaie :'(")
input()
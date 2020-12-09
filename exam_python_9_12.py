from colorama import init
init()
#from colorama import Fore, Back, Style
#print(Fore.RED + 'some red text', end=" ")
#print(Back.GREEN + 'and with a green background')
#print(Style.DIM + 'and in dim text')
#print(Style.RESET_ALL)
#print('back to normal now')

Reponse1=["n","a","c","r","e"]
Reponse2=["l","i","t","r","e"]
Reponse3=["t","r","o","n","c"]
Reponse4=["h","a","c","h","e"]

ligne1=["_","_","_","_","_","_"]
ligne2=["_","_","_","_","_","_"]
ligne3=["_","_","_","_","_","_"]
ligne4=["_","_","_","_","_","_"]

def afficheGrille():
        print (ligne1)
        print (ligne2)
        print (ligne3)
        print (ligne4)

afficheGrille()

input()
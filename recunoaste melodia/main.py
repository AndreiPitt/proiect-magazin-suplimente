import sys

from optiuni import *

if __name__ == '__main__':
    print("Aplicatia a pornit cu succes! Pentru inceput te rog sa alegi una dintre optiuni. ")
    lista_de_optiuni =[1, 2, 3]
    print("OPTIUNI: ")
    print("1 --- Proceseaza o melodie noua")
    print("2 --- Inregistreaza audio si recunoaste melodia daca aceasta exista in fisierul cu melodii")
    print("3 --- Inchide aplicatia")
    try:
        alegere = int(input("Care este alegerea ta? "))
        if alegere == 1:
            procesare()
        elif alegere == 2:
            recunoasteMelodia()
        else:
            sys.exit()
    except Exception as E:
        print("Ceva nu a mers bine :((")
        print(f"Eroarea este: {E}")

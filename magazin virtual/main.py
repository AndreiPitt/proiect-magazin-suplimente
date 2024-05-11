from client import Client
from manager import Manager
from produs import Produs
from utilizator import Utilizator
import sys
import datetime
import time

if __name__ == '__main__':
    ziua_curenta = datetime.datetime.strptime(datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S"),
                                              "%Y-%m-%d %H:%M:%S")
    print(ziua_curenta)
    print("Bun venit la Decathlon! Pentru a putea merge mai departe te rugam sa te loghezi.")
    print("Daca nu ai un cont deja, te rugam sa te inregistrezi.")
    print("Daca vrei sa renunti, apasa tasta q.")
    while True:
        alegere = input("Alegeti una dintre optiuni (1 - logare, 2 - inregistrare, q - quit: ")

        if alegere == "q":
            sys.exit()
        else:
            try:
                if int(alegere) == 1:
                    # LOGARE
                    Utilizator.loadPersons()
                    a = Utilizator.readFormFile()

                    nume = input("Introdu numele de utilizator: ")

                    if Utilizator.checkPersonByName(nume):
                        parola = input("Introduceti parola: ")
                        if [nume, parola] in a:
                            print("Te-ai logat cu succes")
                            print(
                                "Daca faci parte din staff introdu parola de administrator.In caz contrar apasa enter")
                            print("In cazul in care parola este gresita, magazinul considera automat ca esti un client!")
                            raspuns = input()
                            if raspuns == "admin":
                                # MANAGER
                                print(f"Salut {nume}, te-ai logat cu succes ca administrator.")
                                for persoana in Utilizator.persoaneCreate:
                                    if persoana.nume == nume:
                                        manager = Manager(persoana.nume, persoana.email, persoana.parola)

                                meniu = {
                                    "1": "Vizualizeaza produsele",
                                    "2": "Adauga produs nou",
                                    "3": "Sterge produs",
                                    "4": "Inchide magazinul",
                                }
                                optiuni = []
                                while True:
                                    print("Acesta este meniul dvs.")
                                    for keys, values in meniu.items():
                                        optiuni.append(keys)
                                        print(keys + " -> " + values)
                                    optiune = input(f"Introduceti o optiune din meniu: ")
                                    if optiune == '1':
                                        Produs.incarcareProduse()
                                        print(Produs.catalogProduse)
                                        print("In 5 secunde te vei intoarce la meniul principal")
                                        time.sleep(5)
                                    if optiune == '2':
                                        Produs.incarcareProduse()
                                        nume = input("Introdu numele de produsului: ")
                                        if Produs.checkProdusByName(nume):
                                            print("Acest produs exista deja!")

                                        else:
                                            pret = float(input(f"Te rog introdu pretul unei bucati de {nume}: "))
                                            stoc = int(input("Te rog introdu stockul produsului: "))
                                            produs1 = Produs(nume, pret, stoc)
                                            Produs.save(produs1)
                                            print(
                                                f"Produsul a fost creat cu succes.Datele sunt nume:{nume}, pret:{pret}, cantitate:{stoc}")
                                            print("In 5 secunde te vei intoarce la meniul principal")
                                            time.sleep(5)
                                    if optiune == '3':
                                        produse = Produs.readFormFile()
                                        nume_produs = input("Introdu numele produsului pe care vrei sa-l stergi: ")
                                        for produs in produse:
                                            if produs[0] == nume_produs:
                                                produse.remove([produs[0], produs[1], produs[2]])
                                        #Pentru verificare!
                                        #print(produse)

                                        tempProduse = []
                                        for detalii_produs in produse:
                                            stringProdus = detalii_produs[0]+";"+detalii_produs[1]+";"+detalii_produs[2]
                                            tempProduse.append(stringProdus)
                                        Produs.actualizareProduse(tempProduse)
                                        Produs.incarcareProduse()


                                        print("Produsul a fost sters din lista de produse.")
                                        print("In 5 secunde te vei intoarce la meniul principal")
                                        time.sleep(5)

                                    if optiune == '4':
                                        print("Ai inchis magazinul!")
                                        sys.exit()



                            else:
                                # CLIENT
                                print(f"Salut {nume}, bine ai venit la Decathlon")
                                for persoana in Utilizator.persoaneCreate:
                                    if persoana.nume == nume:
                                        client = Client(persoana.nume, persoana.email, persoana.parola)

                                meniu = {
                                    "1": "Vizualizeaza lista de produse",
                                    "2": "Adauga produs in cos",
                                    "3": "Sterge produs din cos",
                                    "4": "Pret total",
                                    "5": "Vizualizeaza cosul de cumparaturi",
                                    "6": "Anuleaza comanda",
                                }
                                optiuni = []
                                while True:
                                    print("Acesta este meniul dvs.")
                                    for keys, values in meniu.items():
                                        optiuni.append(keys)
                                        print(keys + " -> " + values)

                                    optiune = input(f"Introduceti o optiune din meniu: ")
                                    if optiune == '1':
                                        Produs.incarcareProduse()
                                        print(Produs.catalogProduse)
                                        print("In 5 secunde te vei intoarce la meniul principal")
                                        time.sleep(5)

                                    if optiune == '2':
                                        p = input("Introdu numele produsului pe care doresti sa l cumperi: ")
                                        if Produs.checkProdusByName(p):
                                            cantitate = int(input("Introdu cantitatea pe care doresti sa o cumperi: "))
                                            client.cos_de_cumparaturi.adauga_produs(p, cantitate)
                                        else:
                                            print("Nu exista acest produs in catalogul de produse al magazinului")
                                            time.sleep(5)

                                    if optiune == '3':
                                        p = input("Introdu numele produsului pe care doresti sa l scoti din cos: ")
                                        client.cos_de_cumparaturi.sterge_produs(p)
                                        print(f"Produsul {p} a fost scos din cosul dvs!")
                                        time.sleep(5)

                                    if optiune == '4':
                                        client.vizualizeaza_pretul_total()
                                        time.sleep(5)

                                    if optiune == '5':
                                        print(client.cos_de_cumparaturi.obiecte)
                                        print("In 5 secunde te vei intoarce la meniul principal")
                                        time.sleep(5)

                                    if optiune == '6':
                                        client.anuleaza_comanda()
                                        print("Comanda anulata")
                                        sys.exit()




                        else:
                            print("Parola gresita")
                            break

                    else:
                        print("Acest cont nu exista.Te rugam sa te inregistrezi!")



                elif int(alegere) == 2:
                    # INREGISTRARE
                    Utilizator.loadPersons()
                    nume = input("Introdu numele de utilizator: ")
                    if Utilizator.checkPersonByName(nume):
                        print("Acest username este folosit deja!")

                    else:
                        print(f"Numele de utilizator ales este {nume}")
                        email = input("Te rog introdu o adresa de email: ")
                        parola = input("Alege o parola: ")
                        user = Utilizator(nume, email, parola)
                        Utilizator.save(user)
                        print(f"Contul a fost creat cu succes.Datele sunt nume:{nume}, email:{email}, parola:{parola}")
                        print("Acum te poti loga!")

                else:
                    print("Nu exista aceasta optiune!")
            except ValueError:
                print("Nu ai introdus o optiune valida!")

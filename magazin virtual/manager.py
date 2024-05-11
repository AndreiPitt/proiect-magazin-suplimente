from utilizator import Utilizator


class Manager(Utilizator):
    def __init__(self, nume, email, parola):
        super().__init__(nume, email, parola)



    def adauga_produs(self, produs, cantitate):
        produs.stoc += cantitate

    def sterge_produs(self, produs, cantitate):
        if produs.stoc >= cantitate:
            produs.stoc -= cantitate
        else:
            print(f"Nu poti scazi {cantitate} din {produs.stoc}.")
            print("Cantiate insuficienta in stoc!")

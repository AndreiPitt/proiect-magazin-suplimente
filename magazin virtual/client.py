from cos_de_cumparaturi import Cos
from produs import Produs
from utilizator import Utilizator


class Client(Utilizator):
    def __init__(self, nume, email, parola):
        super().__init__(nume, email, parola)
        self.cos_de_cumparaturi = Cos()

    def vizualizeaza_pretul_total(self):
        s = 0
        Produs.incarcareProduse()
    #   print(Produs.catalogProduse)  # lista de obiecte
    #   print(self.cos_de_cumparaturi.obiecte)  # lista de tupluri (nume,cantitate)
        for produs in Produs.catalogProduse:
            for obiect_cumparat in self.cos_de_cumparaturi.obiecte:
                if obiect_cumparat[0] == produs.nume:
                    s += obiect_cumparat[1] * produs.pret

        print(f"Pretul total al cosului de cumparaturi este: {s} lei.")

    def anuleaza_comanda(self):
        self.cos_de_cumparaturi = []

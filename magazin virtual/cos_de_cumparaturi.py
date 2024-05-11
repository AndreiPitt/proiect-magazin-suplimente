class Cos:
    def __init__(self):
        self.obiecte = []

    def adauga_produs(self, produs, cantitate):
        self.obiecte.append((produs, cantitate))

    def sterge_produs(self, produs):
        self.obiecte = [(p, c) for p, c in self.obiecte if p != produs]



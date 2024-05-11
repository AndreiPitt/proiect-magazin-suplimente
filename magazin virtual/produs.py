class Produs:
    catalogProduse = []
    counter = 0

    def __init__(self, nume: str, pret: float, stoc: int):
        assert pret >= 0, f"Pretul {pret} este invalid."
        assert stoc >= 0, f"Pretul {stoc} este invalid."

        self.nume = nume
        self.pret = pret
        self.stoc = stoc
        Produs.counter += 1

    def save(self):
        if not Produs.checkProdusByName(self.nume):
            self.writeToFile("produse.csv")
            Produs.catalogProduse.append(self)

    def writeToFile(self, nume):
        with open(nume, 'a') as f:
            f.write(f"{self.nume};{self.pret};{self.stoc}\n")

    def actualizareProduse(self: list):
        with open("produse.csv", 'w') as f:
            for produs in self:
                f.write(produs+"\n")
        Produs.catalogProduse = []

    @classmethod
    def incarcareProduse(cls):
        with open("produse.csv", 'r') as f:
            content = [line.strip("\n") for line in f.readlines()]
            if content:
                for person in content:
                    details = person.split(";")
                    if not cls.checkProdusByName(details[0]):
                        tempProdus = Produs(details[0], float((details[1])), int(details[2]))
                        cls.catalogProduse.append(tempProdus)
                        Produs.counter += 1

    def __repr__(self):
        return f"{self.nume};pret:{self.pret};cantitate:{self.stoc}"

    @classmethod
    def readFormFile(cls):
        l = []
        f = open("produse.csv", "r")
        content_1 = f.read().split("\n")

        for line in content_1:
            detalii = line.split(";")
            l.append(detalii)
        del l[len(l) - 1]

        # Pentru verificare
        print(l)

        return l

    @classmethod
    def checkProdusByName(cls, nume):
        for produs in cls.catalogProduse:
            if produs.nume == nume:
                return True
        return False

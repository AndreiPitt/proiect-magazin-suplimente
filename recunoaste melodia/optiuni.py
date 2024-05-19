from fingerprints import *
from inregistrare import *


def procesare():
    """"
    Functia procesare() se foloseste pentru a suprascrie semnaturile melodiilor din fisier dupa ce au fost adaugate
    """
    proceseazaFisier("melodii", "fingerprints.csv")


def recunoasteMelodia():
    # Capturarea audio și generarea fingerprint-urilor
    melodie = inregistrareAudio()
    semnatura = generate_fingerprints(melodie)

    try:
        date = incarcaDinCSV("fingerprints.csv")
        # Recunoașterea melodiei
        rezultat, similaritate = gasesteMelodia(semnatura, date)
        print(f'Melodia care a fost recunoscuta: {rezultat},similaritate: {similaritate:.2f}')
    except:
        print("Melodia nu a fost gasita!")

import os
import librosa
import hashlib
import csv
import numpy as np


def generate_fingerprints(audio):
    """"
    Verifică dacă datele audio sunt de tipul punct-flotant iar apoi genereaza semnaturile audio
    """
    if not np.issubdtype(audio.dtype, np.floating):
        audio = librosa.util.buf_to_float(audio)

    S = librosa.stft(audio)
    S_db = librosa.amplitude_to_db(np.abs(S), ref=np.max)
    peaks = np.where(S_db > np.percentile(S_db, 85))
    fingerprints = [hashlib.sha1(f"{peak[0]}-{peak[1]}".encode()).hexdigest() for peak in zip(peaks[0], peaks[1])]
    return fingerprints


def save_fingerprints_to_csv(fingerprints, filename, song_name):
    # Salvarea fingerprint-urilor într-un fișier CSV
    with open(filename, 'a', newline='') as f:
        writer = csv.writer(f)
        for fp in fingerprints:
            writer.writerow([song_name, fp])


def proceseazaFisier(directory, csv_filename):
    print(f"Procesarea directorului {directory} a inceput!")
    with open(csv_filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["song_name", "fingerprint"])

    for file in os.listdir(directory):
        if file.endswith(".mp3") or file.endswith(".wav"):
            file_path = os.path.join(directory, file)
            audio, sr = librosa.load(file_path, sr=None)
            fingerprints = generate_fingerprints(audio)
            save_fingerprints_to_csv(fingerprints, csv_filename, file)
    print(f"Fisierul {csv_filename} a fost suprascris cu succes!")


def incarcaDinCSV(filename):
    fingerprints = {}
    with open(filename, 'r', newline='') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            song_name, fingerprint = row
            if song_name not in fingerprints:
                fingerprints[song_name] = []
            fingerprints[song_name].append(fingerprint)
    return fingerprints


def comparaFingerprints(fp1, fp2):
    """"
    Functia compara_fingerprints compara melodia inregistrata cu cele din directorul creat.
    """
    return len(set(fp1) & set(fp2)) / len(set(fp1) | set(fp2))


def gasesteMelodia(fingerprintinregistrat, fingerprinturisalvate):
    """"
    Functia gasesteMelodia returneaza:
            -numele melodiei care are fingerprinturile asemanatoare cu cele salvate in fisierul csv
            -similaritatea dintre cele doua semnaturi
    """
    melodie = None
    similaritate = 0.0
    for song_name, fingerprints in fingerprinturisalvate.items():
        comparare = comparaFingerprints(fingerprintinregistrat, fingerprints)
        if comparare > similaritate:
            similaritate = comparare
            melodie = song_name

    return melodie, similaritate

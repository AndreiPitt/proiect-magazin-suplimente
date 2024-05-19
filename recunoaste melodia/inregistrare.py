import pyaudio
import numpy as np


FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
inregistrare = []


def inregistrareAudio(timp=5, min_amplitudine=1000):
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    print("Inregistreaza...")
    for _ in range(0, int(RATE / CHUNK * timp)):
        data = stream.read(CHUNK)
        inregistrare.append(np.frombuffer(data, dtype=np.int16))

    print("Inregistrare audio finalizata!")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    if np.max(np.abs(np.hstack(inregistrare))) < min_amplitudine:
        print("Nivelul de amplitudine al fragmentului înregistrat este prea mic. Încercă din nou.")
        return None

    return np.hstack(inregistrare)

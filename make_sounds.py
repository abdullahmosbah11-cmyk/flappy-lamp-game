import wave
import math
import struct
import random
import os

os.makedirs("assets/audio", exist_ok=True)
SAMPLE_RATE = 44100

def save_wav(filename, samples):
    path = os.path.join("assets/audio", filename)
    with wave.open(path, "w") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(SAMPLE_RATE)
        data = b"".join(struct.pack("<h", max(-32767, min(32767, int(s * 32767)))) for s in samples)
        wf.writeframes(data)

flap = []
for i in range(int(SAMPLE_RATE * 0.12)):
    t = i / SAMPLE_RATE
    env = 1.0 - (t / 0.12)
    freq = 280 - (180 * (t / 0.12))
    val = (0.6 * math.sin(2 * math.pi * freq * t) + 0.4 * random.uniform(-1,1) * env * 0.5)
    flap.append(val)
save_wav("flap.wav", flap)

spark = []
for i in range(int(SAMPLE_RATE * 0.18)):
    t = i / SAMPLE_RATE
    env = 1.0 - (t / 0.18)
    freq = 987.77 if t < 0.06 else 1318.51 
    val = math.sin(2 * math.pi * freq * t) * env * 0.5
    spark.append(val)
save_wav("spark.wav", spark)

score = []
for i in range(int(SAMPLE_RATE * 0.14)):
    t = i / SAMPLE_RATE
    env = 1.0 - (t / 0.14)
    freq = 523.25 if t < 0.07 else 783.99
    val = math.sin(2 * math.pi * freq * t) * env * 0.4
    score.append(val)
save_wav("score.wav", score)

crash = []
for i in range(int(SAMPLE_RATE * 0.30)):
    t = i / SAMPLE_RATE
    env = (1.0 - (t / 0.30)) ** 1.5
    val = random.uniform(-1, 1) * env * 0.6
    crash.append(val)
save_wav("crash.wav", crash)

zap = []
for i in range(int(SAMPLE_RATE * 0.25)):
    t = i / SAMPLE_RATE
    env = 1.0 - (t / 0.25)
    freq = 140 + 90 * math.sin(2 * math.pi * 45 * t)
    wave_sq = 1.0 if math.sin(2 * math.pi * freq * t) >= 0 else -1.0
    zap.append(wave_sq * env * 0.45)
save_wav("zap.wav", zap)

buy = [0]
notes = [523.25, 659.25, 783.99]
for i in range(int(SAMPLE_RATE * 0.24)):
    t = i / SAMPLE_RATE
    env = 1.0 - (t / 0.24)
    freq = notes[min(2, int(t / 0.08))]
    wave_sq = 1.0 if math.sin(2 * math.pi * freq * t) >= 0 else -1.0
    buy.append(wave_sq * env * 0.35)
save_wav("buy.wav", buy)

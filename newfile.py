import matplotlib.pyplot as plt
import librosa

filename = '/Users/Jo/Documents/projects/voice_app/dev/aac/id00029/9gE-_vyJmFQ/00058.m4a'
y,sr = librosa.load(filename)

plt.plot(y[0:1000])

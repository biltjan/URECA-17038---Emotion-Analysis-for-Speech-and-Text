from tkinter import *
import os
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from scipy.io import wavfile
from scipy.io.wavfile import read
from scipy import signal

def show_waveplot(window, template, speaker, session, number, frow, fcol):
	directory = os.path.join("Data", "Results", template, speaker, str(session))
	file_name = os.path.join(directory, "".join((str(number),".wav")))
	samplingFrequency, signalData = wavfile.read(file_name)
	plt.title('Wave')
	plt.plot(signalData)
	plt.xlabel('Sample')
	plt.ylabel('Amplitude')
	figure = Figure(figsize=(5,3), dpi = 100)
	a = figure.add_subplot(111)
	a.plot(signalData)
	canvas = FigureCanvasTkAgg(figure, window)
	canvas.draw()
	canvas.get_tk_widget().grid(row=frow, column =fcol, columnspan = 10, rowspan = 10)

def show_specplot(window, template, speaker, session, number, frow, fcol):
	directory = os.path.join("Data", "Results", template, speaker, str(session))
	file_name = os.path.join(directory, "".join((str(number),".wav")))
	samplingFrequency, signalData = wavfile.read(file_name)
	plt.specgram(signalData,Fs=samplingFrequency, cmap="jet")
	plt.xlabel('Time')
	plt.ylabel('Frequency')
	plt.xticks(rotation=90)
	figure = Figure(figsize=(5,3), dpi = 100)
	a = figure.add_subplot(111)
	a.specgram(signalData, Fs=samplingFrequency)
	canvas = FigureCanvasTkAgg(figure, window)
	canvas.draw()
	canvas.get_tk_widget().grid(row= frow, column =fcol, columnspan = 10, rowspan = 10)

def multi_waveplots(template, speaker, session, selections):
	plt.clf()
	directory = os.path.join("Data", "Results", template, speaker, str(session))
	for i in range (1, len(selections)+1):
		file_name = os.path.join(directory, "".join((str(selections[i-1]+1),".wav")))
		input_data = read(file_name)
		audio = input_data[1]
		plt.plot(audio[0:30000], alpha=1/len(selections))
	plt.ylabel("Amplitude")
	plt.xlabel("Time")
	# set the title  
	plt.title("Multiple Wav")
	# display the plot
	plt.show()

def multi_specplots(template, speaker, session, selections):
	plt.clf()
	directory = os.path.join("Data", "Results", template, speaker, str(session))
	for i in range (1, len(selections)+1):
		file_name = os.path.join(directory, "".join((str(selections[i-1]+1),".wav")))
		samplingFrequency, signalData = wavfile.read(file_name)
		plt.specgram(signalData,Fs=samplingFrequency, alpha=1/i, cmap="jet")
	plt.xlabel('Time')
	plt.ylabel('Frequency')
	plt.xticks(rotation=90)
	plt.show()
	



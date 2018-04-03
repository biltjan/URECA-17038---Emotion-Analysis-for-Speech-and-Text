from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk 
import os
import jsonhandler as jsh
import recorder as rec
import plotter
import winsound


class CreateCorpus(Frame):
	counter = 0
	myDict = {}
	senList = []
	emoList = []
	session = 0

	#selected item, useful data read and write along with counter and session
	templateSelect=""
	speakerSelect=""

	#lists for drop down
	templateList=[]
	speakerList=[]

	#for display what to be said
	numberVar = None
	sentenceVar = None
	emotionVar = None
	templateVar = None
	speakerVar = None
	sessionVar = None
	selTemplate = None
	selSpeaker = None

	def record_button(self, display, template, speaker, session, number):
		rec.record_audio(template, speaker, session, number)
		plotter.show_waveplot(display, self.templateSelect[:-5], self.speakerSelect[:-5], self.session, self.counter, 0, 0)

	def delete_button(self, template, speaker, session, number):
		directory = os.path.join("Data", "Results", template, speaker, str(session))
		file_name = os.path.join(directory, "".join((str(number),".wav")))
		os.remove(file_name)

	def play_button(self, template, speaker, session, number):
		directory = os.path.join("Data", "Results", template, speaker, str(session))
		file_name = os.path.join(directory, "".join((str(number),".wav")))
		winsound.PlaySound(file_name, winsound.SND_ALIAS)	

	def prepare_lists(self):
		path = os.path.join("Data", "Template")
		self.templateList.clear()
		self.templateList = os.listdir(path)

		#path=os.path.join(path, str(self.templateList[0]))
		path = os.path.join("Data", "Speaker")
		self.speakerList.clear()
		self.speakerList = os.listdir(path)

		path=os.path.join("Data", "Results", str(self.templateList[0])[:-5], str(self.speakerList[0])[:-5])
		os.makedirs(path, exist_ok=True)
		if (len(os.listdir(path)) != 0):
			self.session = len(os.listdir(path))+1
		else:
			self.session = 1

	def load_template(self, template, speaker):
		self.templateSelect=template
		self.speakerSelect=speaker
		self.myDict = jsh.get_template(template)
		jsh.separate_template(self.myDict, self.senList, self.emoList)
		self.counter = 0

		path=os.path.join("Data", "Results", template[:-5], speaker[:-5])
		os.makedirs(path, exist_ok=True)
		if (len(os.listdir(path)) != 0):
			self.session = len(os.listdir(path))+1
		else:
			self.session = 1
		path=path=os.path.join("Data", "Results", template[:-5], speaker[:-5], str(self.session))
		os.makedirs(path, exist_ok=True)
		self.change_stuff()
		self.templateVar.set(template[:-5])
		self.speakerVar.set(speaker[:-5])
		self.sessionVar.set(str(self.session))

	def change_stuff(self, button = None):
		self.counter = self.counter + 1
		if self.counter >= len(self.senList)+1:
			self.numberVar.set("Session Finished!")
			self.sentenceVar.set("Session Finished!")
			self.emotionVar.set("Session Finished!")

		else:
			self.numberVar.set(str(self.counter))			
			self.sentenceVar.set(self.senList[self.counter-1])
			self.emotionVar.set(self.emoList[self.counter-1])


	def __init__(self, parent, controller):
		self.prepare_lists()
		ttk.Frame.__init__(self, parent)
		imagebuttonHome = ImageTk.PhotoImage(Image.open("home.png"))
		buttonHome = ttk.Button(self, style="parent.Option.TButton", image=imagebuttonHome)
		buttonHome.bind("<Button-1>", lambda eff: controller.show_frame("HomePage"))
		buttonHome.image = imagebuttonHome    
		buttonHome.grid(row=0, columnspan=100, sticky=W)

		labelTitle = ttk.Label(self, text="Create Corpus", style="parent.Important.TLabel")
		labelTitle.place(relx=.5, y=15, anchor="center")

		gridFrame = Frame(self, background="#CCFFCC")
		gridFrame.grid(row=1, column=0)

		labelTemplate = ttk.Label(gridFrame, text="Template", style="parent.TLabel", width=10)
		labelTemplate.grid(row=0, column=0, columnspan=2)
		
		labelSpeaker = ttk.Label(gridFrame, text="Speaker", style="parent.TLabel", width=10)
		labelSpeaker.grid(row=0, column=2, columnspan=2)

		imagebuttonSubmit = ImageTk.PhotoImage(Image.open("submit.png"))
		buttonHome = ttk.Button(gridFrame, style="parent.Option.TButton", image=imagebuttonSubmit)
		buttonHome.bind("<Button-1>", lambda eff: self.load_template(selTemplate.get(), selSpeaker.get()))
		buttonHome.image = imagebuttonSubmit    
		buttonHome.grid(row=1, column=4, columnspan=2)

		selTemplate = StringVar()
		selTemplate.set(self.templateList[0])
		dropDownTemplate = OptionMenu(gridFrame, selTemplate, *self.templateList)
		dropDownTemplate.grid(row=1, column=0, columnspan=2)

		selSpeaker = StringVar()
		selSpeaker.set(self.speakerList[0])
		dropDownSpeaker = OptionMenu(gridFrame, selSpeaker, *self.speakerList)
		dropDownSpeaker.grid(row=1, column=2, columnspan=2)

		self.numberVar = StringVar()
		self.sentenceVar = StringVar()
		self.emotionVar = StringVar()
		self.templateVar = StringVar()
		self.speakerVar = StringVar()
		self.sessionVar = StringVar()
		self.numberVar.set("Current Number")
		self.sentenceVar.set("Sentence to be said")
		self.emotionVar.set("Emotion of speech")
		self.templateVar.set("Selected Template")
		self.speakerVar.set("Selected Speaker")
		self.sessionVar.set("Current Session")

		label = ttk.Label(gridFrame, text="Number", style="parent.TLabel")
		label.grid(row=2, column=0, columnspan = 2)
		numberLabel = Label(gridFrame, textvariable = self.numberVar, background="#CCFFCC", font="Helvetica 12 bold")
		numberLabel.grid(row=2, column=2, columnspan = 2)

		label = ttk.Label(gridFrame, text="Sentence", style="parent.TLabel")
		label.grid(row=3, column=0, columnspan = 2)
		sentenceLabel = Label(gridFrame, textvariable = self.sentenceVar, background="#CCFFCC", font="Helvetica 12 bold")
		sentenceLabel.grid(row=3, column=2, columnspan = 2)

		label = ttk.Label(gridFrame, text="Emotion", style="parent.TLabel")
		label.grid(row=4, column=0, columnspan = 2)
		emotionLabel = Label(gridFrame, textvariable = self.emotionVar, background="#CCFFCC", font="Helvetica 12 bold")
		emotionLabel.grid(row=4, column=2, columnspan = 2)

		label = ttk.Label(gridFrame, text="Template:", style="parent.TLabel")
		label.grid(row=2, column=6, columnspan = 2)
		numberLabel = Label(gridFrame, textvariable = self.templateVar, background="#CCFFCC", font="Helvetica 12")
		numberLabel.grid(row=2, column=8, columnspan = 2)

		label = ttk.Label(gridFrame, text="Speaker", style="parent.TLabel")
		label.grid(row=3, column=6, columnspan = 2)
		sentenceLabel = Label(gridFrame, textvariable = self.speakerVar, background="#CCFFCC", font="Helvetica 12")
		sentenceLabel.grid(row=3, column=8, columnspan = 2)

		label = ttk.Label(gridFrame, text="Session", style="parent.TLabel")
		label.grid(row=4, column=6, columnspan = 2)
		emotionLabel = Label(gridFrame, textvariable = self.sessionVar, background="#CCFFCC", font="Helvetica 12")
		emotionLabel.grid(row=4, column=8, columnspan = 2)

		plotWaveButton = ttk.Button(gridFrame, text="Wave", style = "parent.Small.TButton", command = lambda: plotter.show_waveplot(plotFrame, self.templateSelect[:-5], self.speakerSelect[:-5], self.session, self.counter, 0, 0))
		plotWaveButton.grid(row=5, column= 0, sticky=W)

		plotSpecButton = ttk.Button(gridFrame, text="Spec", style = "parent.Small.TButton", command = lambda: plotter.show_specplot(plotFrame, self.templateSelect[:-5], self.speakerSelect[:-5], self.session, self.counter, 0, 0))
		plotSpecButton.grid(row=5, column= 1, sticky=W)

		plotFrame = Frame(gridFrame, background="#FFFFFF")
		plotFrame.grid(row=7, column=0, rowspan=100, columnspan = 10, sticky=W)

		Label(plotFrame).grid()

		imagebuttonRecord = ImageTk.PhotoImage(Image.open("button3.png"))#Change to apt. icon
		buttonRec = ttk.Button(gridFrame, style="parent.Option.TButton", image=imagebuttonRecord)
		buttonRec.bind("<Button-1>", lambda eff: self.record_button(plotFrame, self.templateSelect[:-5], self.speakerSelect[:-5], self.session, self.counter))
		buttonRec.image = imagebuttonRecord    
		buttonRec.grid(row=2, column=10, columnspan=2, rowspan=3)

		playButton = ttk.Button(gridFrame, text="Play", command = lambda: self.play_button(self.templateSelect[:-5], self.speakerSelect[:-5], self.session, self.counter))
		playButton.grid(row=7, column=10, sticky=W)

		acceptButton = ttk.Button(gridFrame, text="Accept", command = lambda : self.change_stuff())
		acceptButton.grid(row=8, column=10, sticky=W)

		deleteButton = ttk.Button(gridFrame, text="Delete", command = lambda : self.delete_button(self.templateSelect[:-5], self.speakerSelect[:-5], self.session, self.counter))
		deleteButton.grid(row=9, column=10, sticky=W)
		#playButton = ttk.Button(gridFrame, text="Accept", style="parent.Option.TLabel", self.play)



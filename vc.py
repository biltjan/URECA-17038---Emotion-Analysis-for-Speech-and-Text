from tkinter import *
from tkinter import ttk
import os
from PIL import Image, ImageTk 
import plotter
import winsound

class ViewCorpus(Frame)	:
	fileList = []
	templateList=[]
	speakerList=[]
	session=""

	templateVar=None
	speakerVar=None
	sessionVar=None
	selected=None

	templateSelect=""
	speakerSelect=""

	def create_list(self, listofFile):
		self.update(self.templateVar.get(), self.speakerVar.get(), self.sessionVar.get())
		path = os.path.join("Data", "Results", self.templateSelect, self.speakerSelect, self.session)
		print(path)
		fileList = os.listdir(path)
		for filename in fileList:
			listofFile.delete(0, END)
		for filename in fileList:
			listofFile.insert(END, filename)

	def update(self, templateSelect, speakerSelect, sessionSelect):
		self.templateSelect = templateSelect
		self.speakerSelect = speakerSelect
		self.session = sessionSelect

	def __init__(self, parent, controller):
		ttk.Frame.__init__(self, parent)
		imagebuttonHome = ImageTk.PhotoImage(Image.open("home.png"))
		buttonHome = ttk.Button(self, style="parent.Option.TButton", image=imagebuttonHome)
		buttonHome.bind("<Button-1>", lambda eff: controller.show_frame("HomePage"))
		buttonHome.image = imagebuttonHome    
		buttonHome.grid(row=0, columnspan=100, sticky=W)

		labelTitle = ttk.Label(self, text="View Corpus", style="parent.Important.TLabel")
		labelTitle.place(relx=.5, y=15, anchor="center")
		self.templateVar = StringVar()
		self.speakerVar = StringVar()
		self.sessionVar = StringVar()
		self.templateVar.set("TemplateA")
		self.speakerVar.set("U1")
		self.sessionVar.set("1")
		#make sure selectmode = multiple after the show_plot support mutiple graphs at once
		listofFile = Listbox(self, height = 10, selectmode=MULTIPLE)
		listofFile.bind("<Button-1>", lambda eff: self.update(self.templateVar.get(), self.speakerVar.get(), self.sessionVar.get()))
		listofFile.grid(row=3, column=0, columnspan = 2, rowspan=7)

		labelTemplate = ttk.Label(self, text="Template", style="parent.TLabel")
		labelTemplate.grid(row=1, column=0, columnspan=2)

		entryTemplate = Entry(self, textvariable = self.templateVar)
		entryTemplate.grid(row=2, column=0, columnspan = 2)

		labelSpeaker = ttk.Label(self, text="Speaker", style="parent.TLabel")
		labelSpeaker.grid(row=1, column=2, columnspan = 2)

		entrySpeaker = Entry(self, textvariable = self.speakerVar)
		entrySpeaker.grid(row=2, column=2, columnspan=2)

		label = ttk.Label(self, text="Session", style="parent.TLabel")
		label.grid(row=1, column=4, columnspan=2)

		entrySpeaker = Entry(self, textvariable = self.sessionVar)
		entrySpeaker.grid(row=2, column=4, columnspan=2)

		submitButtonImage = ImageTk.PhotoImage(Image.open("submit.png"))
		submitButton = ttk.Button(self, image=submitButtonImage, command = lambda: self.create_list(listofFile))
		submitButton.image = submitButtonImage
		submitButton.grid(row=1, column= 6, rowspan = 2)

		plotWaveButton = ttk.Button(self, text="Wave", style = "parent.Small.TButton", command = lambda: plotter.show_waveplot(self, self.templateSelect, self.speakerSelect, self.session, listofFile.curselection()[0]+1, 14, 0))
		plotWaveButton.grid(row=13, column= 0, sticky=W)

		plotSpecButton = ttk.Button(self, text="Spec", style = "parent.Small.TButton", command = lambda: plotter.show_specplot(self, self.templateSelect, self.speakerSelect, self.session, listofFile.curselection()[0]+1, 14, 0))
		plotSpecButton.grid(row=13, column= 1, sticky=W)

		mergeWave = ttk.Button(self, text="Mult Wave", style = "parent.Small.TButton", command = lambda: plotter.multi_waveplots(self.templateSelect, self.speakerSelect, self.session, listofFile.curselection()))
		mergeWave.grid(row=13, column=2, sticky=W)

		mergeSpec = ttk.Button(self, text="Mult Spec", style = "parent.Small.TButton", command = lambda: plotter.multi_specplots(self.templateSelect, self.speakerSelect, self.session, listofFile.curselection()))
		mergeSpec.grid(row=13, column=3, sticky=W)
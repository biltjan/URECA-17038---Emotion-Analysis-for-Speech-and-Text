from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk 
import os
import cc
import vc


class EmotiveRecApp(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        Tk.iconbitmap(self, default="emorec.ico")
        window = Frame(self)
        window.pack(side = "top", fill = "both", expand = True)
        window.grid_rowconfigure(0,weight = 1)
        window.grid_columnconfigure(0, weight = 1)

        self.geometry("800x600")
        self.title("Emotive Recorder")
        style=ttk.Style()
        style.configure('.', font="Helvetica 12", background='#CCFFCC')
        style.configure("Important.TLabel", font=('Courier', 20, 'bold'), background="#CCFFCC", foreground="#9A9A9A", anchor=CENTER)
        style.configure("Option.TButton", background="#CCFFCC", foreground="#9A9A9A", anchor=CENTER)
        style.configure("Read.TLabel", font=('Helvetica', 12,'bold'), background="#CEFFCE")
        style.configure("Small.TButton", font=('Helvetica', 8))

        self.frames = {}
        self.frames["HomePage"] = HomePage(parent=window, controller=self)
        self.frames["CreateCorpus"] = cc.CreateCorpus(parent=window, controller=self)
        self.frames["ViewCorpus"] = vc.ViewCorpus(parent=window, controller=self)

        self.frames["HomePage"].grid(row=0, column=0, sticky="nsew")
        self.frames["CreateCorpus"].grid(row=0, column=0, sticky="nsew")
        self.frames["ViewCorpus"].grid(row=0, column=0, sticky="nsew")
        self.show_frame("HomePage")

    def show_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()

class HomePage(Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        labelTitle = ttk.Label(self, text = "Please choose an option:", style = "Important.TLabel")
        labelTitle.pack(side = "top", fill="x")

        buttonImage1 = ImageTk.PhotoImage(Image.open("button3.png"))#nanti ganti
        buttonSelect1 = ttk.Button(self,text="Create Template", style="Option.TButton", image=buttonImage1, compound=LEFT)
        buttonSelect1.bind("<Button-1>", lambda eff: controller.show_frame("CreateCorpus"))#nanti ganti
        buttonSelect1.image = buttonImage1    
        buttonSelect1.pack(fill="x")

        buttonImage2 = ImageTk.PhotoImage(Image.open("button3.png"))#nanti ganti
        buttonSelect2 = ttk.Button(self,text="Create User", style="Option.TButton", image=buttonImage2, compound=LEFT)
        buttonSelect2.bind("<Button-1>", lambda eff: controller.show_frame("CreateCorpus"))#nanti ganti
        buttonSelect2.image = buttonImage2    
        buttonSelect2.pack(fill="x")

        buttonImage3 = ImageTk.PhotoImage(Image.open("button3.png"))
        buttonSelect3 = ttk.Button(self,text="Create Corpus", style="Option.TButton", image=buttonImage3, compound=LEFT)
        buttonSelect3.bind("<Button-1>", lambda eff: controller.show_frame("CreateCorpus"))
        buttonSelect3.image = buttonImage3
        buttonSelect3.pack(fill="x")

        buttonImage4 = ImageTk.PhotoImage(Image.open("button3.png"))#nanti ganti
        buttonSelect4 = ttk.Button(self,text="View Corpus", style="Option.TButton", image=buttonImage4, compound=LEFT)
        buttonSelect4.bind("<Button-1>", lambda eff: controller.show_frame("ViewCorpus"))
        buttonSelect4.image = buttonImage4    
        buttonSelect4.pack(fill="x")

        buttonImage5 = ImageTk.PhotoImage(Image.open("button3.png"))#nanti ganti
        buttonSelect5 = ttk.Button(self,text="Settings", style="Option.TButton", image=buttonImage5, compound=LEFT)
        buttonSelect5.bind("<Button-1>", lambda eff: controller.show_frame("CreateCorpus"))#nanti ganti
        buttonSelect5.image = buttonImage5    
        buttonSelect5.pack(fill="x")

        img=Image.open('cc.png')
        logo=ImageTk.PhotoImage(img)
        pictureFrame = Label(self, image=logo, background="#CCFFCC")
        pictureFrame.image = logo
        pictureFrame.pack(side="bottom", anchor=E)

if __name__ == "__main__":
    app = EmotiveRecApp()
    app.mainloop()

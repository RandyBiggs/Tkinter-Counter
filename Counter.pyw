from tkinter import * 
counter = 0
increment = 1
class MyGUI:

    def __init__(self):
        self.__mainwindow = Tk()
        self.__mainwindow.title("Counter")
        self.__mainwindow.iconbitmap(r'C:\Users\RandyBiggs\Desktop\Counter\favicon\counterfavi.ico')
        self.cLabel = Label(text="0", height=3)
        self.cLabel.grid(row=0, column=1, sticky=W+E)
        self.pButton = Button(self.__mainwindow, text="+", width=5, height=2)
        self.pButton.grid(row=3, column=2, sticky=E)
        self.pButton.bind('<Button-1>', self.pCounter)
        self.mButton = Button(self.__mainwindow, text="-", width=5,height=2)
        self.mButton.grid(row=3, column=0, sticky=E)
        self.mButton.bind("<Button-1>", self.mCounter)
        self.rButton = Button(self.__mainwindow, text="Reset", width=20, height=2)
        self.rButton.grid(row=3, column=1, sticky=E)
        self.rButton.bind("<Button-1>", self.rCounter)
        self.sButton = Button(self.__mainwindow, text="⌂", width=2, height=1)
        self.sButton.grid(row=0, column=2)
        self.sButton.bind("<Button-1>", self.openSettings)
        self.incEntry = Entry(self.__mainwindow, width=15)
        self.incEntry.bind("<Return>", self.setIncrement)        
        mainloop()

    def pCounter(self, event):
        global counter
        global increment
        counter += increment
        self.cLabel['text'] = counter

    def mCounter(self, event):
        global counter
        global increment
        counter -= increment
        self.cLabel['text'] = counter
    def rCounter(self, event):
        global counter
        global increment
        counter = 0
        self.cLabel['text'] = counter
    def openSettings(self, event):
        self.incEntry.grid(row=1,column=1, sticky=W+E)
        self.incLabel = Label(self.__mainwindow, text="Set Increment:")
        self.incLabel.grid(row=1, column=0, sticky=W+E)
    def setIncrement(self, event):
        global increment
        increment = int(self.incEntry.get())
gui = MyGUI()

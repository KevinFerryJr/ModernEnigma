
# Enigma Machine Emulator - main.py
import enigma
from PIL import ImageTk, Image
from tkinter import  Label, Entry, Button,Tk

# COLORS #
bgColor = "#10252d"
fgBold = "#e0f8cf"
fgLight = "#3a626d"

#Letters local copy
letters = enigma.letters

class Window(Tk):
    def __init__(self):
        super().__init__()
        self.title("Enigma Emulator")
        self.padSmall = 20
        self.padMed = 40
        self.img = Image.open("head.jpg")
        self.header = ImageTk.PhotoImage((self.img))
        self.img = Image.open("foot.jpg")
        self.footer = ImageTk.PhotoImage((self.img))

#        # Header Image #
#        self.headerLabel = Label(self,# image=self.header,padx=self.padMed, #bg=bgColor)
#        self.headerLabel.pack()

        #Title Lable
        self.encodelabel = Label(self, text="Enter the text you'd like to encode below...", pady=self.padMed, bg=bgColor, fg=fgBold)
        self.encodelabel.pack()
        
        #Text Entry
        self.entry = Entry(self, justify="center", bg=fgLight, fg=bgColor)
        self.entry.pack()
        
        #Text Output Label
        self.outputlabel = Label(self, text="Encoder Outputs Here...", pady=self.padSmall, bg=bgColor, fg=fgLight)
        self.outputlabel.pack()
        
        #Encode Button
        self.encodeButton = Button(self, text="Encode", command=self.onclickEncode, bg=bgColor, fg=fgBold, activebackground=fgLight)
        self.encodeButton.pack()
        
        #Load Button
        self.loadButton = Button(self, text="Load Entry", command=self.onclickLoad, bg=bgColor, fg=fgBold, activebackground=fgLight)
        self.loadButton.pack()
        
        #Reset Button
        self.resetButton = Button(self, text="Reset", command=self.onclickReset, bg=bgColor, fg=fgBold, activebackground=fgLight)
        self.resetButton.pack()
        
        #Save Button
        self.saveButton = Button(self, text="Save Msg", command=self.onclickSave, bg=bgColor, fg=fgBold, activebackground=fgLight)
        self.saveButton.pack()
        
        #First Buffer
        self.pad1 = Label(self, text="", bg=bgColor)
        self.pad1.pack()
        
        #Scrambler Settings
        self.scramblerSettings = Label(self, text="Scrambler Settings", pady=self.padSmall, bg=bgColor, fg=fgLight)
        self.scramblerSettings.pack()
        
        #TickUp Button (R2)
        self.tickUpButton = Button(self, text="R2↑", command=self.onclickRotate2up, bg=bgColor, fg=fgBold, activebackground=fgLight)
        self.tickUpButton.pack()
        
        #TickUp Button (R1)
        self.tickUpButton = Button(self, text="R1↑", command=self.onclickRotate1up, bg=bgColor, fg=fgBold, activebackground=fgLight)
        self.tickUpButton.pack()
        
        #TickUp Button (R0)
        self.tickUpButton = Button(self, text="R0↑", command=self.onclickRotate0up, bg=bgColor, fg=fgBold, activebackground=fgLight)
        self.tickUpButton.pack()
        
        #Rotor Rotations
        self.rotorLabel = Label(self, text = str(enigma.c.resetRotors()), pady=self.padSmall, bg=bgColor, fg=fgBold)
        self.rotorLabel.pack()
        
        #TickDown Button (R0)
        self.tickDownButton = Button(self, text="R0↓", command=self.onclickRotate0dwn, bg=bgColor, fg=fgBold, activebackground=fgLight)
        self.tickDownButton.pack()
        
        #TickDown Button (R1)
        self.tickDownButton = Button(self, text="R1↓", command=self.onclickRotate1dwn, bg=bgColor, fg=fgBold, activebackground=fgLight)
        self.tickDownButton.pack()
        
        #TickDown Button (R2)
        self.tickDownButton = Button(self, text="R2↓", command=self.onclickRotate2dwn, bg=bgColor, fg=fgBold, activebackground=fgLight)
        self.tickDownButton.pack()
        
        #TickDown UP
        self.tickUpButton = Button(self, text="Tick Up", command=self.onClickTickUp, bg=bgColor, fg=fgBold, activebackground=fgLight)
        self.tickUpButton.pack()
        
        #TickDown Button
        self.tickUpButton = Button(self, text="Tick Down", command=self.onClickTickDown, bg=bgColor, fg=fgBold, activebackground=fgLight)
        self.tickUpButton.pack()
        
        #Second Buffer
        self.pad2 = Label(self, text="", bg=bgColor)
        self.pad2.pack()
        
        #Plug Instruction Label
        self.plugInstLabel = Label(self, text="Enter the letters you'd like to swap below...", pady=self.padSmall, bg=bgColor, fg=fgBold)
        self.plugInstLabel.pack()
        
        #Plug1 Label
        self.plug1Label = Label(self, text="Plug One", bg=bgColor, fg=fgLight)
        self.plug1Label.pack()
        
        #Plug1 Entry
        self.plug1Entry = Entry(self, justify="center", bg=fgLight, fg=bgColor)
        self.plug1Entry.pack()
        
        #Plug2 Label
        self.plug2Label = Label(self, text="Plug Two", bg=bgColor, fg=fgLight)
        self.plug2Label.pack()
        
        #Plug2 Entry
        self.plug2Entry = Entry(self, justify="center", bg=fgLight, fg=bgColor)
        self.plug2Entry.pack()
        
        #Add Plug
        self.addPlugButton = Button(self, text="Add Plugs", command=self.onclickAddPlug, bg=bgColor, fg=fgBold, activebackground=fgLight)
        self.addPlugButton.pack()

		#Reset Plug
        self.resetPlugButton = Button(self, text="Reset", command=self.onclickResetPlug, bg=bgColor, fg=fgBold, activebackground=fgLight)
        self.resetPlugButton.pack()
        
        #plug padding Label
        self.plugPadLabel = Label(self, text="", bg=bgColor)
        self.plugPadLabel.pack()
        
        #Plug Settings Label
        self.plugSettingLabel = Label(self, text="Plugboard Settings", bg=bgColor, fg=fgLight)
        self.plugSettingLabel.pack()
        
        #Plugboard Array
        self.plugArray = Label(self, text=enigma.getPlugs(), pady=self.padMed, bg=bgColor, fg=fgBold)
        self.plugArray.pack()

        # Footer Image #
        self.footerLabel = Label(self, image=self.footer,pady=self.padMed, bg=bgColor)
        self.footerLabel.pack()
	
	# ON CLICK ENCODE #
    def onclickEncode(self):
        try:
            self.outputlabel.configure(text=str(enigma.c.encode(self.entry.get())))
            self.rotorLabel.config(text = str(enigma.c.readRotors()))
        except:
            enigma.c.resetRotors()
            print("Invalid Encoder Entry.")

     # ON CLICK RESET
    def onclickReset(self):
        enigma.c.resetRotors()
        self.rotorLabel.config(text = str(enigma.c.readRotors()))
        self.entry.delete(0,'end')
        
    # ON CLICK SAVE
    def onclickSave(self):
      f = open("Saved.txt", "w")
      f.write(self.outputlabel.cget("text"))
      
    # ON CLICK LOAD
    def onclickLoad(self):
      f = open("Load.txt", "r")
      self.entry.delete(0,len(self.entry.cget("text")))
      self.entry.insert(0,f.read())
      
    # ON CLICK TICK UP
    def onClickTickUp(self):
        enigma.c.tick(True)
        self.rotorLabel.config(text = str(enigma.c.readRotors()))
    	
    # ON CLICK TICK DOWN
    def onClickTickDown(self):
        enigma.c.tick(False)
        self.rotorLabel.config(text = str(enigma.c.readRotors()))
    
    
    # ON CLICK ROTATE DIAL (UP 0)
    def onclickRotate0up(self):
        enigma.c.setRotor(0,True)
        self.rotorLabel.config(text = str(enigma.c.readRotors()))
    	
    	# ON CLICK ROTATE DIAL (UP 1)
    def onclickRotate1up(self):
        enigma.c.setRotor(1,True)
        self.rotorLabel.config(text = str(enigma.c.readRotors()))
    	
    	# ON CLICK ROTATE DIAL (UP 2)
    def onclickRotate2up(self):
        enigma.c.setRotor(2,True)
        self.rotorLabel.config(text = str(enigma.c.readRotors()))
    	
    	# ON CLICK ROTATE DIAL (DWN 0)
    def onclickRotate0dwn(self):
        enigma.c.setRotor(0,False)
        self.rotorLabel.config(text = str(enigma.c.readRotors()))
    	
    	# ON CLICK ROTATE DIAL (DWN 1)
    def onclickRotate1dwn(self):
        enigma.c.setRotor(1,False)
        self.rotorLabel.config(text = str(enigma.c.readRotors()))
    	
    	# ON CLICK ROTATE DIAL (DWN 2)
    def onclickRotate2dwn(self):
        enigma.c.setRotor(2,False)
        self.rotorLabel.config(text = str(enigma.c.readRotors()))
    

    # ON CLICK ADD PLUG
    def onclickAddPlug(self):
        try:
    	    p1 = enigma.letters.index(self.plug1Entry.get().lower())
    	    p2 = enigma.letters.index(self.plug2Entry.get().lower())
    	    enigma.p.addPlug(p1,p2)
    	    self.plugArray.config(text = enigma.getPlugs())
        except:
            print("Invalid Plug Entry.")
    	
    # ON CLICK RESET PLUG
    def onclickResetPlug(self):
        enigma.p.reset()
        self.plugArray.config(text = enigma.getPlugs())
        self.plug1Entry.delete(0,"end")
        self.plug2Entry.delete(0,"end")
    		

win = Window()
win.configure(bg=bgColor)
win.onclickReset()
win.mainloop()

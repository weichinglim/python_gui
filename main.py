"""
Wei Ching Lim

--This file contains the class for GUI window.
"""

import tkinter
from tkinter import *
from PIL import Image, ImageTk
import utilities as u

class gui:
      def __init__(self, master):
        frame = Frame(master, width=750, height=500)
        frame.place(x=30, y=30)

        # -------------------- Menu Creation ------------------------
        #Private Industries in 2019        
        self.mbar = Frame(frame, relief = 'raised', width=750, bd = 2)
        self.mbar.pack(expand = 0, fill = X, side = TOP)

        # ------------------- Create industry choice menu -----------

        self.fgbutton = Menubutton(self.mbar, text = 'Year 2019')
        self.fgbutton.pack(side = TOP)
        self.fgmenu = Menu(self.fgbutton, tearoff=0)
        self.fgbutton['menu'] = self.fgmenu

        # Populate image choice menu
        self.fgmenu.add('command', label = 'Q1 to Q4 - 2019', command = self.tot_2019)
        self.fgmenu.add('command', label = 'Quarter 1 2019', command = self.q1_2019)
        self.fgmenu.add('command', label = 'Quarter 2 2019', command = self.q2_2019)
        self.fgmenu.add('command', label = 'Quarter 3 2019', command = self.q3_2019)
        self.fgmenu.add('command', label = 'Quarter 4 2019', command = self.q4_2019)
        
        # ------------------- Create industry choice menu ----------- 
        #Private Industries in 2020
        self.fgbutton = Menubutton(self.mbar, text = 'Year 2020')
        self.fgbutton.pack(side = TOP)
        self.fgmenu = Menu(self.fgbutton, tearoff=0)
        self.fgbutton['menu'] = self.fgmenu

        # Populate image choice menu
        self.fgmenu.add('command', label = 'Q1 to Q4 - 2020', command = self.tot_2020)
        self.fgmenu.add('command', label = 'Quarter 1 2020', command = self.q1_2020)
        self.fgmenu.add('command', label = 'Quarter 2 2020', command = self.q2_2020)
        self.fgmenu.add('command', label = 'Quarter 3 2020', command = self.q3_2020)
        self.fgmenu.add('command', label = 'Quarter 4 2020', command = self.q4_2020)
        
        # ------------------- Create industry choice menu ----------- 
        #Private Industries both 2019 and 2020
        self.fgbutton = Menubutton(self.mbar, text = 'Private Industries 2019-2020')
        self.fgbutton.pack(side = TOP)
        self.fgmenu = Menu(self.fgbutton, tearoff=0)
        self.fgbutton['menu'] = self.fgmenu

        # Populate image choice menu
        self.fgmenu.add('command', label = 'Q1 to Q4 in 2019 & 2020', command = self.both_years)

        #--------------------- Listbox frame ------------------------            
        self.lf = Frame(frame, bd=2, relief='groove')
        self.lb = Label(self.lf, text='Log:')
        self.bt1 = Button(self.lf, text = 'Clear', command = self.clear)
        self.listbox = Listbox(self.lf, height=4)
        self.sbl = Scrollbar(self.listbox, orient=VERTICAL, command=self.listbox.yview)
        self.listbox.configure(yscrollcommand=self.sbl.set)
        self.lb.pack(side=LEFT, padx=5)
        self.bt1.pack(side = BOTTOM)
        self.sbl.pack(side=RIGHT, fill=Y)
        self.listbox.pack(padx=5, fill = X)
        self.lf.pack(expand=0, fill=X, pady=5, side = BOTTOM)

        #--------------------- Textbox frame & Image Label ------------------------        
        self.tb = Text(frame, height = 5, width =55)
        self.lbl = Label(self.tb, text = "Please 'Clear' before loading the next image.")
        self.lbl.config(font = ("Palatino", 12))
        self.tb.pack(side=BOTTOM)
        self.lbl.pack(side=BOTTOM)
        
        self.lblImage = tkinter.Label()

      # -------------------- Function defs ------------------------

      def clear(self):
          self.listbox.delete(0, END)
          self.lblImage.config(image='')

      def tot_2019(self):
          self.lblImage.config(image='')
          u.Industry2019()
          try:
             self.image1 = Image.open('ind2019.png')
             self.obj1 = ImageTk.PhotoImage(self.image1)
             self.lblImage = tkinter.Label(root, image= self.obj1)
             self.lblImage.image = self.obj1
             self.lblImage.place(x=300, y=10)
             self.listbox.insert(END, 'Private industries percent change contribution to GDP during 2019.')
          except:
             self.listbox.insert(END, 'Error loading graph')

      def q1_2019(self):
          self.lblImage.config(image='')
          u.Ind2019_Q1()
          try:
             self.image1 = Image.open('ind2019_Q1.png')
             self.obj1 = ImageTk.PhotoImage(self.image1)
             self.lblImage = tkinter.Label(root, image= self.obj1)
             self.lblImage.image = self.obj1
             self.lblImage.place(x=300, y=10)
             self.listbox.insert(END, 'Private industies performance during Quarter 1 of 2019.')
          except:
             self.listbox.insert(END, 'Error loading graph')
          
      def q2_2019(self):
          self.lblImage.config(image='')
          u.Ind2019_Q2()
          try:
             self.image1 = Image.open('ind2019_Q2.png')
             self.obj1 = ImageTk.PhotoImage(self.image1)
             self.lblImage = tkinter.Label(root, image= self.obj1)
             self.lblImage.image = self.obj1
             self.lblImage.place(x=300, y=10)
             self.listbox.insert(END, 'Private industies performance during Quarter 2 of 2019.')
          except:
             self.listbox.insert(END, 'Error loading graph')
          
      def q3_2019(self):
          self.lblImage.config(image='')
          u.Ind2019_Q3()
          try:
             self.image1 = Image.open('ind2019_Q3.png')
             self.obj1 = ImageTk.PhotoImage(self.image1)
             self.lblImage = tkinter.Label(root, image= self.obj1)
             self.lblImage.image = self.obj1
             self.lblImage.place(x=300, y=10)
             self.listbox.insert(END, 'Private industies performance during Quarter 3 of 2019.')
          except:
             self.listbox.insert(END, 'Error loading graph')

      def q4_2019(self):
          self.lblImage.config(image='')
          u.Ind2019_Q4()
          try:
             self.image1 = Image.open('ind2019_Q4.png')
             self.obj1 = ImageTk.PhotoImage(self.image1)
             self.lblImage = tkinter.Label(root, image= self.obj1)
             self.lblImage.image = self.obj1
             self.lblImage.place(x=300, y=10)
             self.listbox.insert(END, 'Private industies performance during Quarter 4 of 2019.')
          except:
             self.listbox.insert(END, 'Error loading graph')
             
      def tot_2020(self):
          self.lblImage.config(image='')
          u.Industry2020()
          try:
             self.image1 = Image.open('ind2020.png')
             self.obj1 = ImageTk.PhotoImage(self.image1)
             self.lblImage = tkinter.Label(root, image= self.obj1)
             self.lblImage.image = self.obj1
             self.lblImage.place(x=300, y=10)
             self.listbox.insert(END, 'Private industries percent change contribution to GDP during 2020.')
          except:
             self.listbox.insert(END, 'Error loading graph')

      def q1_2020(self):
          self.lblImage.config(image='')
          u.Ind2020_Q1() 
          try:
             self.image1 = Image.open('ind2020_Q1.png')
             self.obj1 = ImageTk.PhotoImage(self.image1)
             self.lblImage = tkinter.Label(root, image= self.obj1)
             self.lblImage.image = self.obj1
             self.lblImage.place(x=300, y=10)
             self.listbox.insert(END, 'Private industies performance during Quarter 1 of 2020.')
          except:
             self.listbox.insert(END, 'Error loading graph')
          
      def q2_2020(self):
          self.lblImage.config(image='')
          u.Ind2020_Q2()
          try:
             self.image1 = Image.open('ind2020_Q2.png')
             self.obj1 = ImageTk.PhotoImage(self.image1)
             self.lblImage = tkinter.Label(root, image= self.obj1)
             self.lblImage.image = self.obj1
             self.lblImage.place(x=300, y=10)
             self.listbox.insert(END, 'Private industies performance during Quarter 2 of 2020.')
          except:
             self.listbox.insert(END, 'Error loading graph')
          
      def q3_2020(self):
          self.lblImage.config(image='')
          u.Ind2020_Q3() 
          try:
             self.image1 = Image.open('ind2020_Q3.png')
             self.obj1 = ImageTk.PhotoImage(self.image1)
             self.lblImage = tkinter.Label(root, image= self.obj1)
             self.lblImage.image = self.obj1
             self.lblImage.place(x=300, y=10)
             self.listbox.insert(END, 'Private industies performance during Quarter 3 of 2020.')
          except:
             self.listbox.insert(END, 'Error loading graph')

      def q4_2020(self):
          self.lblImage.config(image='')
          u.Ind2020_Q4() 
          try:
             self.image1 = Image.open('ind2020_Q4.png')
             self.obj1 = ImageTk.PhotoImage(self.image1)
             self.lblImage = tkinter.Label(root, image= self.obj1)
             self.lblImage.image = self.obj1
             self.lblImage.place(x=300, y=10)
             self.listbox.insert(END, 'Private industies performance during Quarter 3 of 2020.')
          except:
             self.listbox.insert(END, 'Error loading graph')             

      def both_years(self):
          self.lblImage.config(image='')
          u.Industry()  
          try:
             self.image1 = Image.open('totalIndustry.png')
             self.obj1 = ImageTk.PhotoImage(self.image1)
             self.lblImage = tkinter.Label(root, image= self.obj1)
             self.lblImage.image = self.obj1
             self.lblImage.place(x=300, y=10)
             self.listbox.insert(END, 'Private industries percent change contribution to GDP from 2019 to 2020 on a quarterly basis.')
          except:
             self.listbox.insert(END, 'Error loading graph')
        
# main--setup tkinter object, instantiate gui class and display
root = Tk()
root.geometry('1550x1300')
root.configure(bg='light blue')
all = gui(root)
root.title('Data Visualization of Private Industries Contribution to GDP in 2019 to 2020')
root.pack_propagate(0)
root.mainloop()



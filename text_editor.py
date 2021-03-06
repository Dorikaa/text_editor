from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import font
from tkinter.tix import *
import os
import sys

ext = ""

root = Tk("Text Editor")
root.title("TextEditor by horisenpai")

text = Text(root)
text.grid()

fonts = list(font.families())
fonts.sort()

def createMain():
   global fonts
   menubar = Menu(root)
   scrollbar = ScrolledWindow(menubar)
   scrollbar.pack()
   filemenu = Menu(menubar, tearoff=0)
   filemenu.add_command(label="New File", command=newfile)
   filemenu.add_command(label="Save", command=saveas)
   filemenu.add_separator()
   filemenu.add_command(label="Exit", command=close_window)

   menubar.add_cascade(label="File", menu=filemenu)
   fontmenu = Menu(menubar, tearoff=0)
   fontmenu.add_command(label="Arial", command=FontArial)
   fontmenu.add_command(label="Calibri", command=FontCalibri)
   fontmenu.add_command(label="Courier", command=FontCourier)
   fontmenu.add_command(label="Courier New", command=FontCourierNew)
   fontmenu.add_command(label="TimesNewRoman", command=FontTimes)
   fontmenu.add_command(label="Helvetica", command=FontHelvetica)
   fontmenu.add_separator()

   for item in fonts:
      fontmenu.add_command(label="" + item, command=GetFonts(item))

   menubar.add_cascade(label="Font", menu=fontmenu)
   helpmenu = Menu(menubar, tearoff=0)
   helpmenu.add_command(label="About", command=aboutit)
   menubar.add_cascade(label="Help", menu=helpmenu)

   root.config(menu=menubar)
   root.mainloop()


def saveas():
   global text
   global ext
   t = text.get("1.0", END)
   savelocation = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("Text File", "*.txt"), ("All Files", "*.*")))
   file1,ext = os.path.splitext(savelocation)
   file1 = open(savelocation, "w+")
   file1.write(t)
   file1.close()

def newfile():
   global text
   choice = messagebox.askyesno("Warning!", "Would you like to save before?")
   if choice == True:
      saveas()

   if choice == False:
      text.delete('1.0', END)

def close_window():
   root.destroy()

def aboutit():
   messagebox.showinfo("Information", "This program was made by horisenpai")

def FontHelvetica():
   global text
   text.config(font="Helvetica")

def FontCourier():
   global text
   text.config(font="Courier")

def FontTimes():
   global text
   text.config(font="Times")

def FontSymbol():
   global text
   text.config(font="Symbol")

def FontArial():
   global text
   text.config(font="Arial")

def FontCalibri():
   global text
   text.config(font="Calibri")

def FontCourierNew():
   global text
   text.config(font="Courier New")

def GetFonts(n):
   global text
   global fonts
   for item in fonts:
      return text.config(font="item")


createMain()



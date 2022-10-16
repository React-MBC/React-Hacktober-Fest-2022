import time
import easyocr
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Progressbar
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk

# Initilize Tkinter
root = Tk() 
file_name = ""

app = easyocr.Reader(['en']) # Languages as a list

# Setup Layout in Tkinter
file_lab = Label(root, text="Upload The File:").grid(row=0,column=0,padx=10, pady=10, rowspan=2)
file_up = Button(root, text="Browse File", width="15", command=lambda:upload_file())
file_up.grid(row=0,column=1,padx=10, pady=10)
file_pro = Button(root, text="Process", width=15, command=lambda:readImg())
file_pro.grid(row=1,column=1,padx=10, pady=10)

default_text = "Please Wait while the Process Completes\n\nMight Take Some Time\n\nBe Patient"
file_en = Text(root)
file_en.insert(INSERT, default_text)
file_en.grid(row=3,column=0,padx=10, pady=10)

# Function

def readImg():
    time.sleep(.5)
    filename = file_up['text']
    output = app.readtext(filename)
    text = ''
    for op in output:
        text += op[1] + ' '
    file_en.delete(1.0, END)

    file_en.insert(INSERT, text)
    
def upload_file():
    global img
    exts = r' .jpg .jpeg .png'
    f_types = [('Image Files', exts)]
    filename = filedialog.askopenfilename(filetypes=f_types)
    file_up.config(text = filename, width=15)


root.mainloop()
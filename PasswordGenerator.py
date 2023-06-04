#Password Genberator Project

from tkinter import *
import random, string
import pyperclip
root=Tk()
root.title("Password Generator")
root.geometry("600x600")
root.resizable(0,0)
heading=Label(root,text=" Pyhton Password Generator", font=("Arial 15 bold")).pack()
# Giving Option to user
pass_label=Label(root,text="Password Length", font=("Arial 10 bold")).pack()
pass_len=IntVar()

#from tkinter module spinbox
length=Spinbox(root,from_= 6,to_= 32, textvariable=pass_len, width=15).pack()

pass_str=StringVar()
#Use ASCII Values

def Generator():
    password=''
    characters=random.choice(string.ascii_lowercase)+random.choice(string.ascii_uppercase)+random.choice(string.digits)+random.choice(string.punctuation)
    for x in range(0,4):
        password+=random.choice(characters)
    for y in range(pass_len.get()- 4):
        password+=random.choice(characters)
       
    pass_str.set(password)
    
Button(root,text="Generate the Password", command=Generator).pack(pady=5)
Entry(root,textvariable=pass_str).pack()

def Copy_password():
    pyperclip.copy(pass_str.get())
Button(root,text="Copy To Clipboard", command=Copy_password).pack(pady=5)
root.mainloop()

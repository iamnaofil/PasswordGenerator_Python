from tkinter import *
import random
import string
import pyperclip

root = Tk()
root.title("Password Generator")
root.geometry("600x600")
root.resizable(0, 0)

heading = Label(root, text="Python Password Generator", font=("Arial", 15, "bold")).pack()

pass_label = Label(root, text="Password Length", font=("Arial", 10, "bold")).pack()

pass_len = IntVar()

lenght = Spinbox(root, from_=6, to_=32, textvariable=pass_len, width=15).pack()

pass_str = StringVar()

def generate_password():
    password = ""
    for _ in range(pass_len.get()):
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)
    pass_str.set(password)

generate_button = Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=5)

password_entry = Entry(root, textvariable=pass_str)
password_entry.pack()

def copy_password():
    pyperclip.copy(pass_str.get())

copy_button = Button(root, text="Copy to Clipboard", command=copy_password)
copy_button.pack(pady=5)

root.mainloop()

import tkinter as tk
import random
import string
import pyperclip

def generate_password():
    password_length = int(entry_length.get())
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=password_length))
    label_password.config(text="Generated password : " + password)
    pyperclip.copy(password)

root = tk.Tk()
root.title("Password generator")

label_length = tk.Label(root, text="Password length :")
label_length.pack()
entry_length = tk.Entry(root)
entry_length.pack()

button_generate = tk.Button(root, text="Generate password", command=generate_password)
button_generate.pack()

label_password = tk.Label(root, text="")
label_password.pack()

root.mainloop()
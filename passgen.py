import random
from random import choice
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

root = ctk.CTk()
root.geometry('760x400')
root.title('Password Generator')

ctk.set_appearance_mode('System')
ctk.set_default_color_theme('green')


posschars = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, '!', '?', '%', '', '/', '(', ')', '=', '\'', '"', '\\', '*', '[', ']', '{', '}', '+', '-']
for i in range(65, 91):
    posschars.append(chr(i))
for i in range(97, 123):
    posschars.append(chr(i))

def genpass():
    chars = []
    for i in range(10):
        char = random.choice(posschars)
        chars.append(char)
    password = ''.join(str(x) for x in chars)
    textbox.configure(text = password)
    with open('C:\programmi\passgenerator\passwords.txt', 'r+') as file:
        if password not in file:
            file.write(f'{password}\n')
            file.close()

def ezremgen():
    myWords = []
    with open("C:\programmi\passgenerator\words.txt", "r") as inF:
        for line in inF:
            line = line.strip()
            if line == "": continue
            myWords.append(line)
    myWordsOf8Chars = list(filter(lambda x : len(x) == 8, myWords))
    word = random.choice(myWordsOf8Chars)
    chars = []
    chars.append(word)
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    for i in range(2):
        n = random.choice(nums)
        chars.append(n)
    password = ''.join(str(x) for x in chars)
    textbox.configure(text = password)
    with open('passwords.txt', 'r+') as file:
        if password not in file:
            file.write(f'{password}\n')
            file.close()

def copy():
    pw = textbox.cget("text")
    root.clipboard_clear()
    root.clipboard_append(pw)

def setappmode(new_appearance_mode: str):
    ctk.set_appearance_mode(new_appearance_mode)

bottoneg = ctk.CTkButton(root, width=80, height=30, text='Generate password', command=genpass, font=('Helvetica', 15))
bottoneg.grid(row=0, column=0, padx=200, pady=50)
textbox = ctk.CTkLabel(root, width=10, height=40, text='Here you will get the password', font=('Helvetica', 15))
textbox.grid(row=1, column=0, sticky='ns')
textbox.configure(anchor='center')
ezremmodeg = ctk.CTkButton(root, width=80, height=30, text = 'Generate an easy-remembering password', font=('Helvetica', 15), command=ezremgen)
ezremmodeg.grid(row=2, column=0, padx=200, pady=50)
copybutton = ctk.CTkButton(root, width=30, height=20, text='Copy', font=('Helvetica', 15),command=lambda:copy())
copybutton.grid(row=1, column=1)

appearmodeopt = ctk.CTkOptionMenu(root, width=50, height=30, values=["System", "Light", "Dark"], command=setappmode, font=('Helvetica', 15))
appearmodeopt.grid(row=4, column=0)
appearmodelab = ctk.CTkLabel(root, width=50, height=30, text='Set appearance mode', font=('Helvetica', 15))
appearmodelab.grid(row=3, column=0, padx=30)
def esci():
    if messagebox.askyesno(title='Quit', message="Are you sure you want to quit?"):
        root.destroy()
exitbtn = ctk.CTkButton(root, width=30, height=20, text='Exit', command=esci, font=('Helvetica', 15))
exitbtn.grid(row=4, column=0, sticky='se')



root.protocol("WM_DELETE_WINDOW", esci)
root.mainloop()

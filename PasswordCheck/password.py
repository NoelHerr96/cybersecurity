"""_
A password must be at least 12 characters long
Must be a combination of upper-, lowercase letters, numbers and symbols
Easy for you to remember


"""
import tkinter as tk
from tkinter import *
import re


root = tk.Tk()

root.title("Password Checker")

def pass_validator():
    password = pass_inp.get()
    length = False
    digit = False
    uppercase_symbol = False
    special_symbol = False
    
    if password: 
        if len(password) >=12 and len(password)<=24:
            print(f"Length {len(password)} is great.")
            length = True
        else:
            print(f"Your password needs some work. Your password should be at least between 12-24 characters long.")
            
        if re.search(r"\d", password): #Seaches for a digit character
            print("There is at least a digit")
            digit = True
        else:
            print("There is no digit")
            
        if re.search(r"[A-Z]", password): #Searches for uppercase character
            print("There is at least an uppercase character")
            uppercase_symbol = True
        else:
            print("There is no uppercase character")
            
        if re.search(r"[^a-zA-Z0-9]", password): #Searches for characters that are not a digit or a letter, aka special symbols.
            print("There is at least a special symbol")
            special_symbol = True
        else:
            print("There is no special symbol")
        
        return(print(f"\n -Length: {bool(length)} \n -Digit: {bool(digit)} \n -Uppercase: {bool(uppercase_symbol)} \n -Special symbol: {bool(special_symbol)} \n-----------"))

    print(f"Password: {password} Length: {len(password)} \n -Length: {bool(length)} \n -Digit: {bool(digit)} \n -Uppercase: {bool(uppercase_symbol)} \n -Special symbol: {bool(special_symbol)} ")
    return
        
root.geometry("750x300") #Size of the window
tk.Label(root, text="Your password").pack() 

pass_inp = Entry(root, width=40)
pass_inp.pack()

# Button for validating password
close_btn = tk.Button(root, text="Validate password", width="25", command=pass_validator)
close_btn.pack()

# Button for close
close_btn = tk.Button(root, text="close", width="25", command=root.destroy)
close_btn.pack()

#inp = input("Enter your password: ")
#pass_validator(inp)

tk.mainloop()
#imports
from tkinter import *
import os

#Main Screen
master = Tk()
master.title("Banking App 1.0")

#Image Import

#Functions
def register():
    #Vars
    temp_name=StringVar()
    temp_age=StringVar()
    temp_gender=StringVar()
    temp_password=StringVar()
    #Register Screen
    register_screen = Toplevel(master)
    register_screen.title('Register')
    register_screen.geometry('300x250')
    
    #Labels
    Label(register_screen, text="Please enter your details below to register", font=('Calibri',12)).grid(row=0,sticky=N)
    Label(register_screen, text="Name",font=('Calibri',12)).grid(row=1,sticky=W)
    Label(register_screen, text="Age",font=('Calibri',12)).grid(row=2,sticky=W)
    Label(register_screen, text="Gender",font=('Calibri',12)).grid(row=3,sticky=W)
    Label(register_screen, text="Password",font=('Calibri',12),show="*").grid(row=4,sticky=W)

    #Entries
    Entry(register_screen,text_variable=temp_name).grid(row=1)
    Entry(register_screen,text_variable=temp_age).grid(row=2)
    Entry(register_screen,text_variable=temp_gender).grid(row=3)
    Entry(register_screen,text_variable=temp_password,show="*").grid(row=4)

    #Register Button
    Button(register_screen,text="Register").pack
def login():
    print("Login Page")

#Labels
Label(master, text ="Banking Beta", font=('Calibri',14)).grid(row=0, sticky=N, pady=10)
Label(master, text="the most secure you've probably used", font=('Calibri',12)).grid(row=1, sticky=N)

#Buttons
Button(master, text="Login", font=('Calibri',12),width=20,command=login).grid(row=3, sticky=N)
Button(master, text="Register", font=('Calibri',12),width=20,command=register).grid(row=4, sticky=N, pady=10)

                                                                                         
master.mainloop()

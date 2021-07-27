from tkinter import *
import os

def delete2():
  screen3.destroy()

def delete3():
  screen4.destroy()

def delete4():
  screen5.destroy()

def help_section():
  global screen9
  screen9 = Toplevel(screen)
  screen9.title("Help")
  screen9.geometry("300x250")
  
  Label(screen9, text = """
  You typed help
  Please rerun this app after you are done reading the following
  1. type d - to deposit ammount
  2. type w - to withdraw ammount
  """).pack()
def transaction_hub():
  global screen7
  screen7 = Toplevel(screen)
  screen7.title("Transaction Hub")
  screen7.geometry("450x300")
  
  Label(screen7, text = """
  type h - help
  type d - deposit
  type w - withdrawl""").pack()
  enter_command = Entry(screen7, text = "")
  enter_command.pack()
  Button(screen7, text = "Done").pack()

  if enter_command == "h".lower():
    Button(screen7, text = "Help Page", command = help_section).pack()


def bank_account_code():
  global screen6
  screen6 = Toplevel(screen)
  screen6.title("Banking Application")
  screen6.geometry("300x250")
  Label(screen6, text = "Welcome to iBank").pack()
  Button(screen6, text = "Transaction Hub", command = transaction_hub).pack()

def session():
  global screen5
  screen5 = Toplevel(screen)
  screen5.title("Dashboard")
  screen5.geometry("400x400")
  Label(screen5, text = "Welcome to Dashboard").pack()
  Button(screen5, text = "Open Banking App", command = bank_account_code).pack()
  

def login_success():
  global screen3
  screen3 = Toplevel(screen)
  screen3.title("Success")
  screen3.geometry("150x100")
  Label(screen3, text = "Login success").pack()
  Button(screen3, text = "OK", command = delete2).pack()
  if login_success:
    session()   
def password_not_recognized():
  global screen4
  screen4 = Toplevel(screen)
  screen4.title("Error!")
  screen4.geometry("150x100")
  Label(screen4, text = "Password Not Recognized!").pack()
  Button(screen4, text = "OK", command = delete3).pack()


def user_not_found():
  global screen5
  screen5 = Toplevel(screen)
  screen5.title("Error!")
  screen5.geometry("150x100")
  Label(screen5, text = "User Not Recognized!").pack()
  Button(screen5, text = "OK", command = delete4).pack()

def register_user():
  username_info = username.get()
  password_info = password.get()

  file = open(username_info, "w")
  file.write(username_info + "\n")
  file.write(password_info)
  file.close()
  usernameEntry.delete(0, END)
  passwordEntry.delete(0, END)

  Label(screen1, text = "Registration successful", fg = "green", font = ("calibri", 11)).pack()
def login_verify():
  username1 = username_verify.get()
  password1 = password_verify.get()
  username_entry1.delete(0, END)
  password_entry1.delete(0, END)

  list_of_files = os.listdir()
  if username1 in list_of_files:
    file1 = open(username1, "r")
    verify = file1.read().splitlines()
    if password1 in verify:
      login_success()
    else:
      password_not_recognized()
  else:
    user_not_found()
def register():
  global screen1
  screen1 = Toplevel(screen)
  screen1.title("Register")
  screen1.geometry("300x250")

  global username
  global password
  global usernameEntry
  global passwordEntry
  username = StringVar()
  password = StringVar()

  Label(screen1, text = "Please enter details below").pack()
  Label(screen1, text = "").pack()
  Label(screen1, text = "Username * ").pack()
  usernameEntry = Entry(screen1, textvariable = username)
  usernameEntry.pack()
  Label(screen1, text = "Password * ").pack()
  passwordEntry = Entry(screen1, textvariable = password)
  passwordEntry.pack()
  Label(screen1, text = "").pack()
  Button(screen1, text = "Register", width = "10", height = "1", command = register_user).pack()

def login():
  global screen2
  screen2 = Toplevel(screen)
  screen2.title("Login")
  screen2.geometry("300x250")
  Label(screen2, text = "Please enter details below to login").pack()
  Label(screen2, text = "").pack()
  global username_verify
  global password_verify

  username_verify = StringVar()
  password_verify = StringVar()

  global username_entry1
  global password_entry1

  Label(screen2, text = "Username * ").pack()
  username_entry1 = Entry(screen2, textvariable = username_verify)
  username_entry1.pack()
  Label(screen2, text = "").pack()
  Label(screen2, text = "Password * ").pack()
  password_entry1 = Entry(screen2, textvariable = password_verify)
  password_entry1.pack()
  Label(screen2, text = "").pack()
  Button(screen2, text = "Login", width = 10, height = 1, command = login_verify).pack()


def mainScreen():
  global screen
  screen = Tk()
  screen.geometry("300x250")
  screen.title("Banking Application 1.0")
  Label(text = "Banking Application 1.0", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
  Label(text = "").pack()
  Button(text = "Login", height = "2", width = "30", command = login).pack()
  Label(text = "").pack()
  Button(text = "Register", height = "2", width = "30", command = register).pack()
  screen.mainloop()

mainScreen()

from tkinter import *
import os


def delete2():
  screen3.destroy()

def delete3():
  screen4.destroy()

def delete4():
  screen5.destroy()

def withdraw():
  screen7 = Toplevel(screen)
  screen7.title("Withdraw")
  screen7.geometry("400x250")

  Label(screen7, text = "Enter value of withdrawl").pack()
  ammount_of_withdrawl = Entry(screen7, text = "")
  ammount_of_withdrawl.pack()
  withdrawl_ammount = ammount_of_withdrawl.get()
  Button(screen7, text = "Done").pack()
  file2 = open("withdrawl_ammount.txt", "w")
  ammount_in_account_withdrawl = file2.read().splitlines()

def deposit():
  screen8 = Toplevel(screen)
  screen8.title("Deposit")
  screen8.geometry("400x250")

  Label(screen8, text = "Enter value of deposit").pack()
  ammount_of_deposit = Entry(screen8, text = "")
  ammount_of_deposit.pack()
  deposit_ammount = ammount_of_deposit.get()
  Button(screen8, text = "Done").pack()
  file3 = open("deposit_ammount.txt", "w")
  ammount_in_account_deposit = file3.read().splitlines()
  
def user_info():
  screen9 = Toplevel(screen)
  screen9.title("User Info")
  screen9.geometry("400x250")

def total():
  screen10 = Toplevel(screen)
  screen10.title("Total Ammount")
  screen10.geometry("300x250")
  
  Label(screen10, text = ammount_in_account_deposit - ammount_in_account_withdrawl).pack()
  
def bank_account_code():
  screen6 = Toplevel(screen)
  screen6.title("Transactions Hub - Banking App")
  screen6.geometry("400x300")

  Label(screen6, text = "Welcome to Transactions Hub. This is where you make all of your transactions.").pack()
  Label(screen6, text = "Balance: $0").pack()
  Button(screen6, text = "Withdraw", command = withdraw).pack()
  Button(screen6, text = "Deposit", command = deposit).pack()
  Button(screen6, text = "Total in Account", command = total).pack()
  
    
def session():
  global screen5
  screen5 = Toplevel(screen)
  screen5.title("Dashboard")
  screen5.geometry("400x400")
  
  Label(screen5, text = "Welcome to Dashboard").pack()
  Button(screen5, text = "Open Banking App", command = bank_account_code).pack()
  Button(screen5, text = "User Data", command = user_info).pack()
  

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

from tkinter import *
import os


def delete2():
  screen3.destroy()

def delete3():
  screen4.destroy()

def delete4():
  screen5.destroy()
  
def login_success():
  global screen3
  screen3 = Toplevel(screen)
  screen3.title("Success")
  screen3.geometry("150x100")
  Label(screen3, text = "Login success").pack()
  Button(screen3, text = "OK", command = delete2).pack()
  
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
  global genderEntry
  global ageEntry
  username = StringVar()
  password = StringVar()
  username_verify = StringVar()
  password_verify = StringVar()
  age_verify = StringVar()
  gender_verify = StringVar()
 

  Label(screen1, text = "Please enter details below").pack()
  Label(screen1, text = "").pack()
  Label(screen1, text = "Name * ").pack()
  usernameEntry = Entry(screen1, textvariable = username)
  usernameEntry.pack()
  Label(screen1, text = "Password * ").pack()
  global password_entry
  password_entry = Entry(screen1, text = "")
  password_entry.pack()
  Label(screen1, text = "").pack()
  Label(screen1, text = "Age * ").pack()
  age_entry = Entry(screen1, textvariable = age_verify)
  age_entry.pack()
  Label(screen1, text = "").pack()
  Label(screen1, text = "Gender * ").pack()
  gender_entry = Entry(screen1, textvariable = gender_verify)
  gender_entry.pack()
  Label(screen1, text = "").pack()
  Button(screen1, text = "Register", width = "10", height = "1", command = register_user).pack()

def login():
  global screen2
  screen2 = Toplevel(screen)
  screen2.title("Login")
  screen2.geometry("300x250")
  Label(screen2, text = "Please enter details below to login").pack()
  Label(screen2, text = "").pack()

  username_verify1 = StringVar()
  password_verify1 = StringVar()
  age_verify1 = StringVar()
  gender_verify1 = StringVar()
  
  global age_entry1
  global username_entry1
  global password_entry1
  global gender_entry1

  Label(screen2, text = "Name * ").pack()
  username_entry1 = Entry(screen2, textvariable = username_verify1)
  username_entry1.pack()
  Label(screen2, text = "").pack()
  Label(screen2, text = "Age * ").pack()
  age_entry1 = Entry(screen2, textvariable = age_verify1)
  age_entry1.pack()
  Label(screen2, text = "").pack()
  Label(screen2, text = "Gender * ").pack()
  gender_entry1 = Entry(screen2, textvariable = gender_verify1)
  gender_entry1.pack()
  Label(screen2, text = "").pack()
  Label(screen2, text = "Password * ").pack()
  password_entry1 = Entry(screen2, textvariable = password_verify1)
  password_entry1.pack()
  Label(screen2, text = "").pack()
  Button(screen2, text = "Login", width = 10, height = 1, command = login_verify).pack()


def mainScreen():
  global screen
  screen = Tk()
  screen.geometry("300x250")
  screen.title("Banking App")
  Label(text = "Banking App 1.0", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
  Label(text = "").pack()
  Button(text = "Login", height = "2", width = "30", command = login).pack()
  Label(text = "").pack()
  Button(text = "Register", height = "2", width = "30", command = register).pack()
  screen.mainloop()

mainScreen()

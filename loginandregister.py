from tkinter import *

def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info + ".txt", "w")
    file.write(username_info)
    file.write(password_info)

    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)

    Label(text = "Registration successful")
def register():
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
    print("Login session started")

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

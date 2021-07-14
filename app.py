from random import randint

#datatypes - strs, ints, lists, sets, dicts, bools
print("Hello World")

isHot = False
isCold = True
if isHot:
    print("It's a hot day so drink plenty of water")
elif isCold:
    print("It's a cold day so wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")

house_price_for_good_credit = 1000000 * .1
house_price_for_bad_credit = 1000000 * .2
goodCredit = False
if goodCredit:
    print(f"Your down payment is ${house_price_for_good_credit}")
else:
    print(f"Your down payment is ${house_price_for_bad_credit}")

good_credit = True
highIncome = False
if good_credit and highIncome:
    print("Eligible for loan")
else:
    print("NOT eligible for loan")

has_good_credit = False
has_high_income = False
if has_high_income or has_good_credit:
    print("Eligible for loan")
else:
    print("NOT eligible for loan")

hgc = True
has_criminal_record = False
if hgc and not has_criminal_record:
    print("Eligible for loan")
else:
    print("NOT eligible for loan")

temp = int(input("Enter the temperature: "))
if temp >= 30:
    print("It's a hot day")
elif temp <= 10:
    print("It's a cold day")
else:
    print("It's neither hot nor cold")

name = input("Enter your name: ")
if len(name) < 3:
    print("Name must be 15 characters. Please try again.")
elif len(name) > 50:
    print("Name must be 15 characters. Please try again.")
else:
    print("Thank You for entering your real name.")

weight = float(input("Enter your weight: "))
kg_or_pounds = input("(K)g or (L)bs: ")
if kg_or_pounds.upper() == "L":
    print(weight * 0.45)
elif kg_or_pounds.upper() == "K":
    print(weight * 2.20)
else:
    print("I'm sorry but I don't understand that")

#while condition is true:
#  ...
i = int(input("Enter a number:"))
while i >= 5:
   print("This number is greater than or equal to 5.")
else:
   print("This number is not greater than or equal to 5")
print("Done")

i = 1
while i >= 5:
    print(i)
    i = i + 1
print("Done")

secretNumber = int(input("Host, please enter a secret number: "))
guessCount = 0
guessLimit = 3
while guessCount < guessLimit:
    guess = int(input("Guess: "))
    guessCount += 1
    if guess == secretNumber:
        print("You won!")
        break
else:
    print("Sorry, you failed!")

command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif command == 'help':
        print("""
start - to start the car
stop - stop the car
quit - to quit""")
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand.")

for item in 'Python':
    print(item)

for nums in range(12):
    print(nums)

for num in range(5, 10):
    print(num)

for numers in range(5, 10):
    print(numers)

prices = [10, 20, 30, 40]
total = 0
for price in prices:
    total += price
print(f"Total: ${total}")

print("Hello World")

#while loop
i = 1
while 5 > i:
  print("*")
  i = i + 1

#for loop
sum = 0
for i in range(101):
  if i % 2 == 0:
    sum += i
print(sum)

#factorials
def factorial(num):
  product = 1
  while num > 0:
    product *= num
    num -= 1
  print(product)

factorial(int(input("Enter a number:\t")))

nums = [5, 92, -5, 1, 2 ]
sum = 0
min = nums[0]
max = nums[0]

for num in nums:
  sum += num
  if num > max:
    max = num
  if num < min:
    min = num
print(sum)
print(max)
print(min)

def displayList(table):
  for array in table:
    for element in array:
      print(element, end = "\t")
    print()
table = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

table[1][0] = 100
displayList(table)

i = 0
for subarray in table:
  total = sum(subarray)
  minVal = min(subarray)
  maxVal = max(subarray)
  avg = total / len(subarray)
  print("Row:\t", i, "Information")
  print("Sum:\t", i, "Information")
  print("Min:\t", i, "Information")
  print("Max\t:", i, "Information")
  print("Average\t:", i, "Information")
  i += 1

rows = 10
collumns = 10
grid = [[0] * rows] * collumns

for row in range(rows):
    for collumn in range(collumns):
        grid[row][collumn] = randint(0, 10)
        print(grid[row][collumn], end = "")
    print()

#Day 2 Homework

list = [[1, 2, 3, 6, 9, 10], [11, 15, 19, 100]]

def function():
  sum(list) / len(list)

function()

logins = {
"California_51":"Welcome",
"Amazing_Spiderman":"1234"
}

#Dictionaries
print(logins)
#logins.pop("Amazing_Spiderman")
print(logins)
logins.update({"Aaditya123" :
"mynameisaaditya"})
print(logins)
print(logins.keys())
print(logins.values())
print(logins.get("Amazing_Spiderman"))
print(logins["Amazing_Spiderman"])

for element in logins:
  print(element)

for element in logins:
  print(logins[element])

grades = {
    "Science" : "96",
    "Math" : "100",
    "English" : "100",
    "History" : "86"
}

min = grades["Science"]
for element in grades:
    if element < min:
        min = element

print(min)

profile = {
    "Username" : "Aaditya Kabra",
    "Password" : "mynameisaaditya",
    "Follower_Count" : "400000",
    "Following_Count" : "10"
}

def displayDetails():
    print(profile["Username"])
    print(profile["Password"])
    print(profile["Follower_Count"])
    print(profile["Following_Count"])
displayDetails()

#Bank Account Code 
createdAccountusername = input("Enter username that you want to create:\t")
createdAccountpassword = input("Enter password that you want to create:\t")


class bankAccount:
    def __init__(self, money_in_account, withdrawl, deposit, username, password, ammount_of_deposit,
                 ammount_of_withdrawl, balance):
        self.money_in_account = money_in_account
        self.withdrawl = withdrawl
        self.deposit = deposit
        self.username = username
        self.password = password
        self.ammount_of_deposit = ammount_of_deposit
        self.ammount_of_withdrawl = ammount_of_withdrawl
        self.balance = balance

    ammount_of_deposit = int(input("How much do you want to deposit:\t"))
    ammount_of_withdrawl = int(input("How much do you want to withdrawl:\t"))
    username = input("Enter username:\t")
    password = input("Enter password:\t")
    money_in_account = 0
    balance = money_in_account + ammount_of_deposit - ammount_of_withdrawl
    passwordChecker = len(createdAccountpassword) > 10
    one_more_password_check = createdAccountpassword != createdAccountusername
    finalBalance = f"Remaining Ammount: ${balance}"
    how_many_times = 0

    while passwordChecker and one_more_password_check is True:
        while createdAccountusername != username and createdAccountpassword != password and balance > ammount_of_withdrawl:
            print("Either username or password is not correct. Please try again.")
            username = input("Enter username:\t")
            password = input("Enter password:\t")
            if createdAccountusername == username and createdAccountpassword == password:
                print("""
        Intiallalizing...
        Loading Account...
        Account Balance = $0
        """)
            transaction = input("""
        make a deposit - d
        make a withdrawl - w
        Enter transaction:\t
        """)
            ammount_of_deposit = int(input("How much do you want to deposit:\t"))
            ammount_of_withdrawl = int(input("How much do you want to withdrawl:\t"))
            balance = money_in_account + ammount_of_deposit - ammount_of_withdrawl
            if transaction.lower == "w" and ammount_of_withdrawl <= balance:
                print("Transaction succesful")
            elif transaction.lower() == "w" and ammount_of_withdrawl > balance:
                print("Sorry but you don't have that much money in your account!")
                break
            else:
                print("Error please try again")
        while how_many_times < 1:
            print(finalBalance)
            print("Thank You for doing your transaction with iBank!")
            how_many_times += 1
    else:
        print("Error! Password and Username are same!")






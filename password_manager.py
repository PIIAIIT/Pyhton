# PASSWORD MANAGER

import sqlite3
import function
import os

ADMIN_PASSWORD = "admin"
connect = input("Enter your password: ")

while connect != ADMIN_PASSWORD:
    connect = input("Enter your password: ")
    if connect == 'q':
        break
    os.system("cls")

conn = sqlite3.connect('database.db')
c = conn.cursor()
print(conn)

while True:
    print("\nWelcome to the Password Manager by PIIAIIT\n")
    print("Commands:\n")
    print("s = See all passwords")
    print("n = New password")
    print("d = Delete password")
    print("q = Quit")
    userInput = input("\nEnter command: ")

    if userInput == "s":
        conn = sqlite3.connect('Daten/database.db')
        c = conn.cursor()
        function.search_all()
    elif userInput == "n":
        conn = sqlite3.connect('Daten/database.db')
        c = conn.cursor()
        function.create_password()
    elif userInput == "d":
        conn = sqlite3.connect('Daten/database.db')
        c = conn.cursor()
        function.delete_password()
    elif userInput == "q":
        print("Bye Bye")
        break

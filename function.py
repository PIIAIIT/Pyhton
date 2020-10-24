import sqlite3
import os

conn = sqlite3.connect('Daten/database.db')
c = conn.cursor()


def search_all():
    conn = sqlite3.connect('Daten/database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM passwords")

    result = c.fetchall()
    for rows in result:
        print(rows)

    conn.close()
    input("Press Enter to Exit")
    os.system("cls")
    return


def create_password():

    website = input("Enter website: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    c.execute("""INSERT INTO passwords
    (website, username, password) VALUES
    (?, ?, ?)
    """, (website, username, password))

    conn.commit()

    c.execute("SELECT * FROM passwords ORDER BY id DESC LIMIT 1")

    result = c. fetchone()
    for row in result:
        print(row)
    conn.close()
    input("Press Enter to Exit")
    os.system("cls")
    return


def delete_password():
    conn = sqlite3.connect('Daten/database.db')
    c = conn.cursor()
    print(conn)
    decision = input("How do you want to delete your passsword (website, username) ")
    os.system("cls")

    if decision == "website":
        print("\nYou are deleting your passwords by website name")
        user_input = input("Enter website: ")

        c.execute("""DELETE FROM passwords
            WHERE website = ?
            """, (user_input,))
        print("Your password has now been deleted")
    elif decision == "username":
        print("\nYou are deleting your passwords by username")
        user_input = input("Enter username: ")

        c.execute("""DELETE FROM passwords
                    WHERE username = ?
                    """, (user_input,))
        print("Your password has now been deleted")

    conn.commit()
    conn.close()
    input("Press Enter to Exit")
    os.system("cls")
    return

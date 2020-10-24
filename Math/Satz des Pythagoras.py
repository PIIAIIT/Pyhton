import math
from tkinter import *

root = Tk()
root.title('Math Program')



def Satz_des_Pythagoras():
    while True:
        print("============================================")
        sr = input('What are you searching for? (a/b/c)')
        try:
            if sr == 'a':
                b = float(input('What is b?'))
                c = float(input('What is c?'))
                print(math.sqrt((c ** 2) - (b ** 2)))


            elif sr == 'b':
                a = float(input('What is a?'))
                c = float(input('What is c?'))
                print(math.sqrt((c ** 2) - (a ** 2)))

            elif sr == 'c':
                a = float(input('What is a?'))
                b = float(input('What is b?'))

                print(math.sqrt((a ** 2) + (b ** 2)))

            elif sr == 'Quit':
                print("See you next time!")
                break

            else:
                print("Error you need to type in a, b or c!")
        except ValueError:
            print("You cannot sqrt root a negative number!")
Satz_des_Pythagoras()
print("============================================")

root.mainloop()
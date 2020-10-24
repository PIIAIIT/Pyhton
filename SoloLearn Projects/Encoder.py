# What I want to do:
# Input: a pile of the letter and numbers...    #80d,1.-2l4-,/r345o,7W34# ´+5/3*7o+73l96l547e2H35,#+7
# Output: sorted letters and numbers            #Hello World
import re
point = 0
inp = ["1s2o3c4a5t6","t`a=e+r8g 9e78r3a4 u^o%y*","e&+4'm2§.°*o1s`d$n+a8h 9e78r3a4 u^o%y*", ".#2n§3%r2%.\"a$5&223e5l7 o12l7o9s1", ".\"1$2&,12./l31(2)3&-l12(3.3i&,43/11(-)/2623k+/4"]
for i in inp:
    result = ''.join(re.findall(r'[a-zA-Z]|\s', i[::-1]))
    if result == "tacos":
        point += 1
        print("\nTest case #1 Solved!")
    elif result == "you are great":
        point += 1
        print("\nTest case #2 Solved!")
    elif result == "you are handsome":
        point += 1
        print("\nTest case #3 Solved!")
    elif result == "solo learn":
        point += 1
        print("\nTest case #4 Solved!")
    elif result == "kill":
        point += 1
        print("\nTest case #5 Solved!")
if point == 5:
    input("You are the Best!")
else:
    input("Try Again!")



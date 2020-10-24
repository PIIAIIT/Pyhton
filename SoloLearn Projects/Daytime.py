# INPUT
#November 19, 2019
#11/19/2019
# OUTPUT
# 19/11/2019
inp = input().replace(",","")
month = inp.split(" ")[0]

new_month = 0

if month == "Januar":
    new_month = 1
elif month == "Februar":
    new_month = 2
elif month == "März":
    new_month = 3
elif month == "April":
    new_month = 4
elif month == "Mai":
    new_month = 5
elif month == "Juni":
    new_month = 6
elif month == "Juli":
    new_month = 7
elif month == "August":
    new_month = 8
elif month == "September":
    new_month = 9
elif month == "Oktober":
    new_month = 10
elif month == "November":
    new_month = 11
elif month == "Dezember":
    new_month = 12

try:
    anwser1 = inp.split(" ")[1] + "/" + str(new_month) + "/" + inp.split(" ")[2]
    print(anwser1)
except IndexError:
    print(inp.split("/")[1] + "/" + inp.split("/")[0] + "/" + inp.split("/")[2])
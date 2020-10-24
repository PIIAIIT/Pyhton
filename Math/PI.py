import math

def Flacheninhalt(r):
    return math.pi * r ** 2

def Umfang(r):
    return math.pi * r * 2

def Kreisbogen(r, winkel):
    return math.pi * r * (winkel/180)

def Kreissektor(r, winkel):
    return math.pi * r ** 2 * (winkel/360)

def Kugel_Oberflaeche(r):
    return 4 * math.pi * r ** 2

def Kugel_Vol(r):
    return 4/3 * math.pi * r ** 3

while True:
    Figur = input("Ist deine Figur ein Kreis oder eine Kugel? ")
    if Figur == "Kugel" or Figur == "Kreis":
        stat = True if Figur == "Kugel" else False
    elif Figur == "quit":
        break
    else:
        print("Das ist weder Kreis noch Kugel!")
        break
    try:
        rad = int(input("What is your Radius? "))
        if rad == "quit":
            break
    except ValueError:
        print("Das ist keine Nummer.\nBitte nochmal versuchen!")
        rad = int(input("Was ist der Radius? "))
        if rad == "quit":
            break

    durchmesser = rad * 2
    Winkel = int(input("Winkel? (Nur für Bogen, Sektor und Sehne. Sonst 0) "))
    if Winkel == "quit":
        break

    # Print Ausgaben!!!

    print(f"Der Flächeninhalt beträgt: {Flacheninhalt(rad)} cm³")
    print(f"Der Umfang beträgt: {Umfang(rad)} cm²")
    print(f"Der Kreisbogen beträgt: {Kreisbogen(rad,Winkel)} cm") if Winkel != 0 else False
    print(f"Der Kreissektor beträgt: {Kreissektor(rad,Winkel)} cm²") if Winkel != 0 else False
    print(f"Die Oberfläche der Kugel beträgt: {Kugel_Oberflaeche(rad)} cm³") if stat == True else False
    print(f"Der Volumen der Kugel beträgt: {Kugel_Vol(rad)} cm³") if stat == True else False
    print("==============================================")

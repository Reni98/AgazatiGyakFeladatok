szam=int(input("Adj meg egy számot:"))

if szam % 3 == 0 and szam < 40:
    print("A szám osztható 3-al és kisebb,mint 40")

elif szam % 3 == 0 and szam > 40:
        print("A szám osztható 3-al és nagyobb,mint 40")
else:
      print("A szám nem osztható 3 al.")

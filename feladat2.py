import random
sportok = ["foci", "kézilabda", "úszás"]
sport=input("Adj meg egy sportágat: ").lower()
# for s in sportok:
#     if s == sport:
#         print("Benne van a sportág a listában.")
#     else:
#         print("Nincs benne a sportág a listában.")

if sport in sportok:
    print("Benne van a sportág a listában.")
else:
    print("Nincs benne a sportág a listában.")


print(f"A sportágak száma a listában: {len(sportok)}")
sportok.sort()
print(';'.join(i for i in sportok))
random.shuffle(sportok)
print(f"A lista első eleme: {sportok[0]}")
print(f"A lista utolsó eleme: {sportok[-1]} ")


nevek = ["Béla", "Csilla", "Dóra"]

bekeres_szama=int(input("Hány új nevet szeretnél hozzáadni?: "))

for i in range(bekeres_szama):
    nev=input("Add meg a nevet:")
    nevek.append(nev)

print(f"A nevek száma a listában: {len(nevek)}")
print(';'.join(i for i in nevek))
nevek.sort()
print(f"A rendezett lista első eleme: {nevek[0]}")
nevek.pop()
print("Az utolsó elem eltávolítva.")
#Ellenőrzés:
# print(';'.join(i for i in nevek))

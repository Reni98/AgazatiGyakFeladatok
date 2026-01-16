class Fovarosok:
    def __init__(self,fajl):
        self.fajl=fajl

    def beolvas(self):
        fovarosok_lista=[]
        with open("fovarosok.txt","r", encoding='utf-8') as f:
            sorok=f.readlines()

            for s in sorok[1:]:
                adatok=s.strip()
                adat=adatok.split(";")

                orszag=adat[0]
                fovaros=adat[1]
                lakossag=int(adat[2])
                terulet=int(adat[3])
                gdp=int(adat[4])
                epulet_nev=adat[5]
                magassag=int(adat[6])

                fovarosok_lista.append([orszag,fovaros,lakossag,terulet,gdp,epulet_nev,magassag])
        return fovarosok_lista
    
    def kiir(self,lista):
        for l in lista:
            print(f"{l[0]}; {l[1]}; {l[2]}; {l[3]}; {l[4]}; {l[5]}; {l[6]}")

    def legnagyobbterulet(self,lista):
        legnagyobb_terulet=0
        varos=""
        for l in lista:
            if l[3]> legnagyobb_terulet:
                legnagyobb_terulet=l[3]
                varos=l[1]

        print(f"Legnagyobb területű főváros neve: {varos},területe:{legnagyobb_terulet} ")
    
    def legkisebbgdp(self,lista):
        legkisebb=float('inf')
        varos=""
        for l in lista:
            if l[4]<legkisebb:
                legkisebb=l[4]
                varos=l[1]
        print(f"Legkisebb GDP város neve: {varos}, GDP: {legkisebb}")
    def legmagasabbEpulet(self,lista):
        legmagasabb=0
        epulet=""
        for i in lista:
            if i[6]> legmagasabb:
                legmagasabb=i[6]
                epulet=i[5]

        print(f"A legmagasabb épület neve: {epulet}, magasság: {legmagasabb}")

    def orszagok(self, lista):
        orszagok_lista=[]
        for i in lista:
            orszagok_lista.append(i[0])
        print(f";".join(f for f in orszagok_lista))

    def fovaros_megszamol(self, lista):
        print(f"Fővárosok száma: {len(lista)}")

    def fajlbaír(self,lista):
        legnagyobb=0
        varos=""
        for l in lista:
            if l[4]>legnagyobb:
                legnagyobb=l[4]
                varos=l[1]
        print(f"Legnagyobb GDP város neve: {varos}, GDP: {legnagyobb}")

        with open("legjobb_gdp.txt","w",encoding='utf-8') as fajl:
            fajl.write(f"Legnagyobb GDP város neve: {varos}, GDP: {legnagyobb}")

peldany=Fovarosok("feladat_fovarosok.txt")
fovarosok_lista=peldany.beolvas()
peldany.kiir(fovarosok_lista)
peldany.legnagyobbterulet(fovarosok_lista)
peldany.legkisebbgdp(fovarosok_lista)
peldany.legmagasabbEpulet(fovarosok_lista)
peldany.orszagok(fovarosok_lista)
peldany.fovaros_megszamol(fovarosok_lista)
peldany.fajlbaír(fovarosok_lista)
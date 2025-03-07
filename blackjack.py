from random import shuffle
def suma_kart(karty):#jesli as to daje najlepszą sumę
    s=0
    for karta in karty:
        if karta=='A':
            if s+11>21:
                s+=1
            else:
                s+=11
        else:
            s+=karta
    return s
def wymieszane_talie(ilosc_talii):
    tab=[]
    for nr_talii in range(ilosc_talii):
        for kolor in ["pik","kier","karo","trefl"]:
            for numer_karty in range(2,11):
                tab.append(numer_karty)
            for figury in range(3):
                tab.append(10)
            tab.append('A')
    shuffle(tab)
    return tab
def ruch_krupiera(tab):
    karty_krupiera=[]
    for i in range(2):
        karty_krupiera.append(tab.pop())
    if 'A' in karty_krupiera and 10 in karty_krupiera:
        return "WYGRANA_KRUPIERA"
    return karty_krupiera#odkryta_karta_krupiera
def dobieranie_krupiera(tab,jego_karty):#zwraca punkty ktore krupier zdobyl
    jest_as=jego_karty.count('A')
    aktualna_suma=suma_kart(jego_karty)
    while aktualna_suma<17:
        jego_karty.append(tab.pop())
        aktualna_suma=suma_kart(jego_karty)
    print("karty_krupiera: ",jego_karty)
    print("Ilosc jego pkt: ",aktualna_suma)
    return aktualna_suma
def gra(tab):
    print()
    print("=====NOWA GRA=====")
    print()
    twoje_karty=[]
    for i in range(2):
        twoje_karty.append(tab.pop())
    karty_krupiera=ruch_krupiera(tab)
    if karty_krupiera[0]=="WYGRANA_KRUPIERA":
        print("Przegrałeś")
    print("Początkowa karta krupiera to:",karty_krupiera[0])
    suma=suma_kart(twoje_karty)
    while True:
        print("To twoje karty: ",twoje_karty)
        print("Aktualna suma pkt wynosi: ",suma)
        if suma>21:
            print("Frajer jestes i tyle")
            return gra(tab)
        print("Co zamierzasz zrobić?")
        print("1.Hit 2.Stand")
        wybor=int(input())
        if wybor==1:
            nowa_karta=tab.pop()
            print("Pobrałeś: ",nowa_karta)
            twoje_karty.append(nowa_karta)
            suma=suma_kart(twoje_karty)
        elif wybor==2:
            print("==== Rozpoczęto dobieranie krupiera ====")
            pkt_krupiera=dobieranie_krupiera(tab,karty_krupiera)
            print("Suma pkt krupiera: ",pkt_krupiera)
            if pkt_krupiera>=suma and pkt_krupiera<22:
                print("Wygrywa krupier")
            else:
                print("WYGRYWASZ")
            return gra(tab)
tab=wymieszane_talie(1)
gra(tab)
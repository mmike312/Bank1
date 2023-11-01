from random import randint
import pickle

#clasele de obiecte
class Bank:
    def __init__(self, clienti, tranzactii):
        self.clienti = []
        self.tranzactii = []

class Clienti:
    def __init__(self, UID, nume_prenume):
        self.UID = UID
        self.nume_prenume = nume_prenume

class Tranzactii:
    def __init__(self, TID, UID, suma, tip, zi):
        self.TID = TID
        self.UID = UID
        self.suma = suma
        self.tip = tip
        self.zi = zi

    def modSuma(self,x):
        self.suma = x
    
    def modZi(self,x):
        self.zi = x

    def modTip(self, x):
        self.tip = x


#interfata
def meniu():
    print("#########################################################")
    print("1 - Aduga")
    print("2 - Sterge")
    print("3 - Cautare")
    print("4 - Genereaza raport")
    print("5 - Filtreaza")
    print("6 - Undo")
    print("7 - Exit")
    print("#########################################################")

def meniu1():
    print("#########################################################")
    print("1 - Adauga o tranzactie noua")
    print("2 - Adauga un nou client")
    print("3 - Actualizeaza o treanzactie existenta")
    print("4 - Inapoi la meniul pricipal")
    print("#########################################################")

def meniu2():
    print("#########################################################")
    print("1 - Sterge tranzactie")
    print("2 - Sterge client")
    print("3 - Sterge toate tranzactiile din data:")
    print("4 - Sterge toate tranzactiile din perioada:")
    print("5 - Sterge tranzactiile de tip:")
    print("6 - Inapoi la meniul pricipal")
    print("#########################################################")

def meniu3():
    print("Cautare tranzactii:")
    print("#########################################################")
    print("1 - Afiseaza tranzactiile cu sume mai mari de o suma x")
    print("2 - Soldul la data zz:luna:an")
    print("3 - Inapoi la meniul pricipal")
    print("#########################################################")

def meniu4():
    print("Generează raport:")
    print("#########################################################")
    print("1 - Suma totala a tranzactiilor de tipul y")
    print("2 - Soldul unui cont la data zi:luna:an")
    print("3 - Toate tranzactiile de tipul y in ordine descrescatoare a sumei")
    print("4 - Inapoi la meniul pricipal")
    print("#########################################################")

def meniu5():
    print("ACe ai vrea sa filtrezi?")
    print("#########################################################")
    print("1 - Afiseaza clienti")
    print("2 - Filtreaza tranzactii")
    print("3 - Inapoi la meniul pricipal")
    print("#########################################################")
def meniu52():
    print("Alege filtru:")
    print("#########################################################")
    print("1 - Elimina tranzactiile mai mici de x lei")
    print("2 - Elimina tranzactiile de tipul y")
    print("3 - Inapoi la selectia cliienti / tranzactii")
    print("#########################################################")

def meniu6():
    print("#########################################################")
    print("1 - Sterge ultima tranzactie")
    print("2 - Inapoi la meniul pricipal")
    print("#########################################################")

def meniuModifica():
    print("#########################################################")
    print("1 - Modifica suma")
    print("2 - Modifica tipul")
    print("3 - Modifica data")
    print("4 - Meniul precedent")
    print("#########################################################")

def logoBanca(): 
    print("       .  .  .   . .      .            ..    .       .  .")
    print(" ..          .        .  .               .     .        .")
    print(".  .     .   .          ....:...     . . .    . .       .")
    print("     .                ..-**+=+**-..      .        .      ")
    print(" .   ..    .      ..:+*+=::::::-=+*+:..                  ")
    print("         ...:::::+*+=-::==---=---::-=+*+::::::.        ..")
    print("      .....-=+*+=-:::::::::::::::::::::-=+*+=-.....  ....")
    print("      .-+++++++++++++++++++++++++++++++++++++++++=.      ")
    print("     ....----=------=---------------=------=----..       ")
    print(" .      .:-------------------------------------:.        ")
    print("     .  ..::====:::=++=.::+++++::.=+++:::=++=::..  .... .")
    print(".   . . ..:-=**=::=+*#+-:=+##*+=:-+##*=:-+##*=:..  .    .")
    print("        ..:-=++=::=+++=-:=+***+=:-+***=:-***+-:..      . ")
    print(".       ..:--:::::=-::-::=+===+=:-=====:-====-:..       .")
    print("  .  .  ..:-=---::=----::-=*#*+=::++++=:-++++-:..    .   ")
    print("    .   ..:-=**=::-+*#=:::+#%%*=::+##*=::+##*-:..   .    ")
    print("       ...:-=++=::-+++=:::++#**-::+***-::***+-:..   .  . ")
    print(".       .:::=---:::----:::+#%#*-::===+-::====:::..   .   ")
    print(" .      .+***************++%%%++***************+..  .    ")
    print("#########################################################")
    print()
    print(" ____    _    _   _  ____    _      _    _   _ ___ ")
    print("| __ )  / \  | \ | |/ ___|  / \    | |  | | | |_ _|")
    print("|  _ \ / _ \ |  \| | |     / _ \   | |  | | | || | ")
    print("| |_) / ___ \| |\  | |___ / ___ \  | |__| |_| || | ")
    print("|____/_/___\_\_|_\_|\____/_/_  \_\ |_____\___/|___|")
    print("           |  \/  |_ _| | | |  / \  |_ _|")                     
    print("           | |\/| || || |_| | / _ \  | | ")                   
    print("           | |  | || ||  _  |/ ___ \ | | ")                     
    print("           |_|  |_|___|_| |_/_/   \_\___|")          
    print()
    print()
#navigare meniuri

def navigareMeniuPrincipal(o):
    ok = False
    while ok == False:
        meniu()
        x = inputInt( int(1), int(7), "Alege o optiune: ")
        if x == 1:
            meniu1()
            navigareMeniuAdaugare(o)
        elif x == 2:
            meniu2()
        elif x == 3:
            meniu3()
        elif x == 4:
            meniu4()
        elif x == 5:
            meniu5()
            navigareMeniuFiltrare(o)
        elif x == 6:
            meniu6()
            navigareUndoUltimaTranzactie(o)
        elif x == 7:
            ok = True

def navigareMeniuAdaugare(o):
    ok = False
    while ok == False:
        x = inputInt( int(1), int(4), "Ce ai vrea sa adaugi? ")
        if x == 1:
            if len( o.clienti) > 0:
                adaugaTranzactie(o)
            else:
                print("Adauga cienti!!!")
        elif x == 2:
            adaugaUser(o)
        elif x == 3:
            o = actualizareTranzactie(o)
        elif x == 4:
            ok = True

def navigareMeniuStergere(o):
    ok = False
    while ok == False:
        x = inputInt( int(1), int(4), "Ce ai vrea sa adaugi? ")
        if x == 1:
            stergeTranzactie(o)
        elif x == 2:
            stergeUser(o)
        elif x == 3:
            stergeTranzactiiZi(o)
        elif x == 4:
            stergeTranzactiiPerioada(o)
        elif x == 5:
            stergeTranzactieTip(o)
        elif x == 6:
            ok = True

def navigareMeniuFiltrare(o):
    ok = False
    while ok == False:
        x = inputInt( int(1), int(3), "Alege ce ai vrea sa vizualizezi: ")
        if x == 1:
            afiseazaUseeri(o.clienti)
        elif x == 2:
            navigareMeniuFTranzactii(o)
        elif x == 3:
            ok = True

def navigareMeniuFTranzactii(o):
    ok = False
    meniu52()
    while ok == False:
        x = inputInt( 1, 3, "Aplica un filtru: ")
        if x == 1:
            filtreazaTranzaztiiSuma(o)
        elif x == 2:
            filtreazaTranzactiiTip(o)
        elif x == 3:
            ok = True

def navigareUndoUltimaTranzactie(o):
    meniu6()
    ok = False
    afiseazaTranzactii(o)
    while ok == False:
        x = inputInt(1, 2, "Alege o optiune: ")
        if x == 1:
            eliminaUltima(o)
        elif x == 2:
            ok = True




    

#aplicatia - main -

def app():
    dbfile = open('bank_db', 'rb')
    o = Bank( [], [])
    o = pickle.load(dbfile)
    logoBanca()
    navigareMeniuPrincipal(o)
    dbfile = open('bank_db', 'wb')
    pickle.dump(o, dbfile)


#input
def inputInt( i = None, s = None, mesaj = ""):
    """
        Cere input pana cand se itroduce o valoare valida, numar intreg
        La apelarea fara parametri:

        inputInt()

        La aperlarea cu parametri:
        
        inputInt( limita inferioara a numarului valid, limita superioara a numarului valid), mesajul afisat la input)
    """
    ok = False
    x = None
    while ok == False:
        x = input(mesaj)
        try:
            x = int( x)
        except:
            print("Introdu un numar natural care sa corespunda unei optiuni din meniu!!!")
        c = int( 9)
        if type(x) == type(c):
            if i != None and  s!= None:
                if i > x or x > s:
                    print("Introdu un numar cuprins intre", i, "si", s, "!!!")
                else:
                    ok = True
            else:
                return True
    return int(x)  

def introduData():
    an = inputInt( 0, 2023, "Introdu anul ")
    if an % 4 == 0 and an % 100 == 0 and an % 400 != 0:
        luna = inputInt( 1, 12, "Luna: ")
        if luna == 1 or luna == 3 or luna == 5 or luna == 7 or luna == 8 or luna == 10 or luna == 12:
            zi = inputInt(1, 31, "Ziua: ")
        elif luna == 2:
            zi = inputInt(1, 29, "Ziua: ")
        else:
            zi = inputInt(1, 30, "Ziua: ")
    else:
        luna = inputInt( 1, 12, "Luna: ")
        if luna == 1 or luna == 3 or luna == 5 or luna == 7 or luna == 8 or luna == 10 or luna == 12:
            zi = inputInt(1, 31, "Ziua: ")
        elif luna == 2:
            zi = inputInt(1, 28, "Ziua: ")
        else:
            zi = inputInt(1, 30, "Ziua: ")
    return (zi, luna, an)

def stringInput( lmic, lmare, mesaj, mesaj2):
    ok = False
    while ok == False:
        x = input(mesaj)
        if len(x) <= lmare and len(x) >= lmic:
            ok = True
        else:
            x = input(mesaj2)
    return x


#actualizare tranzactie

def actualizareTranzactie(o):
    afiseazaTranzactii(o)
    user = selecteazaUser(o.clienti)
    afiseazaTranzatiileUserului( user, o)
    tranz = selecteazaTranzactie(o.tranzactii)
    for i in o.tranzactii:
        if i.TID == tranz:
            meniuModifica()
            modificaTranz(i)
    return o
            
def modificaTranz(o):
    ok = False
    while ok == False:
        x = inputInt(1, 4, "Alege modificarea pe care vrei sa o faci: ")
        if x == 1:
            suma = inputInt(1, 100000, "Introdu suma noua: ")
            o.modSuma(suma)
        elif x == 2:
            tip = input("Tipul tranzactiei: ")
            o.modTip(tip)
        elif x == 3:
            data = introduData()
            o.modZi(data)
        elif x == 4:
            ok = True


#afisare

def afiseazaUseeri(o):
    print("\n+------+-------------------------------+")
    for i in o:
        print("|",i.UID,"|",i.nume_prenume )
        print("+------+-------------------------------+")
    print()

def afiseazaTranzactii(o):
    print("LISTA TUTUROR TRANZACTIILOR EFECTUATE:")
    print("\n+------+------+------------------+-----------------------+---------------------+")
    for i in o.tranzactii:
        print("|", i.UID, "|", i.TID, "|", i.zi, "|", i.tip, "|", i.suma, "|")
        print("+------+------+------------------+-----------------------+---------------------+")
    print()

def afiseazaTranzatiileUserului(id, o):
    """
    Afiseaza tranzactiile unui user transmis prin ID
    """
    print("\n+------+------+------------------+-----------------------+---------------------+")
    for i in o.tranzactii:
        if i.UID == int(id):
            print("|", i.UID, "|", i.TID, "|", i.zi, "|", i.tip, "|", i.suma, "|")
            print("+------+------+------------------+-----------------------+---------------------+")
    print()


#cautari
def cautaSumeGTX(o):
    pass 

def cautaTranzactiileDinDataXMaiMariDeY(o):
    pass

def cautaTranzactiileTip(o):
    pass


#filtrare
def filtreazaTranzactiiTip(o):
    """
    afiseaza tranzactiile de tipul introdus
    """
    x = stringInput(3, 20, "Introdu tipul de tranzactie pe care vrei sa le filtrezi: ", "Limita este de minim 3, maxim 20 de caractere: ")        
    ok = False
    print("\n+------+------+------------------+-----------------------+---------------------+")
    for i in o.tranzactii:
        if i.tip != x:
            print("|", i.UID, "|", i.TID, "|", i.zi, "|", i.tip, "|", i.suma, "|")
            print("+------+------+------------------+-----------------------+---------------------+")
            ok = True

    if ok != True:
        print("NU EXISTA TRANZACTII DE TIPUL", x)
    print()

def filtreazaTranzaztiiSuma(o):
    """
    afiseaza tranzactiile cu suma mai mare de cea introdusa
    """
    x = inputInt(1, 1000000, "Suma minima a tranzactiilor: ")
    print("\n+------+------+------------------+-----------------------+---------------------+")
    for i in o.tranzactii:
        if i.suma >= x:
            print("|", i.UID, "|", i.TID, "|", i.zi, "|", i.tip, "|", i.suma, "|")
            print("+------+------+------------------+-----------------------+---------------------+")
    print()


#rapoarte

def raportSumaTotala(o):
    pass

def raportContUser(o):
    pass

def raportTranzDeAcelasiTipDupaSuma(o):
    pass


#adaugari

def adaugaUser(o):
    """
    adauga un utilizator, care e carcaterizat de un id si nume_prenume
    """
    x = genereazaUID(o.clienti)
    np = stringInput( 3, 20, "Nume si prenume client nou: ", "Limita este de minim 3, maxim 20 de caractere: ")
    cl = Clienti(x, np)
    try:
        o.clienti.append(cl)
        return True
    except:
        return False

def adaugaTranzactie(o):
    """
    adauga io tranzactie caracterizata de un id propriu, de id-ul utilizatorului, data, suma , tip
    """
    x = genereazaTID(o.tranzactii)
    afiseazaUseeri(o.clienti)
    user = selecteazaUser(o.clienti)
    data = introduData()
    tip = input("Tipul tranzactiei: ")
    suma = inputInt(1, 100000, "Introdu suma: ")
    tr = Tranzactii( x, user, suma, tip, data)
    try:
        o.tranzactii.append(tr)
        return True
    except:
        return False

#stergeri

def stergeTranzactie(o):
    pass

def stergeUser(o):
    pass

def stergeTranzactiiZi(o):
    pass

def stergeTranzactiiPerioada(o):
    pass

def stergeTranzactieTip(o):
    pass

def eliminaUltima(o):
    x = input("Easti sigur ca vrei sa anulezi ultima tranzactie? ( DA / NU )")
    if x == "DA":
        o.tranzactii.pop()
        print("Tranzactie anulata cu succes!!!")
    

#diverse

def selecteazaUser(o):
    """
    selecteaza un user din lisa de useri prin introducerea unui ID valid
    """
    ok = False
    while ok == False:
        x = inputInt(1000, 9999, "Selecteaza cleintul care vrea sa realizeze tranzactia ")
        for i in o:
            if int(x) == int(i.UID):
                ok = True
                n = i.nume_prenume
        if ok == False:
            print("Introdu un ID valid!!!", i.UID, type( i.UID))
        else:
            print("Userul", x, "a fost selectat cu succes")
        return x
 
def selecteazaTranzactie(o):
    """
    selecteaza o tranzactie dein lista de tranzactii pe baza unui id de tranzactie
    """
    ok = False
    while ok == False:
        x = inputInt(1000, 9999, "Selecteaza tranzactia pe care vreti sa o modificati: ")
        for i in o:
            if int(x) == int(i.TID):
                ok = True
        if ok == False:
            print("Introdu un ID valid!!! ")
        else:
            print("Tranzactia cu ID", x, "a fost selectata cu succes")
    return x


def genereazaUID(l_clienti):
    """
    genereaza ID-uri de 4 cifre cat pana cand 
    se gaseste unul nou, unic in lista de clienti
    """
    ok = False
    while ok == False:
        x = randint(1000, 9999)
        ok = True
        for i in l_clienti:
            if i.UID == x:
                ok = False
    return x

def genereazaTID(l_clienti):
    """
        genereaza ID-urid e 4 cifre cat pana cand 
        se gaseste unul nou, unic in lista de tranzactii
    """
    ok = False
    while ok == False:
        x = randint(1000, 9999)
        ok = True
        for i in l_clienti:
            if i.TID == x:
                ok = False
    return x


#teste

app()
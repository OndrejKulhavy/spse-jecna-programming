"""
Nyní už umíte naprgramovat corutine, která vrací výstupy pomocí yield. Jak ale dostat do coroutine vstupy? Konkrétně třeba do druhého volání, nebo do třetího?

Zkusme uvážit tuto corutine:

def pozdrav():
    print("Zadej jmeno:")
    jmeno = yield

    print("Tve jmeno je "+ str(jmeno))
    yield

    print("Nazdar " + str(jmeno))
    yield
A nyní si rozeberme. Jmenuje se pozdrav(). Má tři části. V první části vypíše abyste zadal/a jméno a čeká na vstup, na to je speciální (yield) v závorkách. Ve třetí části napíše jaké mé jméno a přeruší se. V té poslední pak pozdraví a opět se přeruší. Lze ji tedy zavolat (iterovat 3x). Po čtvrté už by vyhodila vyjímku.

Zkusme se podívat jak se v Pythonu 3 taková corutine ovládá. Je to trochu divné, ale je to tak:

corutina1 = pozdrav()       #nastartuje corutinu
next(corutina1)             #spusti prvni cast
corutina1.send("Ondra")     #spusti druhou cast, ktera ocekava data
next(corutina1)             #spusti treti cast
corutina1.close()           #ukonci corutinu
Ano. Je to definitivně divné. Spíš jako připojení do databáze, nebo k sítí. Na začátku nastavím spojení. Na konci ho close(). Ono je to tak, corutina je živá a žije si paralerně s hlavním programem. Když ji chci spustit tak ji iteruji. Jako iterátor přes next() a když ji chci poslat nějakou hodnotu tak je přes send().

Váš úkol je nyní, inspirovat se v tomhle kódu, a přepracovat úlohu 9.7, kde je vydej_obedu() tak aby pracovala takto:

Nejprve vrátí nápoj
Pak zjistí, zda-li je zvoleno jídlo A nebo B
Podle toho vypíše jídlo A nebo B. (Ta jídla si tam musíte přidat, třeba B může být řízek s kaší.
"""

def catch_your_lunch():
    napoj = yield
    yield f"Dostanete: {napoj}"

    volba = yield
    yield f"Vybráno jídlo: {volba}"

    if volba == "A":
        jidlo = ["polévka česneková s bramborem", "segedínský guláš, houskové knedlíky", "jablko"]
    else:
        jidlo = ["polévka česneková s bramborem", "kaše s bramborem", "hruška"]

    yield f"Jídlo: {jidlo}"

    yield "Konec"

corutina1 = catch_your_lunch()   # nastartuje corutinu
print(next(corutina1))            # spusti prvni cast, dostanete nápoj
print(corutina1.send("vitamínový nápoj"))  # posle data (nápoj) a provede druhou část
print(corutina1.send("A"))        # posle data (volbu) a provede třetí část
print(next(corutina1))            # provede poslední část (vypíše jídlo)

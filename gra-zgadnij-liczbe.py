from random import randint
wylosowana = randint(1,100)
i = 0
odpowiedz = -1
poddanie = 0
kod_poddania = randint(1000,9999)
przegrana = 0
wyjscieint = 0

while odpowiedz != wylosowana:
    if odpowiedz != -1 and (odpowiedz < 1 or odpowiedz > 100) and odpowiedz != kod_poddania:
        print("Nieprawidłowy zakres odpowiedzi. Wpisz liczbę w przedziale od 1 do 100.")
    i += 1
    if i == 5:
        poddanie += 1
    odpowiedz = int(input("Wylosuj liczbę od 1 do 100: "))
    if odpowiedz != -1 and odpowiedz != wylosowana and not (odpowiedz < 1 or odpowiedz > 100) and odpowiedz != kod_poddania:
        print("Niestety, nie udało się. Spróbuj jeszcze raz.")
    if poddanie == 1 and poddanie != 2:
        print("Wpisz kod poddania, aby się poddać. Twój kod poddania to", kod_poddania,)
        poddanie += 1
    if poddanie == 2 and odpowiedz == kod_poddania:
        print("Poddałeś się. Wylosowaną liczbą była liczba", wylosowana)
        przegrana += 1
        wyjscieint += 1
        break
if przegrana !=1:
    print("Brawo! odgadłeś liczbę za ", i, " razem.")
    wyjscieint +=1
if wyjscieint == 1:
    wyjscie = input("Wciśnij klawisz enter, aby zamknąć okno.")
    if wyjscie:
        exit(0)



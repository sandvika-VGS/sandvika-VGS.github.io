'''
a) Lag et program der man kan skrive inn poengsummen for en matematikkeksamen. 
Programmet skal skrive ut karakteren på eksamen når vi bruker følgende skala (maks 60 poeng): 

| Karakter | 1   | 2   | 3   | 4   | 5   | 6   |
| -------- | --- | --- | --- | --- | --- | --- |
| Poeng    |     | 12  | 24  | 35  | 45  | 56  |

b) Endre koden slik at programmet "Ugyldig poengsum" dersom man ikke skriver inn et tall mellom 0 og 60
'''


print("Skriv antall poeng på prøven")
poeng = int(input("Poeng (0 - 60): "))

if poeng > 60 or poeng < 0:
    print("Ugyldig poengsum")
elif poeng >= 56:
    print("Karakter 6")
elif poeng >= 45:
    print("Karakter 5")
elif poeng >= 35:
    print("Karakter 4")
elif poeng >= 24:
    print("Karakter 3")
elif poeng >= 12:
    print("Karakter 2")
else:
    print("Karakter 1")



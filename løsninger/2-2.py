'''
Lag et program som spør bruker etter alder. 
Skriv ut en beskjed dersom brukeren er myndig, og en annen beskjed dersom brukeren ikke er myndig. 
Teksten på beskjeden bestemmer du selv. 
Fokuser kun på år, dato blir for komplisert for dette kurset. 
'''

alder = int(input("Hvor gammel er du? År: "))
if alder >= 18:
    print("Gratulerer, du kan kjøre bil!")
else:
    print("Beklager, men du må nok vente noen år")

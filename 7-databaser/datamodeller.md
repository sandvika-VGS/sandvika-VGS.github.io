# Primærnøkkel

Anta at vi skal lage en nettside om pokemon, og ønsker å lagre disse i en database. Da bør vi først se for oss en tabell med informasjonen vi ønsker å lagre

BILDE: tabell med noe pokemongreier

Når vi lager en datamodell over denne tabellen er vi først og fremst interessert i hva slags (type) informasjon vi skal lagre, ikke selve eksempelene. Vi kan derfor forenkle tabellen til følgende:

BILDE: Enkel modell

Når vi lagrer datene må vi være sikre på at vi kan finne tilbake til det vi ønsker. Da må det være en av egenskapene som vi er *100% sikre på at er unik* for hvert objekt i databasen! Denne egenskapen kalles for en **primærnøkkel** og må være med. I modellen med pokemom, er det bare navnet som muligens kan være unikt. Vi kunne ha brukt navn som primærnøkkel, men bare hvis vi er sikre på at det aldri vil komme en pokemon i fremtiden som vil ha samme navn. Hvis vi 
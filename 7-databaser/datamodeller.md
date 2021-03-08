# Primærnøkkel

Anta at vi skal lage en nettside om pokemon, og ønsker å lagre disse i en database. Da bør vi først se for oss en tabell med informasjonen vi ønsker å lagre

BILDE: tabell med noe pokemongreier

Når vi lager en datamodell over denne tabellen er vi først og fremst interessert i hva slags (type) informasjon vi skal lagre, ikke selve eksempelene. Vi kan derfor forenkle tabellen til følgende:

BILDE: Enkel modell

Når vi lagrer datene må vi være sikre på at vi kan finne tilbake til det vi ønsker. Da må det være en av egenskapene som vi er *100% sikre på at er unik* for hvert objekt i databasen! Denne egenskapen kalles for en **primærnøkkel** og må være med. I modellen med pokemon, er det bare navnet som muligens kan være unikt. Vi kunne ha brukt navn som primærnøkkel, men bare hvis vi er sikre på at det aldri vil komme en pokemon i fremtiden som vil ha samme navn. Dersom vi er usikre på om noen av innføringene våre kan brukes som primærnøkler, kan vi alltids legge til ett nytt felt i modellen:

BILDE: Med id som primærnøkkel

Når vi skal lage en modell, vil innføringene som muligens kan brukes som primærnøkler kalles for **kandidatnøkler**.

## Prøv selv - Klasseliste
Anta at du skal lagre informasjon om de som går i klassen din. Hvordan vil datamodellen se ut? Hvilke kandidatnøkler har du? Hvilke av kandidatnøklene egner seg best som primærnøkkel?

## Prøv selv - etellerannet
Gitt følgende datamodell: LEGG TIL BILDE
Argumenter for at ingen av innføringene er gode kandidatnøkler. Gi et forslag til primærnøkkel

# Atomærkravet
Når vi skal lagre data, kan det være lurt å dele opp informasjonen. Dersom man skal kunne søke både på fornavn og etternavn separat, bør disse stå i hver sin kolonne. **Atomærkravet** sier at 

*alle verdier i en database må deles opp så langt det lar seg gjøre uten at de mister sin mening*.

BILDE: fra powerpointen

Selv om det er lurt å ha atomærkravet i bakhånd når du skal lage en datamodell, bør du alltid bruke skjønn. Hva skal dataene brukes til? Hvem skal søke? Hva slags behov har man når man skal hente ut data? Det er ikke alltid man trenger å dele opp informasjonen.

Bilde?

## Prøv selv?
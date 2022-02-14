# Betingelser. If-Løkker

Livet består av mange valg. Det kan være de små valgene (hva skal jeg ha på meg idag?), eller større valg (Hva skal jeg studere). Hva som skjer videre avhenger nok mye av valgene du til stadig gjør. Dersom vi skal kunne programmere mer avansert, må vi også kunne gi datamaskingen muligheten til å kjøre forskjellige instrukser avhengig av ulike valg. 

Frem til nå har koden vårt kjørt linje for linje nedover. En betingelse derimot består av et eller flere utsagn med tilhørende kode. Koden som hører vil bare kjøre dersom utsagnet stemmer (returner True). La oss se på koden der vi regner ut alderen til brukeren, og legge på en betingelse:


```PYTHON
navn = input("Hva heter du? )
f_aar = int(input("Hvilket år er du født? "))

let alder = 2021 - fødselsår;

if alder > 17:
    print("Hei", navn, "du er myndig!")
```

Vi ser her logikken bak en betingelse, skrevet som en `if-setning`. Vi regner ut alder, og så sjekker vi den matematiske betingelsen `alder > 17`. Dersom alder er større en 17 returnerer sjekken **True**, hvilket betyr at print instruksjonen kjører. Dersom betingelsen returnerer **False**, så skjer det ingenting. Vi bruker innhopp for å gruppere hvilken kode som hører til betingelsen. 

Når vi lager en betingelse kan vi avslutte med `else`, altså kode som skal kjøre dersom betingelsen returnerer **False**:

```PYTHON
navn = input("Hva heter du? )
f_aar = int(input("Hvilket år er du født? "))

let alder = 2021 - fødselsår;

if alder > 17:
    print("Hei", navn, "du er myndig!")
else:
    print("Hei", navn, "du er desverre ikke myndig enda")
```

## Flere Betingelser

Vi kan teste flere betingelser samtidig. Anta at vi ønsker å sjekke om et tall ligger mellom 10 og 20. Da vil vi at tallet både skal være større enn 10, og **samtidig** være mindre enn 20. Vi kan skrive følgende:

```PYTHON
tall = input("Hvor mange poeng fikk du?")

if tall > 10 and tall < 20:
    print("Dette tilsvarer middels måloppnåelse")

``` 

Her må begge betingelsene være sanne samtidig for at koden skal kjøre. 

Hvis vi skal lage ferdig koden (0 - 10 poeng er lav måloppnåelse mens 20 - 30 tilsvarer høy), så kan vi kjede sammen flere betingelser. Setningsoppbygningen foregår da som `if - elif - else`. Her starter "if" instruksjonen, elif står for "else if" der vi kan sjekke andre betingelser (vi kan ha flere av disse etter hverandre), mens "else" avslutter. Det er lettest å se i praksis:

```PYTHON
tall = input("Hvor mange poeng fikk du?")

if tall >= 0 and and tall < 10:
    print("Dette tilsvarer lav måloppnåelse")
elif tall > 10 and tall <= 20
    print("Dette tilsvarer middels måloppnåelse")
elif tall > 20 and tall <= 30:
    print("Dette tilsvarer høy måloppnåelse")
else:
    print("Du må skrive inn poeng mellom 0 og 30!")

``` 

Det er viktig at vi har innhopp på all kode som tilhører hver del av betingelsen. Legg merke til at vi strengt tatt kunne ha laget nye if-setninger for hver sjekk i stedet, men det anses som dårlig kode. Da ville man kunne ha havnet i flere sjekker samtidig, og det ønsker vi å unngå. Ved å bruke elif og else, kobler vi alt sammen til samme betingelse.




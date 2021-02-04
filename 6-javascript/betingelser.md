# Betingelser. If-Løkker

Livet består av mange valg. Det kan være de små valgene (hva skal jeg ha på meg idag?), eller større valg (Hva skal jeg studere). Hva som skjer videre avhenger nok mye av valgene du til stadig gjør. Dersom vi skal kunne programmere mer avanserte, må vi også kunne gi datamaskingen muligheten til å kjøre forskjellige instrukser avhengig av ulike valg. Dette gjøres ved hjelp av betingelser, og prinsippet bak kan minne litt om flytskjema: 

BILDE FLYT. PROBLEMLØSNING VS IF ELSE LØKKE

La oss ta utgangspunkt i koden for alder fra forrige side. Den kan for eksempel se slik ut:

```JAVASCRIPT
let fødselsår = window.prompt("Hvilket år er du født?");
let alder = 2021 - fødselsår;

document.write("Du blir " + alder + " i løpet av året.")
```

Anta at vi ønsker å sjekke om brukeren er myndig eller ikke. Da blir betingelsen om brukeren er yngre enn 18 år eller ikke. Vi kan utvide koden ved å legge til følgende:

```JAVASCRIPT

let fødselsår = window.prompt("Hvilket år er du født?");
let alder = 2021 - fødselsår;

if(alder > 17){
    document.write("Du er myndig");
}
else{
    document.write("Du er ikke myndig enda");
}
```

Vi ser her logikken bak en betingelse, skrevet som en **if-løkke**. Betingelsen må ligge i en parentes, så bruker vi {} for å spesifisere hva slags kode som skal kjøre dersom betingelsen er sann. Hvis betingelsen er usann, hopper koden over til *else* feltet i stedet. Legg merke til at else ikke har en betingelse.

## Prøv selv - Berg og Dalbane
Bruk window.prompt for å ta inn brukerens høyde i cm. Hvis høyden er over 100cm så skrives det en melding om at brukeren for lov til å kjøre berg- og dalbanen. Hvis brukeren ikke er høy nok, skal det i stedet gis en beskjed om det.

## Flere Betingelser

Vi kan teste flere betingelser samtidig. Anta at vi ønsker å sjekke om et tall ligger mellom 10 og 20. Da vil vi at tallet både skal være større enn 10, og **samtidig** være mindre enn 20. Vi kan skrive følgende:

```JAVASCRIPT
if(tall >= 10 && tall <= 20){
    document.write("tallet er mellom 10 og 20)
}
``` 
Her må begge betingelsene være sanne samtidig for at koden skal kjøre. 

Anta videre at vi enten skal sjekke om tallet er under 10, mellom 10 og 20, eller over 20. Da holder det ikke lenger med en **if/else** løkke, det er jo tre muligheter! Vi kan legge til flere betingelser:

```JAVASCRIPT
if(tall < 10){
    document.write("Tallet er under 10");
}
else if(tall >= 10 && tall <= 20){
    document.write("tallet er mellom 10 og 20");
}
else{
    document.write("Tallet er over 20");
}
``` 

Vi må bruke **else if** for å koble alle betingelsene sammen, vi kan legge til så mange vi vil. 

## Prøv selv - Kroppstemperatur
Hos friske mennesker varierer kroppstemperaturen vanligvis mellom 36.5 og 37.5 grader. Lag et program som avgjør om en persons kroppstemperatur ligger henholdsvis under, innenfor eller over normal kroppstemperatur. Programmet skal lese kroppstemperaturen fra window.prompt().

## Prøv selv - Inntekt og Skatt
I det fiktive landet Ruritania er skattereglene slik at hvis en person har inntekt < 10000, så betaler man 10% skatt på hele inntekten, og hvis inntekten >= 10000, så betaler man 10% skatt på de første 10000 kronene og 30% skatt på resten av inntekten. Lag et program som regner ut og skriver ut hvor mange kroner som skal betales i skatt. Programmet skal lese inntekten fra window.prompt(). 
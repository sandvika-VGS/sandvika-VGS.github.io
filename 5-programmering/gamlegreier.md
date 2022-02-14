
 kan lagre tekst, da må vi huske anførseltegnene:

```JAVASCRIPT
let konge = "Harald";
console.log("Hei" + konge);
```
*Hva tror du skrives til konsollen nå? Prøv selv!*

## Prøv selv: Anførselstegn

Forklar forskjellen på koden rett over og følgende:
```JAVASCRIPT
let konge = "Harald";
console.log("Hei" + "konge");
```

## Lagre input

Vi kan også lagre langt mer avanserte ting (for eksempel html-elementer, input fra bruker, lister etc). Prøv følgende kode:

```JAVASCRIPT
let navn = window.promt("Hva heter du?");
console.log("Hei " + navn + ", hyggelig å møte deg!");
```
Her ble altså navnet som brukeren av nettsiden skrev inn lagret i variabelen *navn*. Vi kan da bruke navnet i resten av koden vår, for eksemel til å skrive en hilsen.

## Prøv selv: Kalkulator for temperatur.

```JAVASCRIPT
const fahrenheit = 50;
const celsius = (fahrenheit - 32)*(5/9);
console.log(celsius);
```

Sett deg først inn i koden, hva skjer her? Endre så koden slik at brukeren kan skrive inn fahrenheit i nettleseren (bruk prompt). Skriv en så fin tekst der både fahrenheit og celsius skrives i nettleseren (her kan du bruke document.write). Et forslag til løsning finner du i slutten av kapittelet

## Prøv selv: Regn ut brukerens alder.

Lag en nettside som spør hvilket år du er født. Bruk dette til å skrive en beskjed til bruker om hvor gammel han eller hun vil bli i løpet av året. Legg merke til at vi dropper måned og dato foreløpig, det blir litt for komplisert.



## Prøv selv - Kroppstemperatur
Hos friske mennesker varierer kroppstemperaturen vanligvis mellom 36.5 og 37.5 grader. Lag et program som avgjør om en persons kroppstemperatur ligger henholdsvis under, innenfor eller over normal kroppstemperatur. Programmet skal lese kroppstemperaturen fra window.prompt().

## Prøv selv - Inntekt og Skatt
I det fiktive landet Ruritania er skattereglene slik at hvis en person har inntekt < 10000, så betaler man 10% skatt på hele inntekten, og hvis inntekten >= 10000, så betaler man 10% skatt på de første 10000 kronene og 30% skatt på resten av inntekten. Lag et program som regner ut og skriver ut hvor mange kroner som skal betales i skatt. Programmet skal lese inntekten fra window.prompt(). 
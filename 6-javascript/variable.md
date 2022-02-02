# Variabler
![Variable](variable_glass.jpg)
*På samme måte som denne krydderhylla, kan vi lagre mye forskjellig i datamaskinens minne*

En av de viktigste prinsippene når vi skal kode, er at vi kan lagre alt mulig i datamaskinens minne. Det vi lagrer kan vi hente opp igjen i koden, og bruke når vi selv ønsker det. Når vi lagrer noe i datamaskinens minne på denne måten kaller vi det for en **variabel**. God bruk av variable er fundamentalt for å lære seg å programmere godt. Akkurat som med glassene i bildet over, kan vi lagre alt mulig rart; bokstaver, setninger, tall og lister er eksempler på variable som ofte brukes. Der det er lurt å merke glassene, må vi være påpasselige å si nøyaktig hva vi lagrer, slik at datamaskinen har riktig oversikt. Da vil det også være i stand til å bruke riktig variabel til riktig tid. 

## Lagre en variabel.
Dersom vi for eksempel ønsker å lagre tallet 10 skriver vi 

```PYTHON
tall = 10
```

 Navnet på variabelen (i dette tilfellet **tall**) tilsvarer merkelappen til krydderhylla. Selv om vi bestemmer navnet selv, bør vi velge et navn som gir mening. Vi skal se nærmere for skikk og bruk for variabelnavn etterhvert.

## Hente en variabel
Når vi har lagret en variabel kan vi hente den ved å bruke navnet (merkelappen) vi satte på den:

```PYTHON
tall = 10
print(tall)
```
Hva tror du skrives til konsollen? Sjekk selv.



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




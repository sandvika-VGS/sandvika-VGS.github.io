# Variabler


## Lagre variabler
En av de viktigste prinsippene når vi skal kode, er at vi kan lagre alt mulig i datamaskinens minne. Da bruker vi nøkkelordene *let* eller *const*. Dersom vi ønsker å lagre et tall skriver vi 

```JAVASCRIPT
const a = 10
```

Vi bruker const hvis det ikke skal være mulig å endre tallverdien, mens vi bruker let i det motsatte tilfellet. NB: Navnet på variabelen (i dette tilfellet **a**) bestemmer vi selv. Vi kunne like gjerne ha skrevet *let lise = 10*, som regel prøver vi å velge navn som gir mening.

## Prøv selv
Lag et script-element i html-fila di, og legg til følgende:

```HTML
<h1>Mitt første program</h1>
<script>
    const a = 10;
    console.log(a + 10);
</script>
```

Hva tror du skrives til konsollen? Sjekk selv.

## Ulike variabeltyper

Vi kan lagre tekst

```JAVASCRIPT
let konge = "Harald";
console.log("Hei" + konge)
```
*Hva tror du skrives til konsollen nå? Prøv selv!*

Vi kan også lagre langt mer avanserte ting (for eksempel html-elementer, input fra bruker, lister etc). Prøv følgende kode:

```JAVASCRIPT
let navn = window.promt("Hva heter du?");
console.log("Hei " + navn + ", hyggelig å møte deg!");
```
Her ble altså navnet som brukeren av nettsiden skrev inn lagret i variabelen *navn*. Vi kan da bruke navnet i resten av koden vår, for eksemel til å skrive en hilsen.

## Prøv selv

```JAVASCRIPT
const fahrenheit = 50;
const celsius = (fahrenheit - 32)*(5/9);
console.log(celsius);
```

Sett deg først inn i koden, hva skjer her? Endre så koden slik at man selv kan skrive inn fahrenheit i nettleseren (bruk prompt). Skriv en fin tekst der både fahrenheit og celsius skrives i nettleseren (her kan du bruke document.write)


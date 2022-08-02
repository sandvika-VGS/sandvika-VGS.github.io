# Hyperlenker

Hyperlenker er det som binder nettet sammen.
De gjør det mulig å lenke sammen egne og andres dokumenter, slik at vi kan bevege oss rundt på nettet.

## Hyperlenker i HTML

Se på følgende html snutt:

`<a href="https://www.sandvika.vgs.no/">Skolens hjemmeside</a>`

I HTML lages hyperlenker med å bruke `<a>` - elementet. Her står bokstaven a som en forkotelse for **anchor**.
Attributtet `href` angir hvor lenken peker.
Det som står mellom taggene er det som synes på nettsiden. Html-koden ovenfor vil da se slik ut på nettleseren:

![Eksempel](/eksempellenke.png)

> Tips: For at lenken skal åpne i en ny fane kan vi legge til attributtet `target="_blank"`   
> [Sjekk ut w3schools for å se hva mer du kan gjøre med lenker](https://www.w3schools.com/tags/tag_a.asp)

### Innholdet til a - elementet

I eksempelet ovenfor skrev vi ren tekst i innholdsbiten av lenke elementet, det er ganske vanlig men vi kan være mer avanserte
Alle elementer som ligger nøstet inn i et a-element blir en del av lenka. Slik kan for eksempel nettaviser gjøre både bilde og tekst klikkbare for å lese mer om saken:

```HTML
<a href="https://www.vg.no/sistenytt">
    <img src="kjempekultbilde.png">
    <p>Du vil aldri tro hva som skjedde!</p>
</a>
```

## URL

URL er en forkortelse for Uniform Resource Locator, og viser til *"adresser"*, eller *"stier*, på internett.
Verdien til attributtet *href* i en a-tagg er en URL.
URL'en til Sandvika VGS: `https://www.sandvika.vgs.no`

### Lokal URL

En lokal URL er en *sti* til en fil lagret lokalt på en PC.
Eks: `C:/Users/thorchr/desktop/uk3_html_css/bilde2.jpg`

Vi deler lokale URL'er i *absolutte* og *relative*.
URL'en over er en absolutt URL fordi den viser til den faktiske plasseringen til en fil.
Mens en relativ URL viser til plasseringen av en fil relativt til filen vi er i.
Hvis filen vi er i, er i samme mappe som bilde2.jpg, vil dette være den relative URL'en: `bilde2.jpg`.

Her kommer noen eksempler på hvordan vi kan legge til bilde2.jpg på nettsiden index.html

### I samme mappe

```
-uke2
  |
  |-index.html
  |-bilde2.jpg
```
`<img src="bilde2.jpg">`

### Bilde ligger i en bilder-mappe

For å gå inn en undermappe brukes `navnPåMappe/`

```
-uke2
  |
  |-index.html
  |-bilder
    |
    |-bilde2.jpg
```
`<img src="bilder/bilde2.jpg`

### Bilde og nettsiden ligger i hver sin undermappe

For å gå ett nivå opp brukes `../`

```
-uke2
  |
  |-hjem
    |
    |-index.html
  |-bilder
    |
    |-bilde2.jpg
```
`<img src="../bilder/bilde2.jpg`
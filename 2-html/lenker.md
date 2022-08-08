# Hyperlenker

Hyperlenker er det som binder nettet sammen.
De gjør det mulig å lenke sammen egne og andres dokumenter, slik at vi kan bevege oss rundt på nettet.

## Hyperlenker i HTML

Se på følgende html snutt:

`<a href="https://www.sandvika.vgs.no/">Skolens hjemmeside</a>`

I HTML lages hyperlenker med å bruke `<a>` - elementet. Her står bokstaven a som en forkotelse for **anchor**.
Attributtet `href` angir hvor lenken peker.
Det som står mellom taggene er det som synes på nettsiden. Html-koden ovenfor vil da se slik ut på nettleseren:

![Eksempel](bilder/2_3%20-%20lenker/eksempellenke.png)

> Tips: For at lenken skal åpne i en ny fane kan vi legge til attributtet `target="_blank"`   
> [Sjekk ut w3schools for å se hva mer du kan gjøre med lenker](https://www.w3schools.com/tags/tag_a.asp)

### Innholdet til a - elementet

I eksempelet ovenfor skrev vi ren tekst i innholdsbiten av lenke elementet. Det er ganske vanlig men vi kan være mer avanserte. Alle elementer som ligger nøstet inn i et a-element blir en del av lenka. Slik kan for eksempel nettaviser gjøre både bilde og tekst klikkbare for å lese mer om saken:

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

I dette eksempelet ser vi at ved å gå inn i de fire mappene (Users, thorchr, desktop, uk3_html_css) så finner vi en fil som heter bilde2.jpg

Vi deler lokale URL'er i `absolutte` og `relative`.

URL'en over er en absolutt URL fordi den viser til den faktiske plasseringen til en fil. Absolutte lenker er fine for å se nøyaktig plassering av mapper og undermapper for fila, men det kan bli slitsomt i lengden.

Mens en relativ URL viser til plasseringen av en fil i forhold til filen vi er i. Dette høres nok komplisert ut, men se på utforskeren til VS Code:

![Bilde: Utforsker VS Code](/vscode.png)

Anta at vi jobber med hjemmeside.html, da er vi i mappen uke 2. Den relative URL'en til 
bilde2.png blir da bare `bilde2.jpg` (siden vi er i samme mappe). Dersom bilde2.jpg derimot er i andre mapper, må vi skrive stien ved å hoppe enten inn eller ut av undermappene.

Her kommer noen eksempler på hvordan vi kan skriver relative stier til bilde2.jpg ved å enten gå inn i, eller hoppe ut av mapper.

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

Her må vi først ut av hjem-mappen før vi kan gå inn i bilder-mappen. For å gå ett nivå opp brukes `../`

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


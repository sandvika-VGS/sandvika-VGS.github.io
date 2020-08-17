# 3.1 Html lager nettsiden

Du har trolig vært på utallige nettsider hele livet uten å tenke særlig nøye gjennom hvordan de er laget. La oss få ett innblikk ved å gjøre følgende:

-Velg en nettside du ofte besøker

-Høyreklikk hvor som helst på siden.

-Velg "Vis kildekode" (eller "View source code")

-Se raskt gjennom

Her var det nok mye uforståelig tekst, men det er altså slik nettsiden er laget. Mye her er skrevet på et språk som vi kaller HTML. HTML bruker vi til å bestemme hva som skal være på nettsiden vår, og i en begrenset grad hvordan den skal se ut.

![alt text](./bilde.jpg "Eksempel på kildekode")

Fra [wikipedia.org](https://no.wikipedia.org/wiki/HTML): _HyperText Markup Language (HTML, hypertekstmarkeringsspråk) er et markeringsspråk for formatering av nettsider med hypertekst og annen informasjon som kan vises i en nettleser.
HTML benyttes til å strukturere informasjon – angi noe tekst som overskrifter, avsnitt, lister og så videre – og kan, i en viss grad, brukes til å beskrive utseende og semantikk i et dokument._

Dersom vi skal lage en nettside må vi altså lære oss å skrive html. Vi lagrer det vi skriver i en _html-fil_, som nettleserene kan åpne og vise slik vi ønsker. VS Code er et eksempel på en editor som hjelper oss med å skrive html. 

La oss prøve:

-Åpne VS Code

-Sørg for at du har installert utvidelsen "open in browser" (les "2 - Oppsett" for hjelp)

-Velg File og så "New File"

-Velg File og så "Save as". Lagre den som "hjemmeside.html"

-Kopier inn følgende tekst

```HTML
    <!DOCTYPE html>
    <html>
        <body>
            <h1>Hallo verden!</h1>
        </body>
    </html>
```

-Høyreklikk hvor som helst på siden og velg "Open in default browser"

Gratulerer du har nå laget din første hjemmeside. La oss se nærmere på hva som skjedde.

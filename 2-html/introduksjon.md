## Html lager nettsiden

Du har trolig vært på utallige nettsider hele livet uten å tenke særlig nøye gjennom hvordan de er laget. La oss få ett innblikk ved å gjøre følgende:

- Velg en nettside du ofte besøker

- Høyreklikk hvor som helst på siden.

- Velg "Vis kildekode" (eller "View source code")

- Se raskt gjennom

Her var det nok mye uforståelig tekst, men det er altså slik nettsiden er laget. Mye her er skrevet på et språk som vi kaller HTML. HTML bruker vi til å bestemme hva som skal være på nettsiden vår, og i en begrenset grad hvordan den skal se ut.

![alt text](./bilde.jpg "Eksempel på kildekode")

Fra [wikipedia.org](https://no.wikipedia.org/wiki/HTML): _HyperText Markup Language (HTML, hypertekstmarkeringsspråk) er et markeringsspråk for formatering av nettsider med hypertekst og annen informasjon som kan vises i en nettleser.
HTML benyttes til å strukturere informasjon – angi noe tekst som overskrifter, avsnitt, lister og så videre – og kan, i en viss grad, brukes til å beskrive utseende og semantikk i et dokument._

I IT-1 må vi lære oss 3(!) språk for å lage gode hjemmesider. HTML bestemmer hva som skal være med. CSS bestemmer hvordan siden skal se ut. Javascript hjelper oss med mer avansert interaksjon på nettsiden.

Vi må altså først lære oss å skrive html. Akkurat som når du skriver tekstfiler som word eller onenote kan lese, må du nå skrive en _html-fil_ som nettleserene kan tolke og vise frem. Vi vil helst ha program som er designet for å hjelpe oss til å skrive html. Heldigvis finnes det mange gode alternativer og noen av de er gratis. I år bruker vi VS Code.

La oss prøve:

- Åpne VS Code

- Sørg for at du har installert utvidelsen "open in browser" (les "1.2 - Oppsett" for hjelp)

- Velg File og så "New File"

- Velg File og så "Save as". Lagre den som for eksempel "hjemmeside.html" (filnavnet kan være hva som helst, men det må slutte med .html)

- Kopier inn følgende tekst

```HTML
    <!DOCTYPE html>
    <html>
        <body>
            <h1>Hallo verden!</h1>
        </body>
    </html>
```

- Høyreklikk hvor som helst på siden og velg "Open in default browser"

Gratulerer du har nå laget din første hjemmeside. La oss se nærmere på hva som skjedde.

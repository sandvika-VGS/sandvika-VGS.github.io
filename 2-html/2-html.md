# 1. HTML

Du har trolig vært på utallige nettsider hele livet uten å tenke særlig nøye gjennom hvordan de er laget. La oss få ett innblikk ved å gjøre følgende:

-Velg en nettside du ofte besøker
-Høyreklikk hvor som helst på siden.
-Velg "Vis kildekode" (eller "View source code")
-Se raskt gjennom

Her var det trolig mye uforståelig tekst, men dette er altså slik nettsiden er laget. Mye her er skrevet på et språk som vi kaller HTML. Dette språket bruker vi til å bestemme hva som skal være på nettsiden vår, og i en begrenset grad hvordan det skal se ut.

![alt text](./bilde1.jpg "Et utsnitt av html kode på nrk.no" ':size=200')



_HyperText Markup Language (HTML, hypertekstmarkeringsspråk) er et markeringsspråk for formatering av nettsider med hypertekst og annen informasjon som kan vises i en nettleser.
HTML benyttes til å strukturere informasjon – angi noe tekst som overskrifter, avsnitt, lister og så videre – og kan, i en viss grad, brukes til å beskrive utseende og semantikk i et dokument.
Hentet fra [wikipedia.org](https://no.wikipedia.org/wiki/HTML)_

![alt text](./bilde.jpg "Bildetekst")

```HTML
    <!DOCTYPE html>
    <html>
        <body>
            <h1>Hallo verden!</h1>
        </body>
    </html>
```

# 1.1 Vanlige HTML-elementer

- h1 (Header 1) – Overskriften på dokumentet
- h2 – h6 (Header 2 – Header 6) – Underoverskrifter (angir underseksjoner)
- table (Table) – Lager en tabell
- ul (Unordered List) – Punktliste
- ol (Ordered List) – Nummerert liste
- br (Break) – Linjeskift
- div (Division) – En seksjon i dokumentet
- p (Paragraph) – Et avsnitt, vises som regel med en blank linje over og under
- strong (Strong) – Indikerer viktig tekst, vises vanligvis i fete typer
- b (Bold) – Gir fet skrift, men ingen viktighetshentydning
- em (Emphasis) – Indikerer vektlagt tekst, vises normalt i kursiv
- i (Italics) – Gir kursiv tekst
- a (Anchor) – En lenke til en annen ressurs på nettet (nettside, e-postadresse, nyhetsgruppe etc.)
- form (Form) – Benyttes for å sette inn skjemaelementer, skrivefelt, knapper, avkryssningsbokser og lignende.


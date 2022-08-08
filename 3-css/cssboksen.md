# CSS - "Boksen"

Vi har sett at vi kan endre farge og størrelse på html-elementene våre. Når det gjelder posisjonering og layout, så må vi starte med å lære oss fire viktige css-egenskaper som *alle* html-element består av. For å forstå hvordan disse fungerer er det lurt å forestille seg hver html-element som en egen boks, der denne boksen består av:

* Content: Innholdet, altså delen der tekst og bilder vises.
* Padding: Et område som ligger rundt innholdet.
* Border: En grense som ligger rundt både innhold og padding.
* Margin: Et område på utsiden av border.

Det kan kanskje være litt forvirrende å se for seg hvordan dette fungerer, når du for eksempel skriver en overskrift inne i et h1-element har du hverken sett spor av hverken bokser eller de andre begrepene. Det er fordi vi kun har vært oppmerksomme på innholdsbiten av elementet! La oss se på et eksempel som lett visualiserer boks-modellen. 

Vi starter med en overskrift, og setter en annen bakgrunnsfarge på denne enn resten av nettsiden:

![alt text](./bilder/3_3%20cssboksen/cssoverskrift0.png)

Det er nå innholdsdelen som er farget rosa, 



![alt text](./cssboks.png "Boks-Modellen")

Alle html-element består av boksmodellen ovenfor, men veldig ofte er de "skrudd av" og dermed ikke synlige før vi endrer på egenskapene. La oss ta for oss et h1 element, vi setter på en bakgrunnsfarge og skrur på border i CSS.

```CSS
h1{
    background-color: pink;
    border: solid black 1px;
}
```

Da får vi følgende utseende

![alt text](./cssoverskrift.png)

La oss se hva padding gjør:

```CSS
h1{
    background-color: pink;
    border: solid black 1px;
    padding: 20px;
}
```
![alt text](./cssoverskrift2.png)

Vi ser at padding fyller luft rundt innholdet til elementet, men innenfor den sorte linjen vi tegnet med border. Tilsvarende vil margin fylle luft utenfor den sorte linjen.
> OBS!
>
> Ved å sette left-, right-, top- eller bottom- foran i CSS, kan man finjustere både margin, padding og border!

Husk at vi kan endre margin, padding og border på alle html element

## Div - elementet

Et html-element vi bruker veldig mye er div-elementet. Dette elementet har satt alle delene av boks-modellen til 0, slik at vi kan se på det som en usynlig boks rundt inhholdet. Ved å nøste div-elementer rundt hverandre kan man gruppere innhold som man så kan bestemme utseende på.
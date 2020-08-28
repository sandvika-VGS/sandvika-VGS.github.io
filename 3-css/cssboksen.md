# CSS - "Boksen"

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
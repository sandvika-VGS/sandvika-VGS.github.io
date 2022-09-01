# Hva er CSS?

CSS er stilspråk som står for *Cascading Style Sheet*. Det brukes til å sette såkalte stiler på html-elementene våre, og gir oss langt flere muligheter for å posisjonere de slik vi ønsker.
Det er CSS som brukes til å sette bakgrunnsfarger på nettsiden, endre teksttype, størrelser på bilder etc..

Siden CSS er et eget språk skrives det ikke med de samme reglene som html, så la oss starte med det grunnleggende.



## Oppbygningen av CSS-regler

![Et CSS-regelsett](./bilder/3_1%20-%20css/css-regel.png)
  
Hele koden i bildet over utgjør et CSS-regelsett.
Et regelsett består av flere mindre deler:  

1. **Selektor:** Dette er en kobling til HTML-elementet som det skal settes stil på. I dette tilfellet alle `<p>`-elementer.
2. **Egenskap:** Forteller hvilken egenskap som skal endres på, eks: `color`.
3. **Verdi:** Forteller hvilken verdi egenskapen skal ha, eks: `red`.
4. **Deklarasjon:** Utgjøres av både egenskapen og verdien. Hele linjen med kode kalles for en CSS-regel.


Et regelsett består ofte av flere deklarasjoner, og hele CSS-koden vil som regel ha flere regelsett, se eksemplet under.

```CSS
body{
    background-color: lightgrey;
}
p{
    font-size: 24px;
    color: red;
}
```

Her har vi to selektorer nemlig `body` og `p`. Vi husker at body-elementet omsluttet alt som vises på nettsiden vår, så ved å sette en bakgrunnsfarge her endrer vi farge på hele siden. I tillegg endrer vi altså skriftstørrelse og farge på alle p-elementene våre. Nå i begynnelsen er det vanskelig å vite både hvilke egenskaper og valg man faktisk har. Vi kommer til å endel med CSS, slik at man lærer seg de mest vanlige triksene og blir tryggere på å slå opp resten.

Først må vi uansett vite hvor vi faktisk skal skrive CSS-koden vår, og her har vi flere valg. Vi kan lage en egen css-fil og koble den sammen med html fila vår. Det egner seg kanskje best når vi lager et nettsted bestående av flere sider, for da kan vi bruke samme css-fil for å sette felles utseende på nettsidene våre. Vi ser mer på dette senere.

Alternativt kan vi nøste et `<style>`-element inn i  `<head>` i html-fila vår. Da kan vi skrive all css vi trenger inne i dette elementet. Nettsiden vi har jobbet med i forrige kapittel vil dermed se ut som følger (legg merke til style elementet):

```HTML
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Min Side</title>
            <style>
                body{
                  background-color: lightgrey;
                }
                p{
                  font-size: 24px;
                  color: red;
                }
            </style>
        </head>
        <body>
            <h1>Hallo verden!</h1>
            <p>Katten min er veldig gretten</p>
            <p>Den er også veldig lat</p>
            <p>Her er et bilde av katten min:</p>
            <img src="minkatt.jpg" alt="katten min">
        </body>
    </html>
```
*Eksperimenter selv ved å prøve deg frem med andre egenskaper og verdier i VS-Code.|


Hva hvis vi bare vi bare vil sette farge på det midterste avsnittet? Selektorene vi har sett på hittil endrer jo på alle element av samme type. Neste side tar for seg litt mer avanserte selektorer som gir flere muligheter.


## Oppgaver

1. Lag et nettsted om solsystemet
   - Last ned filen [solsystemet.zip](https://raw.githubusercontent.com/sandvika-VGS/sandvika-VGS.github.io/master/3-css/solsystemet.zip)
   - Nettsted skal minst ha:
   - Fire undersider:
     - index.html – hjemmesiden
     - solen.html – En infoside om solen
     - mars.html – En infoside om mars
     - planetene.html – En oversikt over planetene
   - Navigasjonsbar
   - Overskrifter
   - En egen CSS-fil
   - En annen bakgrunnsfarge enn hvit

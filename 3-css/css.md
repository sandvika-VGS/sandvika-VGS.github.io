# Hva er CSS?

CSS er, slik som HTML, ikke et programmeringsspråk, heller ikke et markeringsspråk.
CSS er et stilspråk.
Det brukes til å sette stiler på nettsider.
For eksempel er det CSS som brukes til å sette bakgrunnsfarger på nettsiden, endre teksttype, størrelser på bilder, osv..

Følgende linjer med kode gjør at alle p-elementer (avsnitt) på nettsiden har rød tekst:

```CSS
p {
    color: red;
}
```

CSS skrives i eget `<style>`-element i  `<head>`.
Under er et eksempel på en nettside med CSS-kode. Legg merke til `style`-elementet.
```HTML
<!DOCTYPE html>
<html lang="no">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Min hjemmeside</title>
    <style>
      p{
        color: red;
      }
    </style>
  </head>
  <body>
    <p>Min katt er veldig gretten</p>
  </body>
</html>
```

> CSS kan også skrives i en egen `CSS`-fil, det skal vi se på senere.

## Oppbygningen av CSS-regler

![Et CSS-regelsett](css-regel.png)  
Hele koden i bildet over utgjør et CSS-regelsett, den består av flere mindre deler som vi skal se nærmere på.

1. **Selektor:** Dette er navnet til HTML-elementet som det skal settes stil på. I dette tilfellet `<p>`-elementer.
2. **Egenskap:** Forteller hvilken egenskap som skal endres på, eks: `color`.
3. **Verdi:** Forteller hvilken verdi egenskapen skal ha, eks: `red`.
4. **Deklarasjon:** Utgjøres av både egenskapen og verdien. Hele linjen med kode kalles for en CSS-regel.

Et regelsett består ofte av flere regler, f.eks slik som i koden under.

```CSS
p{
    font-size: 24px;
    color: white;
    background-color: black;
}
```

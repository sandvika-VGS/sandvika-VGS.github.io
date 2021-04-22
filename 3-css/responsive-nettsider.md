# Responsive nettsider

En responsiv nettside er en nettside hvor innholdet automatisk tilpasses størrelsen på skjermen eller nettleservinduet.
Elementene på nettsiden vil automatisk krympes, strekkes eller flyttes for å tilpasse størrelsen de har tilgjengelig.
Under er et eksempel på hvordan www.nytimes.com ser ut med forskjellig skjermstørrelser.

![PC-versjon](./responsive-nettsider/pc.png ':size=800')  
*PC-versjon*

![Tablet-versjon](./responsive-nettsider/tablet.png ':size=400')  
*Tablet-versjon*

![Mobil-versjon](./responsive-nettsider/mobil.png ':size=200')  
*Mobilversjon*

## Vanlige skjermstørrelser

Regelverket for universell utforming sier at nettsider skal kunne brukes av alle, og som designere vet vi ikke hva slags skjerm brukerne våre har.
Derfor er det viktig at vi lager nettsider som ser bra ut på alle typer skjermer.
Les mer om universell utforming og responsivt design på [uu.difi.no](https://uu.difi.no/krav-og-regelverk/kom-i-gang/hvordan-teste-universell-utforming-av-ditt-nettsted#forstoerring).

Under kan du se en oversikt over de mest vanlige skjermstørrelsene. 

![Vanlige skjermstørrelser](./responsive-nettsider/breakpoints.png)
*Vanlige skjermstørrelser. [Hentet fra freecodecamp](https://www.freecodecamp.org/news/the-100-correct-way-to-do-css-breakpoints-88d6a5ba1862/)*

## Responsive nettsider med CSS


### % skalerer elementer etter skjermstørrelsen 

For at elementer skal skaleres etter størrelsen på skjermen, kan vi bruke enheten % på width.
I koden under vil bildene alltid ta 100% av plassen de har fått.

````css
img{
    width: 100%;
}
````

> Eksperttips: Det er også mulig å bruke `max-width`. I eksemplet under er main 900px i bredden så lenge skjermstørrelsen er stor nok. Hvis skjermstørrelsen er under 900px, vil main skaleres etter skjermen.
> ````css
> main{
>   width: 900px;
>   max-width: 100%;
> }
> ````

### Media queries

Media queries brukes når CSS-kode bare skal gjelde hvis en spesiell betingelse er oppfylt.
Det kan for eksempel være at en grid skal vise fire bilder i bredden på store skjermer, men bare ett bilde i bredden på små.

#### Skrivemåte
````css
@media (betingelse){
    /* CSS-kode som skal gjelde hvis betingelsen er oppfylt */
}
````

#### max- og min-width

Det finnes mange typer media queries, du kan lese om alle på [MDN web docs](https://developer.mozilla.org/en-US/docs/Web/CSS/Media_Queries/Using_media_queries).
I IT1 er vi mest interessert i `max-width` og `min-width`, disse lar oss lage CSS som kun gjelder for gitte skjermbredder.

````css
/* Minimum bredde, gjelder fra verdi og oppover */
@media (min-width: 1200px) {
  div {
    background-color: yellow;
  }
}

/* Maks bredde, gjelder opp til verdi  */
@media (max-width: 900px) {
  div {
    background-color: blue;
  }
}
````

### Eksempel - Responsiv grid

Vi kan lage en grid responsiv ved å endre antall elementer som vises i bredden.

````css
.grid{
    display: grid;
    grid-gap: 5px;
    grid-template-columns: repeat(4, 1fr);
}
@media(max-width: 900px){
    .grid{
        grid-template-columns: 1fr 1fr 1fr;
    }
}
@media(max-width: 700px){
    .grid{
        grid-template-columns: 1fr 1fr;
    }
}
````

Koden over gir nettsiden under:

![Eksempel - Grid](responsive-nettsider/grid-eksempel.png ':size=400')

### Eksempel - Responsiv navigasjonsbar med flex

For å gjøre en navigasjonsbar responsiv kan vi endre på flex-direction.

````css
nav {
  display: flex;
  justify-content: space-around;
}

@media (max-width: 900px) {
  nav {
    flex-direction: column;
    align-items: center;
  }
}
````

### Eksperttips: Responsiv nettside uten media-query

Henter fra [CSS-tricks.com - A Complete Guide to Grid](https://css-tricks.com/snippets/css/complete-guide-grid/).

<iframe src="https://codesandbox.io/embed/responsiv-nettside-med-grid-fiejm?fontsize=14&hidenavigation=1&theme=dark"
     style="width:100%; height:500px; border:0; border-radius: 4px; overflow:hidden;"
     title="Responsiv nettside med grid"
     allow="accelerometer; ambient-light-sensor; camera; encrypted-media; geolocation; gyroscope; hid; microphone; midi; payment; usb; vr; xr-spatial-tracking"
     sandbox="allow-forms allow-modals allow-popups allow-presentation allow-same-origin allow-scripts"
></iframe>

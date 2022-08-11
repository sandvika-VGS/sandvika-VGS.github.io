# Flex

## Plassering av elementer

Hittil har vi sett litt hvordan man kan endre stil på elementene vi ønsker, og vi har jobbet med egenskapene til "Boks-modellen". Ettersom man har hatt et ønske om å ha bedre kontroll over hvordan elementer skal plasseres, er det utviklet flere mer avanserte teknikker som vi nå skal se nærmere på. Den første av disse kalles `flex`. Vi bruker gjerne flex når vi skal posisjonere elementer i en dimensjon, altså på en linje eller en rad. 


## Posisjonering av lenker med Flex

Som vanlig er det best å starte med et eksempel. De aller fleste nettsteder du besøker består av mange undersider, og har da en felles fane der du lett kan navigere deg rundt. La oss bruke flex til å lage en slik fane med lenker på toppen av nettsidene våre. Det er naturlig å skrive denne koden i et header element, før resten innholdet som vi legger i main-elementet:

```HTML
<body>
    <header>
        <nav>
            <a href="...">Lenke 1</a>
            <a href="...">Lenke 2</a>
            <a href="...">Lenke 3</a>
            <a href="...">Lenke 4</a>
            <a href="...">Lenke 5</a>
        </nav>
    </header>
    <main>
        (...)
    </main>
</body>
```
Uten CSS ser det ikke spesielt imponerende ut:

![alt text](./bilder/3_4%20flex/navbar1.png)

Vi skal nå vise hvordan vi ganske enkelt kan posisjonere lenke slik vi ønsker ved hjelp av flex i CSS. Da trenger vi alltid ha et element som forelder for det vi skal posisjonere. Vi ser av koden i eksempelet over, at nav-elementet passer fint som en slik forelder.

![alt text](./bilder/3_4%20flex/flexboks.png)

Vi starter med å skru på flex på forelder elementet.

```CSS
nav{
    display: flex;
}
```

Legg merke til at ingenting endrer seg enda, vi har bare satt igang verktøyet og må nå vite hvilke egenskaper vi har tilgjengelig.

## Flex - Egenskaper.

Følgende egenskaper er mye brukt:

* `flex-direction`: row / column. Her bestemmer vi om barna skal plasseres langs en rad eller kolonne. Standardinnstillingen er `row` altså horisontalt, og vi trenger derfor ikke denne egenskapen med mindre lenkene skal ligge vertikalt.

* `justify-content:` flex-start / flex-end / center / space-between /space-around. Den viktigste egenskapen for posisjonering. Vi ser nærmere på denne i eksempler nedenfor.

* `align-items:` flex-start / flex-end / center /baseline. Her bestemmer vi hvordan elementene skal legge seg i "motsatt retning" av det vi valgte i "flex-direction". Dersom vi har lagt elementene på en rad, vil align-items justere de i høyden. Motsatt vil elementer i en kolonne kunne justeres horisontalt. 

## Alternativ 1 - Horisontal Spredning

La oss pynte på navigasjonsfanen vår, se nøye på hver egenskap og resultatet og prøv å avgjøre hva hver linje gjør.

```CSS
nav{
    background-color: lightgrey;
    padding-top: 20px;
    padding-bottom: 20px;
    border-bottom: solid black 2px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

nav a{
    color: black;
    text-decoration: none;
}
```

![alt text](./bilder/3_4%20flex/navbar2.png)

*Resultatet*

> Vi ser at "space-around" gjør at barna til nav fyller hele skjermen, men like mye luft på 
> hver side. `text-decoration: none;` er en egenskap som fjerner understreken på lenkene. 

## Alternativ 2 - Horisontalt Venstrestilt

En annen variant er å legge padding på selve lenkene, og bruke "flex-start" i stedet.:

```CSS
nav{
    padding-top: 20px;
    padding-bottom: 20px;
    border-bottom: solid black 2px;
    display: flex;
    justify-content: flex-start;
    align-items: center;
}

nav a{
    color: black;
    padding-right: 30px;
}
```
![alt text](./bilder/3_4%20flex/navbar3.png)

*Resultat*

## Alternativ 3 - Mobil/Vertikal

For en nettside til mobiltelefon, er det beste som regel å ha fleks-elementene i en kolonne. Vi endrer flex-direction og setter litt padding mellom lenkene:

```CSS
        nav{
            background-color: lightgray;
            padding-top: 20px;
            padding-bottom: 20px;
            border-bottom: solid black 2px;
            border-top: solid black 2px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }  
        nav a{
            color: black;
            padding-bottom: 10px;
        }
```
![alt text](./bilder/3_4%20flex/navbar5.png)

## Alternativ 4 - Horisontalt i grupper

Ofte er det vanlig å ha lenker til nettstedet til venstre, og innlogging eller min side til høyre. Vi nøster lenkene slik at det bare blir to fleks-barn og legger `space-between` på disse:

```HTML
<body>
    <header>
        <nav class="flex-container">
            <div id="venstre-lenker">
                <a href="...">Lenke 1</a>
                <a href="...">Lenke 2</a>
                <a href="...">Lenke 3</a>
                <a href="...">Lenke 4</a>
            </div>
            <div id="høyre-lenker">
                <a href="...">Lenke 5</a>
            </div>
        </nav>
    </header>
</body>
```

```CSS
        .flex-container{
            background-color: lightgray;
            padding-top: 20px;
            padding-bottom: 20px;
            border-bottom: solid black 2px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }  
        nav a{
            color: black;
            text-decoration: none;
            padding-right: 30px;
        }
```

![alt text](./bilder/3_4%20flex/navbar4.png)

*Resultat*


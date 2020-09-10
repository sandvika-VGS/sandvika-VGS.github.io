# Flex

## Avansert plassering. Flex og Grid.
Hittil har vi sett litt hvordan man kan endre stil på elementene vi ønsker, og vi har jobbet med egenskapene til "Boks-modellen".. Ettersom man har hatt et ønske om å ha bedre kontroll over hvordan elementer skal plasseres, er det utviklet flere mer avanserte teknikker som vi nå skal se nærmere på. De viktigste kalles *flex* og *grid*.

Vi bruker gjerne flex når vi jobber i en dimensjon altså på en linje eller en rad. Dette passer for eksempel perfekt til en navigasjonsbar i header-elementet. 

<bilde>

Grid bruker vi som regel til innhold i to dimensjoner, der vi lager et slags "rutenett" som vi legger elementene i.

<bilde>

## Introduksjon til Flex.
Vi skal nå lage en navigasjonsbar ved hjelp av flex, denne legger vi i header. Når vi skal bruke flex må vi alltid ha et element som ligger rundt alt vi skal plassere sammen.

![alt text](./flexboks.png)

Siden vi lager navigasjonsbaren i header elementet, kan vi legge til et nav element som fungerer som en flex-boks:

```HTML
<body>
    <header>
        <nav class="flex-container">
            <a href="...">Lenke 1</a>
            <a href="...">Lenke 1</a>
            <a href="...">Lenke 1</a>
            <a href="...">Lenke 1</a>
            <a href="...">Lenke 1</a>
        </nav>
    </header>
</body>
```

I css kan vi nå skru på flex på flex-boksen, da vil alle elementene (barna) til flexboksen etterpå kunne plasseres slik vi ønsker:

```CSS
.flex-container{
    display: flex;
}
```

Legg merke til at ingentin endrer seg enda, vi har bare "skrudd på" flex-egenskapene.

## Flex - Egenskaper.

Følgende egenskaper er mye brukt:

* flex-direction: row / column. Her bestemmer vi om flex-elementene skal plasseres langs en rad eller kolonne. Standard er rad, i så tilfelle trenger vi ikke å skrive denne egenskapen.

* justify-content: flex-start / flex-end / center / space-between /space-around. Denne egenskapen bestemmer hvordan elementene skal legge seg langs raden eller kolonnen.

* align-items: flex-start / flex-end / center /baseline. Her bestemmer vi hvordan elementene skal legge seg i "motsatt retning". Dersom vi har lagt elementene på en rad, vil align-items justere de i høyden. Motsatt vil elementer i en kolonne kunne justeres horisontalt. 

Det finnes langt flere egenskaper, men disse er de vanligste. Vi skal også bruke grid som et alternativ for en del av egenskapene vi ikke lister opp her.

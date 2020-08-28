# Ulike Selektorer i CSS

Vi har hittil sett på hvordan vi kan endre på alle html element av en type ved å bruke en selektor, men kan vi bare endre ett enkelelement? I andre tilfeller ønsker vi raskt å sette lik stil på forskjellige element, finnes det en raskere måte å gjøre dette på enn å skrive egen css for hvert element? 

Svaret på begge spørsmålene er ja, ved å bruke andre typer selektorer så kan vi med raskt og med full presisjon endre stil på nøyaktig de elementene vi ønsker. Først må vi introdusere to viktige attributter:

```HTML
<section class="norefjell">
    <h1 class="norefjell">Fjelltur i sommerferien</h1>
    <img src="fjelltopp.jpg" alt="bilde av en fjelltopp" id="fjelltopp">
    <p class="norefjell">I sommer gikk vi en tur til Høgevarde, det er en (...)</p>
</section>
```

Attributtene **class** og **id** er ofte brukt. Id brukes for å få tilgang til et enkelt unikt element, mens class brukes for å raskt få tilgang til en gruppe elementer. Dermed følger det at ingen elementer kan ha samme id, mens mange elementer kan (og bør) ha samme klasse. Når vi planlegger utseende for nettsiden vår er det lurt å tenke over hvordan vi bør sette opp class- og id- attributtene.

## Class-Selektor

Når vi har en klasse vi ønsker å endre stil på med css kan vi ikke bare skrive navnet på denne slik vi er vant til som en selektor, da leter nettleseren etter ett element med det navnet. Vi må derfor ha en egen skrivemåte for en selektor som skal peke på en klasse:

```CSS
.norefjell{
    font-family:cursive;
    color: lightgrey;
}
``` 
Legg merke til punktumet foran, det indikerer at du skal endre på alle elementer som har klassen "norefjell"

## Id-Selektor

Tilsvarende som class-selektoren har vi også en egen skrivemåte for id-selektoren:

```CSS
#fjelltopp{
    border: solid red 2px;
}
``` 
*Denne css-snutten endrer bare på fjelltopp-bildet, ingen eventuelle andre bilder på nettsiden.*
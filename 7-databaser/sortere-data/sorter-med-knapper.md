# Sorter med knapper

Selv med en grovsortering i navigasjonsbaren kan det godt være at vi ønsker å sortere varene våre enda mer.

I dette avsnittet ser vi på hvordan dette kan gjøres ved hjelp av knapper.

Vi legger til en attributt kalt sjanger i firestore, og fyller denne med for eksempel: krim, fantasy, sci-fi og barn.

**For romanene som ikke oppfyller en av disse sjangerene, lar vi bare feltet stå tomt.**

## HTML

```html
<button id="alle" onclick="hentAlleBoker()">Alle Romaner</button>
<button id="krim" onclick="hentKrim()">Krim</button>
<button id="fantasy" onclick="hentFantasy()">Fantasy</button>
<button id="scifi" onclick="hentScifi()">Science Fiction</button>
<button id="barn" onclick="hentBarn()">For barn og unge</button>
```

Vi kaller på funksjoner som skal gjøre riktige spørringer når vi trykker på en knapp. Disse funksjonene må vi lage, men det blir veldig likt tidligere.

## Javascript

```js
const hentKrim = async () => {
    secBoker.innerHTML = ``; //Sletter gammelt innhold i secBoker.
    const svar = await boker.where("sjanger", "==","krim").get();
    for(const bok of svar.docs){
        lagHTML(bok.id, bok.data());
    }
}
```

Vi må lage de tre andre funksjonene også, men de lages på nøyaktig samme måte. Funksjonen hentAlleBoker har vi fra før av, så den trenger vi ikke lage på nytt.

## Alternativt - IT2-versjon

Det er også mulig å lage dette med bare en funksjon hentSjanger(sjanger), hvor vi sender inn sjangeren som parameter.

```html
<button id="alle" onclick="hentAlleBoker()">Alle Romaner</button>
<button id="krim" onclick="hentSjanger('Krim')">Krim</button>
<button id="fantasy" onclick="hentSjanger('Fantasy')">Fantasy</button>
<button id="scifi" onclick="hentSjanger('Sci-Fi')">Science Fiction</button>
<button id="barn" onclick="hentSjanger('Barn')">For barn og unge</button>
```

> Sjangeren som står mellom parentesene må være helt lik den i databasen.
>Legg merke til at det som sendes inn i funksjonen (mellom parentesene) skrives med 'enkle anførseltegn'. Dette er fordi sjangeren som sendes inn i funksjonen må være en string, og vi allerede er inne i en string definert med doble anførselstegn.

```js
const hentSjanger = async (sjanger) => {
    secBoker.innerHTML = ``; //Sletter gammelt innhold i secBoker.
    const svar = await boker.where("sjanger", "==",sjanger).get();
    for(const bok of svar.docs){
        lagHTML(bok.id, bok.data());
    }
}
```

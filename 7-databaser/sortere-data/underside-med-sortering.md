# Eksperttips - Åpne underside med sortering

## Hovedsiden

Hovedsiden inneholder en lenke til undersiden alle-boker.html, denne lenken har også med tilleggsinformasjonen **sjanger=krim**.

```html
<a href="alle-boker.html?sjanger=Krim">
    <img src="bildeAvKrim.jpg">
</a>
```

## Alle-boker.html

På siden alle-boker.html kan vi hente ut informasjonen som ligger i URL-en.

```js
// henter type fra URL-adressen
const url = new URL(window.location.href);
const sjanger = url.searchParams.get("sjanger");
```

Denne typen kan vi nå bruke i funksjonen som henter bøker på denne siden.

```js
// funksjon som henter bøker fra databasen
const hentBoker = async () => {
  let svar; // Oppretter en tom variabel for svar
  
  if(type){ // hvis det finnes en type gjør følgende:
    svar = await boker.where("sjanger","==",sjanger).get();
  }
  else{ // ellers, altså hvis det ikke finnes en type, gjør følgende:
    svar = await boker.get();
  }
  
  console.log(svar);
  for(const bok of svar.docs){
    lagHTML(bok.id, bok.data());
  }
}

hentBoker(); // Kjører funksjonen hentAlle
```

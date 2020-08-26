# Strukturering av nettsiden

## Block elementer vs. inline elementer

Når vi skal strukturere en nettside bør vi vite hvordan elementene våre legger seg på siden.
De fleste elementene vi bruker på nettsiden vil i utgangspunktet være enten et `block`-element eller et `inline`-element.

- Et `block`-element vil stå på en egen linje på nettsiden. Ingen elementer vil legge seg ved siden av disse. Disse elementene har ofte inline-elementer inne i seg. Eksempler på slike elementer er avsnitt og lister.
- Et `inline`-element ligger inne i block-elementer, og vil ikke ligge på en egen linje. Eksempler på slike elementer er lenker og bilder.

## Semantiske elementer

For å enklere kunne strukturere nettsider bruker vi semantiske elementer, som vil si elementer med tagger som sier noe om innholdet i elementet.
Disse elementene er `block`-elementer, og de har ikke har noe eget innhold, de brukes kun til struktur.
De mest vanlige semantiske taggene er:

| Tag       | Beksrivelse |
|-----------|-------------|
|`<header>` |topptekst|
|`<main>`   |hovedinnhold|
|`<footer>` |bunntekst|
|`<section>`|samler innhold som hører sammen|
|`<article>`|selvstendig innhold|
|`<div>`    |diverse innhold|

En vanlig strukturering av nettsiden med semantsike elementer ser slik ut:

![Semantiske tagger](semantiske-tagger.png)

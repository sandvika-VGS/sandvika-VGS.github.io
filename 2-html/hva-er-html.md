# Hva er HTML?

HTML er ikke et programmeringsspråk.
Det er et markeringsspråk, som brukes til å strukturere innhold på nettsider.
HTML består av *elementer*, som brukes for å pakke inn innhold, slik at det vises på en spesiell måte i nettleseren.
*Taggene* som pakker inn innholdet forteller nettleseren om innholdet er tekst, en lenke, et bilde, og så videre.
Se for ekesemepel på følgende linje med innhold:

```
Katten min er veldig gretten
```
Hvis vi har lyst at denne teksten skal stå for seg selv på nettsiden, kan vi legge på *paragraph*-tagger (avsnitts-tagger).

```HTML
<p>Katten min er veldig gretten</p>
```

## Oppbygningen av et HTML-element

![Et HTML-element](tag.png)  
Delene av dette *p-elementet* er følgende:

1. **Åpningstaggen:** Denne består av navnet på elementet (i dette tilfellet p), pakket inn i *krokodillemunner*.
2. **Lukketaggen:** Denne er lik som åpningstaggen, bare at vi legger til en skråstrek før navnet på elementet.
3. **Innholdet:** I mellom taggene er innholdet i elementet, som i dette tilfellet bare er tekst.
4. **Hele elementet:** Åpningstaggen, lukketaggen og innholdet utgjør hele elementet.

## Attributter

Elementer kan også ha attributter som ser slik ut:
![HTML-element med attributt](attributt.png)  
Attributter innholder ekstra informasjon om elementet, som ikke vises på nettsiden.
I dette tilfellet er `class` attributtnavnet, og `editor-note` attributtverdien.
`class` bruker vi for å kunne hente ut dette elementet senere, slik at vi f.eks kan endre stil på det.  

En attributt burde alltid ha følgende:

1. Mellomrom mellom attributten og elementnavnet.
2. Attributtnavnet etterfulgf av et likhetstegn.
3. Attributtverdien inne i anførselstegn.

> OBS!
>
> Noen få attributter trenger ikke attributtverdi.

## Nøstede elementer

I HTML kan du putte elementer inne i elementer, dette kalles *nøsting*.
Hvis vi har lyst til å understreke at katten vår er veldig gretten, kan vi sette "veldig" i et `<strong>` element, det vil gjøre at "veldig" blir skrevet med fet skrift på nettsiden.

```HTML
<p>Katten min er <strong>veldig</strong> gretten.</p>
```

> OBS!
>
> Her må du passe på at du nøster riktig. Dette blir feil:
>
> ```HTML
> <p>My cat is <strong>very grumpy.</p></strong>
> ```
>
> Elementene må åpnes og lukkes korrekt, slik at de er innenfor eller utenfor hverandre.
> Hvis de overlapper, slik som i koden over, vil nettleseren din prøve å tippe hva du mener, og det blir ofte feil.


# Bilder i databasen

Bilder som skal brukes på nettstedet burde lagres lokalt sammen med html-filene til prosjektet. Legg gjerne bildene i en egen bildemappe, slik som på bildet nedenfor.

![Bilder i VS Code](bilder-vs-code.png ':size=400')

Når bildene ligger lagret på PCen må vi lagre filnavnet i databasen, slik som på bildet under.

![Bilder i firestore](bilder-firestore.png)

Etter at filnavnet til bildet ligger i firestore kan vi hente det ut sammen med resten av dataen vi henter fra databasen.

![Bilder kode](bilder-kode.png)

Legg merke til "bilder/", dette er fordi bildene ligger i mappen bilder.

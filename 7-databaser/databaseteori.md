# Statiske og Dynamiske Nettsider

Nettsidene vi har laget hittil har vært **statiske**. Det betyr at de ser ut nøyaktig slik vi har laget de, og vil dermed være like for alle brukere. De kan kun endres dersom vi går inn i html-filene og gjør endringene der. Mange av nettsidene du vanligvis besøker er ikke statiske, de er **dynamiske**. Det betyr at innholdet du ser på nettsiden, ikke nødvendigvis er det samme som andre. Ta for eksempel youtube og netflix. Begge har forslag til videoer basert på dine preferanser. Selv om for eksempel du og dine foreldre er på samme nettside, er sjansen veldig stor for at dere ser forskjellig innhold på siden. Nettsiden er altså dynamisk og velger ut innhold dere ser basert på blant annet historikk og preferanser. 

Et annet eksempel kan være nettsider der man kan poste egne meldinger eller skrive anmeldelser. Her blir det håpløst dersom utvikleren av nettsiden må ta imot tekstene for å så manuelt legge de til. Da må prosessen automatiseres. Meldingene må lagres et sted, slik at nettsiden automatisk kan hente de frem og vise de på skjermen der det trengs.

Istedet for at alle komponentene til nettsiden ligger i html-fila, lagrer altså vi deler av den et annet sted i skyen. Så bygger vi opp nettsiden slik at den kan hente de delene den trenger slik vi ønsker det. Dermed er nettsiden dynamisk, og vil kunne se anderledes ut for ulike brukere.

 En nettbutikk vil for eksempel lagre alle varene sine utenfor html fila. Hvis du besøker den og søker etter blå jakker av et spesifikt merke, vil den kunne hente de aktuelle varene og vise de på nettsiden. Dermed slipper utviklerene å lage en egen side for blå jakker.  
 
 For å lage slike nettsider trenger vi altså et sted å lagre det innholdet som skal være dynamsik. Til det bruker vi **databaser**. I tillegg må vi vite hvordan nettsiden kommuniserer med databasen vår. Innenfor Informasjonsteknologien er en slik håndtering av data et stort område, og i resten av kapittelet ser vi litt nærmere på teorien som ligger til grunn.


 # Database - Lagring av Data

De fleste virksomheter har behov for å lagre data. Det kan være informasjon om kunder, pasienter, varebeholdning, bevis etc, listen er lang. Tidligere ble alt lagret fysisk i ulike arkiv. Informasjonen måtte da være systematisert på en måte slik at det ble lett å finne frem. Nå som de fleste bedrifter har digitalisert informasjonen, er den i stedet lagret i skyen (eller på egne servere). Informasjonen må fortsatt lagres på en god måte for at vi skal finne frem. 

I tillegg må vi ha et system som lar oss kommunisere med serveren, slik at vi kan:

* Lagre nye data
* Hente frem data
* Endre data
* Slette data 

Allerede på 1970-tallet utviklet man et språk for å håndtere denne digitaliseringen. Språket kalles for **SQL** (Structured Query Language). Med SQL følger det med regler for hvordan informasjonen bør struktureres og lagres.

I senere tid har det også kommet andre alternative måter å håndtere databaser på, ofte med større frihet. Disse ulike alternativene går under sekkebegrepet **NoSQL**. 

Nå til dags er det en jungel av ulike løsninger som kan hjelpe oss, både innen SQL og NoSQL. Det blir opp til hver enkelt utvikler/bedrift å avgjøre hvilket system man vil bruke (eller om man vil programmere sitt eget system).

Resten av dette kapittelet så skal vi se nærmere på hvordan vi best bør systematisere informasjonen. I neste kapittel skal så vi gå gjennom et eksempel på hvordan vi kan gjennomføre det i praksis, og dermed lage dynamiske nettsider.
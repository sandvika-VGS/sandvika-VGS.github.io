# Statiske og Dynamiske Nettsider

Nettsidene vi har laget hittil har vært **statiske**. Det betyr at de ser ut nøyaktig slik vi har laget de, og vil dermed være like for alle brukere. De kan kun endres dersom vi går inn i html-filene og gjør endringene der. Mange av nettsidene du besøker er ikke statiske, de er **dynamiske**. Det betyr at innholdet du ser på nettsiden, ikke nødvendigvis er det samme som andre. Ta for eksempel youtube og netflix. Begge har forslag til videoer basert på dine preferanser, og disse forslagene vil variere fra person til person. Et annet eksempel er nettbutikker der du er i stand til å vise varer etter mange ulike kategorier. For begge eksemplene blir det håpløst om de som lager nettsidene skal lage alle de forskjellige variantene på egenhånd. Et tredje eksempel kan være nettsider der man kan poste egne meldinger eller skrive anmeldelser. Her blir det håpløst å måtte ta imot tekstene for å så manuelt legge de til nettsiden. Alle disse er eksempler på dynamiske nettsider. Istedet for at alle komponentene til nettsiden ligger i html-fila, lagrer vi deler av den et annet sted i skyen. Så bygger vi nettsiden slik at den kan hente de delene den trenger fra skyen, og dermed vil nettsiden kunne se anderledes ut for ulike brukere.

 Nettbutikken vil for eksempel lagre alle varene sine utenfor html fila. Hvis du besøker den og søker etter blå jakker av et spesifikt merke, vil den hente de aktuelle varene og vise de på nettsiden. For å lage dynamiske nettsider trenger vi altså et sted å lagre de ulike komponentene. Til det bruker vi **databaser**. Databaser er et stort og viktig emne innenfor Informasjonsteknologi, og spenner mye lengre enn det å lage nettsider. I resten av kapittelet ser vi derfor på noe av teorien bak databaser.

 # Database - Lagring av Data

De fleste virksomheter har behov for å lagre data. Det kan være informasjon om kunder, pasienter, varebeholdning, bevis og så videre. Listen er lang. Tidligere ble alt lagret fysisk i arkiv. Når det var snakk om store mengder informasjon, måtte alt være lagret på en måte slik at det ble lett å finne frem til det vi trenger. Nå som de fleste har digitalisert informasjonen, er den i stedet lagret i skyen eller på virksomhetens egen server. Dataene må fortsatt lagres på en god måte for at vi skal finne frem. Vi må ha et system som lar oss kommunisere med serveren, og systemet må la oss gjøre følgende:

* Lagre nye data
* Hente frem data
* Endre data
* Slette data 

Allerede på 1970-tallet utviklet man et språk for å håndtere overnevnte kommunikasjon med databaser. Dette kalles for **SQL** (Structured Query Language). Med SQL følger det med regler for hvordan databasene bør struktureres og lagres. I senere tid har det også kommet andre alternative måter å håndtere databaser på, ofte med større frihet på hvordan dataene skal lagres. Disse ulike alternativene går under sekkebegrepet **NoSQL**. Nå til dags er det en jungel av ulike løsninger både innen SQL og NoSQL, og det blir opp til hver enkelt utvikler/bedrift å avgjøre hvilket system man vil bruke (eller om man vil programmere sitt eget system).

Uansett hva vi bruker så bør vi lære oss god skikk for å lagre data. Det blir fort så store mengder og uoversiktlig at vi bør lage oss en **datamodell** på forhånd.
# En dårlig modell

Anta at du får i oppdrag til å lage en datamodell for en burgerkjede med flere filialer. Arbeidsgiver vil gjerne ha informasjon om de ansatte og hvilken avdeling de jobber på. De må også ha kontaktinformasjon til hver avdeling. Dersom du ikke er ferdig med IT-1 faget er det naturlig å foreslå en modell som på figuren under. Denne modellen er ikke spesielt god, noe vi må se nærmere på.

BIlde

Når modellen skal implementeres husker vi at vi skal kunne legge til nye data, endre eksisterende data og eventuelt slette data. La oss undersøke hvilke problemer for disse situasjonene:

* Legge til data: Dersom man skal legge til en nyansatt må man alltid føre på informasjon om avdelingen på nytt. Vi vil helst unngå å dobbeltlagre informasjon. Sjansen for at noen skriver feil øker for hver gang. Det vil skape problemer for en nyansatt, dersom vedkommende for eksempel ikke finnes i noen avdeling som følge av at noen tastet inn feil.

* Slette data: Se på det nederste objektet på figuren. Avdelingen til Art Vandelay er nyopprettet og det er kun han som er ansatt der. Dersom Art slutter, må vi slette objektet fra databasen. Problemet med er at da forsvinner hele avdelingen!

* Endre data: Se for deg at avdelingen på Billingstad har 20 ansatte. Dersom vi skal endre telefonnummer til avdelingen, må vi inn i alle 20 objektene for å endre det. Det medfører mye ekstraarbeid og øker sjansen for feil.

Det som er problematisk med modellen ser altså ut til å være at vi har koblet sammen informasjon om ansatte med informasjon om avdelingen. Løsningen må være å separere informasjonen i to forskjellige tabeller, for så på en eller annen måte å koble de sammen. Vi må lære oss å lage en **relasjonsmodell**

# Relasjonsmodeller

La oss se på et par andre litt enklere eksempler.

## En til en relasjon
Bilde

 I den første figuren har vi skilt ut informasjon om land og hovedsteder i to ulike tabeller. Vi kan nå for eksempel koble disse sammen med å legge til primærnøkkelen til land i tabellen for hovedstad. Denne kalles da en **fremmednøkkel**. Dersom vi søker opp en hovedstad kan vi samtidig søke opp landet med primærnøkkel som tilsvarer verdien i fremmednøkkel-feltet. Alternativt dersom vi søker opp en hovedstad, kan vi samtidig be om landet med den riktige primærnøkkelen. I dette eksempelet er kan et land kun ha en hovedstad. Tilsvarende hører en hovedstad kun til ett land. Dermed har vi en **en til en** relasjon mellom tabellene. Vi tar med relasjonene ved å sette opp modellen som vist på figuren:

Bilde

## En til mange relasjon

Neste eksempel er en veterinærklinikk som vil ha oversikt over kundene sine. De velger å skille informasjon om dyr og eiere i to tabellern. For enkelhets skyld sier vi at et dyr kun kan ha en eier. Eieren derimot kan ha mange dyr. Vi har da en **en til mange** relasjon. I eksempelet med land og hovedstad, kunne vi velge hvor vi satte fremmednøkkelen, men det kan vi ikke nå lenger. Dersom vi hadde satt en fremmednøkkel for dyrene hos eier, kunne vi hatt flere innføringer i samme felt, og det følger ikke atomærkravet. Vi må derfor sette eier som fremmednøkkel hos dyrene, og det gir oss følgende modell:

bilde

## Mange 

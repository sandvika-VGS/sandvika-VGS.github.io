# En dårlig modell

Anta at du får i oppdrag til å lage en datamodell for en burgerkjede med flere filialer. Arbeidsgiver vil gjerne ha informasjon om de ansatte og hvilken avdeling de jobber på. De må også ha kontaktinformasjon til hver avdeling. Dersom du ikke er ferdig med IT-1 faget er det naturlig å foreslå en modell som kan ligne på noe av følgende:

BIlde

Når modellen skal implementeres husker vi at vi skal kunne legge til nye data, endre eksisterende data og eventuelt slette data. La oss se nærmere på hvorfor denne modellen medfører problemer på alle områder:


* Legge til data: Dersom man skal legge til en nyansatt må man alltid føre på informasjon om avdelingen på nytt. Vi vil helst unngå å dobbeltlagre informasjon. Sjansen for at noen skriver feil øker for hver gang. Det vil skape problemer for en nyansatt, dersom denne ikke finnes i noen avdeling som følge av at noen tastet inn feil.

* Slette data: Avdelingen til Art Vandelay er nyopprettet og det er kun lederen som er ansatt der. Dersom Art slutter, må vi slette objektet fra databasen. Problemet med er at da forsvinner hele avdelingen!

* Endre data: Se for deg at avdelingen på Billingstad har 20 ansatte. Dersom vi skal endre telefonnummer til avdelingen, må vi inn i alle 20 objektene for å endre det. Det medfører mye ekstraarbeid og øker sjansen for feil.

Det som er problematisk med modellen ser altså ut til å være at vi har koblet sammen informasjon om ansatte med informasjon om avdelingen. Løsningen må være å separere informasjonen i to forskjellige tabeller. Vi må da lære oss å lage en **relasjonsmodell**

# Relasjonsmodeller
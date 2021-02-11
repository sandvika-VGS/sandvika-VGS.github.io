# Piksler

Vi skal nå se på hvordan vi kan lagre et bilde som en rekke med 0 og 1. Da må vi først se nærmere på hvordan et bilde egentlig er bygd opp på datamaskinen. Velg deg et bilde du selv har lagret og zoom inn så langt du klarer. Det vil etterhvert se ut som en rekke med fargede firkanter:

BILDE: Zoom inn på piksler

Hver firkant kalles for en **piksel** eller et bildepunkt. Oppløsningen et bilde har tilsvarer antall piksler i bredden og høyden, et bilde med oppløsning 1200x1000 har altså 1200 piksler i bredden og 1000 i høyden. Det tilsvarer totalt 1200 000 piksler, altså "firkanter" med hver sin farge. Vi kan tenke oss at dersom vi klarer å gjøre hver piksel sin farge om til 0 og 1, så kan vi lagre disse fargene i en bestemt rekkefølge som bits eller bytes. Da vil programmet som skal vise bildet kunne lese en kjempelang rekke med 0 og 1, gjøre de om til farger, så til slutt å sette de sammen i den riktige rekkefølgen. 

## Farger



I forrige delkapittel så vi på et eksempel på et 8 bits system der vi hadde 8 strømbrytere vi kunne skru av og på. Vi regnet oss frem til at det da var 256 mulige kombinasjoner bryterene kunne ha. Det kan være lurt å gjøre en slik rekke med 0 og 1 om til et vanlig tall. For eksempel bør det jo være slik at hvis vi skrur på alle bryterene: 
> 1111 1111 
så tilsvarer det 256.

Vi må altså kunne regne tall gitt på et totallssystem om til et titallssystem. La oss først se litt nærmere på hvordan titallssystemet vi er veldig vant med egentlig fungerer. Vi kaller det for titallssystemet fordi vi har 10 unike symboler for tall vi kan bruke (fra 0 til 9). Når vi har kommet til tallet 9 har vi "brukt opp" symbolene våre og setter dermed et 1 tall på "tierplassen" og 0 på enerplassen. Symbolkombinasjonen 1 og 0, altså 10, lærer vi allerede som barn at tilsvarer 10. Trolig er det fordi det er naturlig å telle på fingrene at menneskeheten utviklet et titallssystem (Mayaindianerene brukte et 20 tallsystem, kan du tenke deg hvorfor?).

I et femtallsystem har man bare 5 unike symboler altså 0 1 2 3 4. Når vi har kommet til 4 har vi altså "brukt opp" symbolene våre og må skrive 10. Det indikerer at vi har 1 på **femmer** plassen og 0 enere. Vi teller altså som følger i et femtallsystem:

| Femtallssystemet | Titallssystemet |
|------------------|-----------------|
|0                 |0                |
|1                 |1                |
|2                 |2                |
|3                 |3                |
|4                 |4                |
|10                |5                |
|11                |6                |
|...               |...              |
|14                |9                |
|20                |10               |
|21                |11               |
|...               |...              |
|44                |24               |
|100               |25               |

I et totallssystem er logikken helt lik, vi har bare to unike symboler, nemlig 0 og 1. Når vi har "brukt opp" disse må vi introdusere en ny plass, altså toerplassen. Tabellen vil da se slik ut:

| Totallssystemet | Titallssystemet |
|------------------|-----------------|
|0                 |0                |
|1                 |1                |
|10                |2                |
|11                |3                |
|100               |4                |
|101               |5                |
|110               |6                |
|111               |7                |
|1000              |8                |
|...               |...              |
|1111 1111         |256              |

# Oppgaver med løsning

## Variabler og Datatyper



#### Oppgave 1.1

Print ut noen selvvalgte beskjeder. Prøv å se hva som skjer dersom du glemmer anførselstegnene.



#### Oppgave 1.2 

a ) Hva tror du skjer dersom vi kjører følgende kode? 

```PYTHON
a = 2
print(a + 2)
``` 

b) Hvorfor er det ingen anførselstegn i print-instruksjonen denne gangen?

<details>
    <summary>Klikk for Løsning</summary>

    Koden printer ut 4. Vi kan ikke bruke anførselstegn fordi det ikke er en streng vi skal printe ut

</details>



#### Oppgave 1.3

Se på følgende kode:

```PYTHON
lengde = 5
bredde = 7

areal = lengde*bredde

print("Arealet av rektangelet er", areal)
```
Hvorfor bruker vi variable for lengde og bredde? Kunne vi ikke bare ha skrevet arealet rett inn i print-funksjonen?

<details>
    <summary>Klikk for Løsning</summary>

    Variable gir bedre oversikt når man leser koden. Dersom man ønsker å regne areal for et annet rektangel er det mye lettere å endre på verdien på variablene enn å gå inn i resten av koden for å endre på tallene. Dette blir spesielt viktig jo større koden er.

</details>



#### Oppgave 1.4

Spør den du sitter nærmest om alder. Lagre både navn og alder i to forskjellige variabler. Print en tekst som skriver ut følgende tekst rikig: Hei *navn*, du er *alder* år.

<details>
    <summary>Klikk for Hint</summary>

    Lag et input-felt for navn og alder. Husk komma i mellom strenger og variable når du printer ut
</details>

<details>
    <summary>Klikk for Løsning</summary>

    navn = input("Hva heter du? ")
    alder = input("Hvor gammel er du? ")

    print("Hei", navn, "du er", alder, "år")

</details>



#### Oppgave 1.5

![oppgave 5](./oppgave_5.png)

a) Forklar hva som er galt med denne koden? Hvorfor blir det feil? Rett opp koden slik at den kjører 

b) Skriv adressen ut på følgende to måter ved å bruke variabler: "Adressen er Kongens gate 432b" og "Gaten er Kongens Gate, husnummeret er 432, oppgang b" 

<details>
    <summary>Klikk for Løsning</summary>

    a) I linje 3 er b skrevet uten anførselstegn. Da leter programmet etter en variabel som heter b, somn ikke finnes.

    b) 
    
    gate = "Kongens gate"
    husnr = "432"
    oppgang = "b"

    print("Adressen er", gate + husnummer + oppgang)
    print("Gaten er", gate, ", husnummeret er", husnr, "oppgang", oppgang)

</details>



#### Oppgave 1.6

Du er på restaurant med venner, og på regningen er følgende informasjon:

Total pris for mat og drikke: 850 kr
Ungdomsrabatt: 25 % 
Tips: 10 %

a) Legg informasjonen inn i variabler som tall (ikke bruk %, det gir ikke mening når vi programmerer)

b) Bruk variablene for total pris og ungdomsrabatt til å regne ut rabatten.

c) Trekk fra rabatt og bruk så variabelen for tips til å regne ut tips. 

d) Legg på tips, og skriv ut summen for måltidet etter både rabatt og tips 

e) Lag en variabel for antall personer, og skriv ut pris per person samt antall personer.

<details>
    <summary>Klikk for Hint</summary>
    - Lag de tre variablene
    - Husk prosentformlene: pris*rabatt/100 gir selve rabatten
    - Lag egne variable for alle mellomregningen.
    - Bruk mellomregningene til å regne ut det som skal betales
    - print ut alle variable du er usikre på underveis så er det lettere å finne ut om matematikken stemmer

</details>
<details>
    <summary>Klikk for Løsning</summary>

    pris = 850
    rabatt_prosent = 25
    tips = 10
    ant_pers = 3

    rabatt_kr = pris*rabatt_prosent/100
    tips_kr = pris*tips_kr

    totalt = pris - rabatt_kr + tips_kr
    per_pers = totalt/ant_pers

    print("Pris etter rabatt og tips er", totalt, "det blir", per_pers, "kr per person")

</details>
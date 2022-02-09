# Her regner vi tips før rabatt, man kan argumentere for at det kan gjøres motsatt

pris = 850
rabatt_prosent = 25
tips_prosent = 10
ant_pers = 3

rabatt_kr = pris*rabatt_prosent/100
tips_kr = pris*tips_prosent/100

totalt = pris - rabatt_kr + tips_kr
per_pers = totalt/ant_pers

print("Pris etter rabatt og tips er", totalt,
      "det blir", per_pers, "kr per person")

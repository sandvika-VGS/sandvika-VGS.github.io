# Her regner vi tips før rabatt, man kan argumentere for at det kan gjøres motsatt

print("-- Restaurantkalkulatoren --")
pris = float(input("Pris (kr): "))
rabatt_prosent = float(input("Rabatt (%): "))
tips_prosent = float(input("Tips (%): "))
ant_pers = float(input("Antall personer: "))

rabatt_kr = pris*rabatt_prosent/100
tips_kr = pris*tips_prosent/100

totalt = pris - rabatt_kr + tips_kr
per_pers = totalt/ant_pers

print("Pris etter rabatt og tips er", totalt,
      "det blir", per_pers, "kr per person")

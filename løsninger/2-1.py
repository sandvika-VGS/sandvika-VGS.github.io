hemmelig_tall = 4

print("Hvilket tall tenker jeg på? Gjett et tall mellom 1 og 10")
gjett = int(input("Ditt tall: "))

if gjett == hemmelig_tall:
    print("Gratulerer! Du gjettet riktig")
else:
    print("Beklager, du gjettet feil")
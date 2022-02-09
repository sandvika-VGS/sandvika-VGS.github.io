#priser

brød = 20
melk = 15
ost = 40
youghurt = 12

# handling
print("-- Velkommen til IT-butikken --")
print("Hvor mange brød vil du ha?")
ant_brød = int(input("> "))
print("Hvor mange melk vil du ha?")
ant_melk = int(input("> "))
print("Hvor mange oster vil du ha?")
ant_ost = int(input("> "))
print("Hvor mange yoghurt vil du ha?")
ant_yoghurt = int(input("> "))

# utregning av pris
pris = brød * ant_brød + melk * ant_melk + ost * ant_ost + youghurt * ant_yoghurt
print("Du skal betale ", pris, " kr.")
print("-- Takk for handelen --")
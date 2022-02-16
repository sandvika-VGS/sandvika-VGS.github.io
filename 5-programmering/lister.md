# Lister

```python
skole_liste = ["Sandvika", "Valler", "Nesbru"]
karakter_liste = [4, 3, 2]
```

| skole_liste | `"Sandvika"` | `"Valler"` | `"Nesbru"` |
| ----------- | ------------ | ---------- | ---------- |
| indeks      | 0            | 1          | 2          |

| Metode / Operasjon               | Resultat                                      | Beskrivelse                                       |
| -------------------------------- | --------------------------------------------- | ------------------------------------------------- |
| `skole_liste[1]`                 | `"Valler`                                     | Hent ut det som ligger på indeks `1`              |
| `skole_liste[2] = "Stabekk" `    | `["Sandvika", "Valler", "Stabekk"]`           | Sett det som ligger på indeks `2` til `"Stabekk"` |
| `skole_liste[-1]`                | `"Nesbru"`                                    | Hent ut det som ligger `-1` fra slutten av listen |
| `skole_liste[-2]`                | `"Valler"`                                    | Hent ut det som ligger `-2` fra slutten av listen |
| `len(skole_liste)`               | `3`                                           | Lengden av listen                                 |
| `skole_liste + karakter_liste`   | `["Sandvika", "Valler", "Stabekk", 4, 3, 2]`  | Slå sammen lister                                 |
| `"Valler" in skole_liste`        | `True`                                        | Sjekk om noe er i listen                          |
| `"Nesbru" not in skole_liste`    | `False`                                       | Sjekk om noe ikke er i listen                     |
| `skole_liste.index("Sandvika")`  | `0`                                           | Finn plassering til noe i listen                  |
| `skole_liste.append("Stabekk")`  | `["Sandvika", "Valler", "Nesbru", "Stabekk"]` | Legg noe til på slutten av listen                 |
| `skole_liste.insert(1, "Rud")`   | `["Sandvika", "Rud", "Valler", "Nesbru"]`     | Sett noe inn i listen på en gitt indeks           |
| `skole_liste.remove("Valler")`   | `["Sandvika", "Nesbru"]`                      | Fjern noe fra listen                              |
| `skole_liste.sort()`             | `["Nesbru", "Sandvika", "Valler"]`            | Sorter listen etter ASCII-tabellen                |
| `skole_liste.sort(reverse=True)` | `["Valler", "Sandvika", "Nesbru"]`            | Sorter listen motsatt vei etter ASCII-tabellen    |
| `" og ".join(skole_liste)`       | `"Valler og Sandvika og Nesbru"`              | Slår listen sammen til en tekst                   |
| `",".join(skole_liste)`          | `"Valler,Sandvika,Nesbru"`                    | Slår listen sammen til en tekst                   |

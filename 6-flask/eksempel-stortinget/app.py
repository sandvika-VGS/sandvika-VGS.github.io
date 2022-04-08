from flask import Flask, render_template
import json # importerer json-biblioteket, som lar oss bruke ferdiglagde funksjoner for å jobbe med json-filer

app = Flask(__name__)

fil = open("politikere.json", encoding="utf8") # åpner fila politikere.json som tekst
politikere = json.load(fil) # tolker innholdet i "fil" som en json-fil, polikere er nå en ordbok
fil.close() # lukker fila fil

#favoritter = ["trygve", "bjornar", "sylvi", "audun"]
fil_favoritter = open("favoritter.json", encoding="utf8")
favoritter = json.load(fil_favoritter)
fil_favoritter.close() # lukker fila fil_favoritter


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/politikere")
def rute_politikere():
    return render_template("politikere.html", politikere=politikere)

@app.route("/politiker/<id>")
def rute_politiker(id):
    politiker = politikere[id]
    return render_template("politiker.html", politiker=politiker, id=id)

@app.route("/favoritter")
def rute_favoritter():
    return render_template("favoritter.html", favoritter=favoritter, politikere=politikere)

@app.route("/politiker/legg-til/<id>")
def rute_legg_til(id):
    favoritter.append(id)

    fil_favoritter = open("favoritter.json", "w") # åpner fila favoritter.json
    json.dump(favoritter, fil_favoritter) # legger favorittlisten i fila fil_favoritter
    fil_favoritter.close() # lukker fila fil_favoritter

    return rute_politiker(id)


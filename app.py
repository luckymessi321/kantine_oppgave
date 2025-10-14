from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/meny')
def meny():
    return render_template("meny.html", day = datetime.datetime.now().strftime("%A"), target_key = "rett", target_key2 = "beskrivelse", list = [{"Monday": "Mandag", "Tuesday": "Tirsdag", "Wednesday": "Onsdag", "Thursday": "Torsdag", "Friday": "Fredag"}, {"Mandag": {"rett": "Pølse", "beskrivelse": "Pølse i brød"},
                                                                                                                                                                                                                                                               "Tirsdag": {"rett": "Pizza", "beskrivelse": "Pizza med pepperoni og maur"},
                                                                                                                                                                                                                                                               "Onsdag": {"rett": "Burger", "beskrivelse": "Burger med hundekjøtt"},
                                                                                                                                                                                                                                                               "Torsdag": {"rett": "Skorpion", "beskrivelse": "Skorpion med navnet Skarner"},
                                                                                                                                                                                                                                                               "Fredag": {"rett": "Ræv", "beskrivelse": "Ræva til moren din"}}])

@app.route('/kontakt')
def kontakt():
    return render_template("kontakt.html")

@app.route('/varer')
def varer():
    return render_template("varer.html")

if __name__ == "__main__":
    app.run()

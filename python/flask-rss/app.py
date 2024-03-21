from flask import Flask, request, render_template
from flask import request
import feedparser

app = Flask(__name__)

@app.route("/demo0")
def demo0():
    return "<h1>Hola món!</h1>"

@app.route("/demo1")
def demo1():
    return render_template("hola.html")

@app.route("/demo2")
def demo2():
    return render_template("demo.html", nom = "Lola", edat=6)

@app.route("/demo3/<nom>/<int:edat>")
def demo3(nom, edat):
    return render_template("demo.html", nom = nom, edat = edat)

@app.route("/demo4")
def demo4():
    nom = request.args.get('nom', default = "Desconegut/a", type = str)
    edat = request.args.get('edat', default = 0, type = int)
    return render_template("demo.html", nom = nom, edat = edat)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/lavanguardia/<seccio>')
def lavanguardia(seccio):
    rss = get_rss_lavanguardia(seccio)
    return render_template("lavanguardia.html", rss = rss)

def get_rss_lavanguardia(seccio):
    # versió on descarrega l'XML de la web
    # xml = f"https://www.lavanguardia.com/rss/{seccio}.xml"
    
    # versió que fa servir l'XML descarregat
    xml = f"./rss/lavanguardia/{seccio}.xml"
    
    rss = feedparser.parse(xml)
    return rss

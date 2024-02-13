from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from datetime import datetime
from urllib.request import urlopen
import sqlite3

app = Flask(__name__)                                                                                                                  

@app.route('/tawarano/')
def meteo():
    response = urlopen('https://samples.openweathermap.org/data/2.5/forecast?lat=0&lon=0&appid=xxx')
    raw_content = response.read()
    json_content = json.loads(raw_content.decode('utf-8'))
    results = []
    for list_element in json_content.get('list', []):
        dt_value = list_element.get('dt')
        temp_day_value = list_element.get('main', {}).get('temp') - 273.15 # Conversion de Kelvin en °c 
        results.append({'Jour': dt_value, 'temp': temp_day_value})
    return jsonify(results=results)
    
@app.route("/contact/")
def MaPremiereAPI():
    return render_template("contact.html")

@app.route("/rapport/")
def mongraphique():
    return render_template("graphique.html")

@app.route('/paris/')
def get_paris_weather():
    response = urlopen('https://samples.openweathermap.org/data/2.5/forecast?lat=48.8566&lon=2.3522&appid=xxx')
    raw_content = response.read()
    json_content = json.loads(raw_content.decode('utf-8'))
    results = []
    for list_element in json_content.get('list', []):
        dt_value = list_element.get('dt')
        temp_day_value = list_element.get('main', {}).get('temp') - 273.15  # Conversion de Kelvin en °c 
        results.append({'Jour': dt_value, 'temp': temp_day_value})
    return jsonify(results=results)

@app.route('/commits/')
def get_commit_minutes():
    # URL de l'API GitHub pour les commits du projet
    url = "https://api.github.com/repos/OpenRSI/5MCSI_Metriques/commits"

    # Récupération des données depuis l'API GitHub
    response = requests.get(url)
    commits_data = response.json()

    # Extraction des minutes de chaque commit
    commits_minutes = [extract_minutes(commit['commit']['author']['date']) for commit in commits_data]

    # Création du format JSON avec les minutes des commits
    results = [{'minute': minute} for minute in commits_minutes]
    
    return jsonify(results=results)
    
@app.route("/histogramme/")
def monhisto():
    return render_template("histo.html")

@app.route('/')
def hello_world():
    return render_template('hello.html') #commentaire
  
if __name__ == "__main__":
  app.run(debug=True)

from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from datetime import datetime
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  

@app.route("/contact/")
def MaPremiereAPI():
    return "<h2><!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page de contact</title>
</head>
<body>
    <h2>Ma page de contact</h2>
    <p>Vous pouvez me contacter via les informations suivantes :</p>
    <ul>
        <li>Adresse e-mail : votre@email.com</li>
        <li>Numéro de téléphone : +33 1 23 45 67 89</li>
        <li>Adresse postale : 123 rue de la Contacterie, 75000 Paris, France</li>
    </ul>
    <h3>Formulaire de contact :</h3>
    <form action="/envoyer-message" method="post">
        <label for="nom">Nom :</label><br>
        <input type="text" id="nom" name="nom"><br>
        <label for="email">E-mail :</label><br>
        <input type="email" id="email" name="email"><br>
        <label for="message">Message :</label><br>
        <textarea id="message" name="message" rows="4" cols="50"></textarea><br>
        <input type="submit" value="Envoyer">
    </form>
    <p>Merci de me contacter, je répondrai dans les plus brefs délais.</p>
</body>
</html>
</h2>"

@app.route('/')
def hello_world():
    return render_template('hello.html') #commentaire
  
if __name__ == "__main__":
  app.run(debug=True)

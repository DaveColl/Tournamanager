#importiert die libraries um Flask zu verwenden und HTML-Dateien zu rendern
from flask import Flask , render_template

# Initialisiert die Flask-Instanz von der Flask-Klasse und erstellt eine neue Flask-Anwendung
app = Flask(__name__)

# Definiert die Route für die Startseite der Anwendung und gibt die index.html-Datei zurück
@app.route('/')
# Die Funktion index() wird aufgerufen, wenn die Startseite aufgerufen wird
def index():
    return render_template('index.html')

#Startet die Flask-Anwendung, wenn das Skript direkt ausgeführt wird. Der Debug-Modus ist aktiviert und die Anwendung ist auf allen Netzwerkadressen verfügbar.
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
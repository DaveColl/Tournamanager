#importiert die libraries um Flask zu verwenden, HTML-Dateien zu rendern und das Backend aufzurufen
from flask import Flask, render_template
import requests

# Initialisiert die Flask-Instanz von der Flask-Klasse und erstellt eine neue Flask-Anwendung
app = Flask(__name__)

# Adresse des Backends im Docker-Netzwerk. "backend" ist der Servicename aus der
# docker-compose.yml - Docker löst diesen Namen automatisch zur richtigen
# Container-IP auf, wir müssen also keine feste IP-Adresse eintragen.
BACKEND_URL = 'http://backend:5000/api/status'

# Definiert die Route für die Startseite der Anwendung
@app.route('/')
def index():
    # Ruft das Backend direkt aus Python auf (Server-zu-Server), statt das dem
    # Browser per JavaScript zu überlassen. So bleibt das ganze Projekt in
    # einer einzigen Programmiersprache (Python).
    try:
        response = requests.get(BACKEND_URL, timeout=3)
        backend_data = response.json()
    except requests.exceptions.RequestException:
        # Wird ausgelöst, wenn das Backend nicht erreichbar ist (z.B. noch
        # nicht gestartet oder abgestürzt)
        backend_data = None

    # Übergibt die Backend-Daten an die HTML-Vorlage, die sie mit Jinja
    # (den {{ }}-Platzhaltern) in der Seite anzeigt
    return render_template('index.html', backend_data=backend_data)

#Startet die Flask-Anwendung, wenn das Skript direkt ausgeführt wird. Der Debug-Modus ist aktiviert und die Anwendung ist auf allen Netzwerkadressen verfügbar.
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

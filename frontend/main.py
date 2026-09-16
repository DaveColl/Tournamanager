#importiert die libraries um Flask zu verwenden, HTML-Dateien zu rendern und das Backend aufzurufen
from flask import Flask, render_template
import requests

# Initialisiert die Flask-Instanz von der Flask-Klasse und erstellt eine neue Flask-Anwendung
app = Flask(__name__)

# Adresse des Backends im Docker-Netzwerk. "backend" ist der Servicename aus der
# docker-compose.yml - Docker löst diesen Namen automatisch zur richtigen
# Container-IP auf, wir müssen also keine feste IP-Adresse eintragen.
BACKEND_URL = 'http://backend:5000/api/status'


def get_backend_status():
    # Ruft das Backend direkt aus Python auf (Server-zu-Server). Wird sowohl
    # beim ersten Laden der Seite (index) als auch bei jeder Aktualisierung
    # (status_fragment) benutzt, damit die Logik nur an einer Stelle steht.
    try:
        response = requests.get(BACKEND_URL, timeout=3)
        return response.json()
    except requests.exceptions.RequestException:
        # Wird ausgelöst, wenn das Backend nicht erreichbar ist (z.B. noch
        # nicht gestartet oder abgestürzt)
        return None


# Definiert die Route für die Startseite der Anwendung
@app.route('/')
def index():
    return render_template('index.html', backend_data=get_backend_status())


# Wird von einem kleinen JavaScript-Schnipsel auf der Seite alle 30 Sekunden
# aufgerufen. Gibt - anders als eine JSON-API - fertiges HTML zurück, das die
# Seite direkt per innerHTML einsetzt. Dadurch bleibt die komplette Logik
# (was angezeigt wird) in Python/Jinja, JavaScript muss nichts "verstehen".
@app.route('/status-fragment')
def status_fragment():
    return render_template('status_fragment.html', backend_data=get_backend_status())


#Startet die Flask-Anwendung, wenn das Skript direkt ausgeführt wird. Der Debug-Modus ist aktiviert und die Anwendung ist auf allen Netzwerkadressen verfügbar.
if __name__ == '__main__':
    app.run(host='0.0.0.0')

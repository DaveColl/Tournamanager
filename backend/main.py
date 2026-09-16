#importiert die libraries um Flask zu verwenden und JSON-Antworten zu erstellen
from flask import Flask, jsonify

# Initialisiert die Flask-Instanz von der Flask-Klasse und erstellt eine neue Flask-Anwendung
# Das Frontend wird separat (per nginx) ausgeliefert, das Backend dient nur noch als JSON-API
app = Flask(__name__)

# Healthcheck-/Status-Endpunkt, den das Frontend abfragen kann, um die Verbindung zu prüfen
@app.route('/api/status')
def status():
    return jsonify(status='ok', service='tournamanager-backend')

#Startet die Flask-Anwendung, wenn das Skript direkt ausgeführt wird. Der Debug-Modus ist aktiviert und die Anwendung ist auf allen Netzwerkadressen verfügbar.
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
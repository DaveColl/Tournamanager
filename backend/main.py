import random
import pymysql

#importiert die libraries um Flask zu verwenden und JSON-Antworten zu erstellen
from flask import Flask, jsonify

# Initialisiert die Flask-Instanz von der Flask-Klasse und erstellt eine neue Flask-Anwendung
# Das Frontend läuft als eigener Container und ruft dieses Backend serverseitig
# (Python zu Python, über das Docker-Netzwerk) auf. Das Backend dient nur noch
# als JSON-API und liefert selbst kein HTML aus.
app = Flask(__name__)

# Healthcheck-/Status-Endpunkt, den das Frontend abfragen kann, um die Verbindung zu prüfen
@app.route('/api/status')
def status():
    return jsonify(status='ok', service='tournamanager-backend')

# Hier startet der Randomizer für die ersten Matches.
def get_db_connection():
    return pymysql.connect(
        host='database',
        user='Turnier_Admin',
        password='?bBxar1v{V1>Ty/h-qH',
        database='Turnier_DB',
        cursorclass=pymysql.cursors.DictCursor,
    )

@app.route("/randomize_matches", methods=["POST"])
def randomize_matches():
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT TEAM_ID, Team_Name FROM Teams")
        teams = cursor.fetchall()

        if len(teams) < 2:
            return jsonify({"error": "Not enough teams to create matches."}), 400

        random.shuffle(teams)
        cursor.execute("TRUNCATE TABLE Matches")  # Löscht alle bisherigen Matches

        for i in range(0, len(teams) - 1, 2):
            Team_ID1 = teams[i]['TEAM_ID']
            Team_ID2 = teams[i + 1]['TEAM_ID']

            cursor.execute(
                "INSERT INTO Matches (Team_ID1, Team_ID2) VALUES (%s, %s)",
                (Team_ID1, Team_ID2)
            )

        conn.commit()
        return jsonify({"message": "Matches randomized successfully."}), 200

    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500

    finally:
        cursor.close()
        conn.close()

#Startet die Flask-Anwendung, wenn das Skript direkt ausgeführt wird. Der Debug-Modus ist aktiviert und die Anwendung ist auf allen Netzwerkadressen verfügbar.
if __name__ == '__main__':
    app.run(host='0.0.0.0')
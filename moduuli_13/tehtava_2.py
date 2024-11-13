from flask import Flask, jsonify
import mysql.connector

conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='turvallinenrootsalasana',
        database='flight_game',
        collation='utf8mb4_unicode_ci',
    )

app = Flask(__name__)
@app.route('/airport/<icao>')
def get_airport(icao):
    cursor = conn.cursor()

    sql = "SELECT ident, name, municipality FROM airport WHERE ident = %s"
    cursor.execute(sql, (icao,))
    answer = cursor.fetchone()

    cursor.close()
    conn.close()

    vastaus = {
        "ICAO": answer[0],
        "Name": answer[1],
        "Municipality": answer[2]
    }
    return jsonify(vastaus)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000)
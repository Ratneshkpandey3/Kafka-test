from flask import Flask, jsonify
import psycopg2
import logging

app = Flask(__name__)

app.config['DEBUG'] = True


try:
    conn = psycopg2.connect(
        dbname='transactions',
        user='user',
        password='password',
        host='postgres',
        port=5432
    )
    cursor = conn.cursor()
except psycopg2.Error as e:
    logging.error(f"Unable to connect to the database: {e}")
    cursor = None

@app.route('/transactions', methods=['GET'])
def get_transactions():
    if cursor is None:
        return jsonify({"error": "Database connection failed"}), 500

    try:
        cursor.execute("SELECT * FROM transactions")
        transactions = cursor.fetchall()
        return jsonify(transactions)
    except psycopg2.Error as e:
        logging.error(f"Database query failed: {e}")
        return jsonify({"error": "Database query failed"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0')

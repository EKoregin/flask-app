from flask import Flask
import psycopg2
import yaml

app = Flask(__name__)

with open("config.yml", "r") as f:
    config = yaml.safe_load(f)

@app.route('/')
def hello():
    conn = psycopg2.connect(
        host=config['database']['host'],
        database=config['database']['name'],
        user=config['database']['user'],
        password=config['database']['password']
    )
    conn.close()
    return f"Hello from {app.name} on {config['database']['host']}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

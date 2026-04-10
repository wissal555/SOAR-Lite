from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/stats')
def get_stats():
    try:
        with open("stats.json", "r") as f:
            return jsonify(json.load(f))
    except:
        return jsonify({"total_attempts": 0, "blocked_ips": []})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
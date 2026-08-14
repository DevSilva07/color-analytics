from flask import Flask, render_template, request, jsonify
from collections import Counter
from datetime import datetime

app = Flask(__name__)

# Educational demo only:
# This application analyzes already-recorded results.
# It intentionally does NOT claim to predict the next gambling outcome.

HISTORY = [
    "red", "blue", "red", "red", "blue", "blue", "red", "blue",
    "red", "blue", "blue", "red", "red", "blue", "red", "blue"
]

def stats(results):
    total = len(results)
    red = results.count("red")
    blue = results.count("blue")
    return {
        "total": total,
        "red": red,
        "blue": blue,
        "red_pct": round(red / total * 100, 1) if total else 0,
        "blue_pct": round(blue / total * 100, 1) if total else 0,
    }

@app.route("/")
def index():
    return render_template("index.html", history=HISTORY, stats=stats(HISTORY))

@app.post("/api/results")
def add_result():
    data = request.get_json(silent=True) or {}
    result = data.get("result")
    if result not in {"red", "blue"}:
        return jsonify({"error": "Use red ou blue."}), 400

    HISTORY.append(result)
    return jsonify({
        "message": "Resultado registrado para análise.",
        "history": HISTORY,
        "stats": stats(HISTORY),
    })

@app.post("/api/reset")
def reset():
    HISTORY.clear()
    return jsonify({"history": HISTORY, "stats": stats(HISTORY)})

@app.get("/api/stats")
def api_stats():
    return jsonify(stats(HISTORY))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

from flask import Flask, jsonify
import csv

app = Flask(__name__)

@app.route("/")
def home():
    return "quantium virtual internship Task 2 API Running"

@app.route("/sales")
def sales():
    data = []

    with open("output.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)

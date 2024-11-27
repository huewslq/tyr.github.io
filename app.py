from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)


with open("tours.json", encoding="utf-8") as f:
    tours = json.load(f)
    
# with open("tours.json") as f:
#     tours = json.load(f)

@app.route('/')
def index():
    return render_template("index.html", tours=tours)

@app.route('/tour/<int:tour_id>')
def tour(tour_id):
    tour = next((t for t in tours if t["id"] == tour_id), None)
    if tour:
        return render_template("tour.html", tour=tour)
    return "Tour not found", 404

@app.route('/book', methods=['POST'])
def book():
    name = request.form.get("name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    tour_id = request.form.get("tour_id")
    
    tour = next((t for t in tours if str(t["id"]) == tour_id), None)
    
    if tour:
        return render_template("confirmation.html", name=name, tour=tour)
    return "Booking failed", 400

if __name__ == '__main__':
    app.run(debug=True)

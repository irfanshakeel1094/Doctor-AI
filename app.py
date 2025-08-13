import os
import json
import requests
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from geopy.distance import geodesic

# Load environment variables (like your Google Maps API key)
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Initialize Flask app
app = Flask(__name__)

# A simple symptom database with advice, medicine, and dosage
SYMPTOMS_DB = {
    "fever": {
        "advice": "You may have a common viral fever. Stay hydrated and rest.",
        "medicine": "Paracetamol",
        "dosage": "500mg every 6 hours"
    },
    "headache": {
        "advice": "It could be a tension headache. Try to relax.",
        "medicine": "Ibuprofen",
        "dosage": "400mg every 8 hours after food"
    },
    "cold": {
        "advice": "It seems like a common cold. Warm fluids can help.",
        "medicine": "Cetirizine",
        "dosage": "10mg once daily at night"
    }
}

@app.route("/chat", methods=["POST"])
def chat():
    try:
        # Get user input
        data = request.json
        symptom = data.get("message", "").strip().lower()
        lat = data.get("lat")
        lon = data.get("lon")
        city_name = data.get("city", "").strip().lower()

        # Look up the symptom in our database
        response = SYMPTOMS_DB.get(symptom, {
            "advice": "I couldn't identify the symptom. Please consult a doctor.",
            "medicine": "undefined",
            "dosage": "undefined"
        })

        # If coordinates are provided, search for doctors near the user
        if lat and lon:
            try:
                doctor_search = requests.get(
                    "https://maps.googleapis.com/maps/api/place/nearbysearch/json",
                    params={
                        "location": f"{lat},{lon}",
                        "radius": 30000,
                        "type": "doctor",
                        "keyword": "best doctor",
                        "key": GOOGLE_API_KEY
                    },
                    timeout=5
                )
                nearby_results = doctor_search.json()

                # If doctors are found nearby
                if nearby_results.get("status") == "OK" and nearby_results.get("results"):
                    top_doctors = []
                    for place in nearby_results["results"][:5]:
                        top_doctors.append({
                            "name": place.get("name"),
                            "address": place.get("vicinity")
                        })
                    response["doctors"] = top_doctors
                else:
                    # If no doctors are found nearby, search major nearby cities
                    cities = ["chennai", "bangalore", "hyderabad", "delhi", "mumbai"]
                    alternatives = []
                    for city in cities:
                        search_city = requests.get(
                            "https://maps.googleapis.com/maps/api/place/textsearch/json",
                            params={
                                "query": f"best doctors in {city}",
                                "key": GOOGLE_API_KEY
                            },
                            timeout=5
                        )
                        city_results = search_city.json()
                        if city_results.get("status") == "OK" and city_results.get("results"):
                            for result in city_results["results"][:1]:
                                place_lat = result["geometry"]["location"]["lat"]
                                place_lon = result["geometry"]["location"]["lng"]
                                distance = geodesic((lat, lon), (place_lat, place_lon)).km
                                alternatives.append({
                                    "name": result["name"],
                                    "address": result.get("formatted_address"),
                                    "distance_km": round(distance, 2)
                                })
                    # Sort by closest city and show top 3
                    alternatives.sort(key=lambda x: x["distance_km"])
                    response["doctors"] = alternatives[:3] if alternatives else []

            except requests.RequestException as api_error:
                print("Google API failed:", api_error)
                response["doctors"] = []

        return jsonify(response)

    except Exception as general_error:
        print("Unexpected error:", general_error)
        return jsonify({"error": "An internal server error occurred."}), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)

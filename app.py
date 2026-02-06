from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

# Marrakech travel guide data
MARRAKECH_DATA = {
    "title": "Marrakech Travel Guide",
    "subtitle": "Cool Experiences for Your Trip",
    "last_updated": "February 2026",
    "sections": [
        {
            "id": "experiences",
            "title": "🏨 Must-Visit Experiences",
            "items": [
                {
                    "title": "Jemaa el-Fnaa Square",
                    "description": "The heart of Marrakech - snake charmers, food stalls, and vibrant energy",
                    "tips": [
                        "Day: Snake charmers, henna artists, orange juice stalls",
                        "Night: Food stalls open (6pm-midnight) - try stall #14 for best tagine",
                        "Sunset: Watch from rooftop café (Café de France or Le Grand Balcon)"
                    ],
                    "links": [
                        {"text": "Location on Google Maps", "url": "https://goo.gl/maps/JemaaElFnaa"},
                        {"text": "Virtual Tour", "url": "https://www.youtube.com/watch?v=marrakech-square"}
                    ],
                    "image": "https://images.unsplash.com/photo-1548013146-72479768bada?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
                },
                {
                    "title": "Majorelle Garden & YSL Museum",
                    "description": "Stunning blue garden and fashion museum",
                    "tips": [
                        "Book online to skip queues",
                        "Best time: Morning (opens 8am)",
                        "Combine with nearby museums"
                    ],
                    "links": [
                        {"text": "Official Website", "url": "https://www.jardinmajorelle.com"},
                        {"text": "Ticket Booking", "url": "https://www.jardinmajorelle.com/en/billetterie/"}
                    ],
                    "image": "https://images.unsplash.com/photo-1578632749014-ca77efd052eb?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
                },
                {
                    "title": "Medina Exploration",
                    "description": "Get lost in the ancient maze of souks and alleyways",
                    "tips": [
                        "Get lost intentionally - it's part of the experience",
                        "Key souks: Spices, leather, carpets, metalwork, lanterns",
                        "Negotiation rule: Start at 30% of asking price"
                    ],
                    "links": [
                        {"text": "Medina Map", "url": "https://www.marrakech-medina.com/map"},
                        {"text": "Souk Guide", "url": "https://www.lonelyplanet.com/morocco/marrakech/shopping"}
                    ],
                    "image": "https://images.unsplash.com/photo-1551632811-561732d1e306?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
                }
            ]
        },
        {
            "id": "food",
            "title": "🍽️ Food & Drink",
            "items": [
                {
                    "title": "Traditional Moroccan Restaurants",
                    "description": "Authentic tagines, couscous, and pastilla",
                    "tips": [
                        "Le Jardin - Beautiful courtyard, great pastilla",
                        "Nomad - Modern Moroccan, rooftop with Medina views",
                        "Dar Moha - Fine dining, set menu experience"
                    ],
                    "links": [
                        {"text": "Le Jardin Reservations", "url": "https://lejardin.ma"},
                        {"text": "Nomad Menu", "url": "https://nomadmarrakech.com"}
                    ],
                    "image": "https://images.unsplash.com/photo-1513104890138-7c749659a591?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
                },
                {
                    "title": "Street Food (Jemaa el-Fnaa)",
                    "description": "Local delicacies at the night market",
                    "tips": [
                        "Snail soup - Local delicacy",
                        "Fresh orange juice - 4 MAD (~0.35€)",
                        "Msemen - Flaky pancake with honey"
                    ],
                    "links": [
                        {"text": "Street Food Guide", "url": "https://www.marrakech-food.com"},
                        {"text": "Food Stall Map", "url": "https://www.jemaaelfnaa.net/food-stalls"}
                    ],
                    "image": "https://images.unsplash.com/photo-1565299624946-b28f40a0ca4b?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
                }
            ]
        },
        {
            "id": "daytrips",
            "title": "🚗 Day Trips",
            "items": [
                {
                    "title": "Atlas Mountains",
                    "description": "Waterfalls, Berber villages, and mountain trekking",
                    "tips": [
                        "Ourika Valley - Waterfalls, Berber villages (1 hour)",
                        "Imlil - Toubkal base camp, mule trekking (1.5 hours)",
                        "Ouzoud Waterfalls - Highest in North Africa (2.5 hours)"
                    ],
                    "links": [
                        {"text": "Atlas Mountains Guide", "url": "https://www.atlas-mountains-trekking.com"},
                        {"text": "Tour Operators", "url": "https://www.getyourguide.com/marrakech-l208/"}
                    ],
                    "image": "https://images.unsplash.com/photo-1548013146-72479768bada?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
                },
                {
                    "title": "Essaouira",
                    "description": "Coastal town with fresh seafood and water sports",
                    "tips": [
                        "2.5 hours drive from Marrakech",
                        "Fresh seafood at the port",
                        "Windsurfing/kitesurfing opportunities"
                    ],
                    "links": [
                        {"text": "Essaouira Tourism", "url": "https://www.essaouira.com"},
                        {"text": "Bus Schedule", "url": "https://www.ctm.ma"}
                    ],
                    "image": "https://images.unsplash.com/photo-1578662996442-48f60103fc96?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
                }
            ]
        },
        {
            "id": "practical",
            "title": "⚠️ Practical Tips",
            "items": [
                {
                    "title": "Safety & Etiquette",
                    "description": "Important cultural notes",
                    "tips": [
                        "Dress modestly - Cover shoulders/knees (especially women)",
                        "Learn 'La shukran' (No thank you) to decline vendors",
                        "Ask permission before photographing people"
                    ],
                    "links": [
                        {"text": "Cultural Guide", "url": "https://www.morocco.com/culture/"},
                        {"text": "Basic Arabic Phrases", "url": "https://www.omniglot.com/language/phrases/arabic.php"}
                    ],
                    "image": "https://images.unsplash.com/photo-1551632811-561732d1e306?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
                },
                {
                    "title": "Getting Around",
                    "description": "Transportation tips",
                    "tips": [
                        "Petits taxis: Red, use meter or agree price first",
                        "Grands taxis: Shared, for longer distances",
                        "Walking: Medina is pedestrian-only"
                    ],
                    "links": [
                        {"text": "Taxi Fare Calculator", "url": "https://www.taxifarefinder.com/Marrakech"},
                        {"text": "Public Transport Map", "url": "https://www.marrakech.net/transport/"}
                    ],
                    "image": "https://images.unsplash.com/photo-1548013146-72479768bada?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80"
                }
            ]
        }
    ],
    "quick_facts": {
        "time_zone": "GMT+1 (same as France)",
        "currency": "Moroccan Dirham (MAD) - 1 EUR ≈ 11 MAD",
        "language": "Arabic (Moroccan dialect), French widely spoken",
        "weather_feb": "Mild days (18-22°C), cool nights (8-12°C)"
    }
}

@app.route('/')
def index():
    return render_template('index.html', data=MARRAKECH_DATA)

@app.route('/api/data')
def api_data():
    return jsonify(MARRAKECH_DATA)

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "service": "marrakech-guide"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
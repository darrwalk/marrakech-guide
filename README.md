# Marrakech Travel Guide Web App

A beautiful web application showcasing cool experiences in Marrakech, Morocco.

## Features

- 🏨 Must-visit experiences with photos
- 🍽️ Food & drink recommendations
- 🚗 Day trip suggestions
- ⚠️ Practical travel tips
- 📱 Mobile-responsive design
- 🔗 Useful external links
- 🎨 Moroccan-inspired color scheme

## Tech Stack

- **Backend:** Flask (Python)
- **Frontend:** Bootstrap 5, HTML/CSS/JavaScript
- **Deployment:** Render.com
- **Images:** Unsplash API

## Local Development

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   python app.py
   ```
4. Open http://localhost:5000

## Deployment on Render

1. Push to GitHub
2. Connect repository to Render
3. Render will auto-detect `render.yaml` and deploy

## API Endpoints

- `GET /` - Main web interface
- `GET /api/data` - JSON data endpoint
- `GET /health` - Health check endpoint

## License

Created for personal travel use. Images from Unsplash.
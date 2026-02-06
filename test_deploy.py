from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Marrakech Travel Guide</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body { background: #f8f9fa; font-family: 'Segoe UI', sans-serif; }
            .hero { background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), url('https://images.unsplash.com/photo-1548013146-72479768bada?ixlib=rb-1.2.1&auto=format&fit=crop&w=1600&q=80'); background-size: cover; color: white; padding: 80px 0; }
            .card { border-radius: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.1); margin-bottom: 20px; border: none; }
            .card-header { background: #c1272d; color: white; border-radius: 15px 15px 0 0 !important; }
        </style>
    </head>
    <body>
        <div class="hero text-center">
            <div class="container">
                <h1 class="display-4">Marrakech Travel Guide</h1>
                <p class="lead">Essential tips for your trip to the Red City</p>
                <p class="text-muted">Updated February 2026</p>
            </div>
        </div>
        
        <div class="container py-5">
            <div class="row">
                <div class="col-md-4">
                    <div class="card">
                        <div class="card-header">
                            <h5>🏨 Must-Visit Experiences</h5>
                        </div>
                        <div class="card-body">
                            <ul>
                                <li><strong>Jemaa el-Fnaa Square</strong> - Heart of Marrakech</li>
                                <li><strong>Majorelle Garden</strong> - Stunning blue garden</li>
                                <li><strong>Medina Exploration</strong> - Get lost in ancient alleys</li>
                            </ul>
                        </div>
                    </div>
                </div>
                
                <div class="col-md-4">
                    <div class="card">
                        <div class="card-header">
                            <h5>🍽️ Food & Drink</h5>
                        </div>
                        <div class="card-body">
                            <ul>
                                <li><strong>Traditional Tagines</strong> - Slow-cooked Moroccan stews</li>
                                <li><strong>Street Food</strong> - Jemaa el-Fnaa night stalls</li>
                                <li><strong>Mint Tea</strong> - Served everywhere</li>
                            </ul>
                        </div>
                    </div>
                </div>
                
                <div class="col-md-4">
                    <div class="card">
                        <div class="card-header">
                            <h5>🚗 Day Trips</h5>
                        </div>
                        <div class="card-body">
                            <ul>
                                <li><strong>Atlas Mountains</strong> - Waterfalls & Berber villages</li>
                                <li><strong>Essaouira</strong> - Coastal town (2.5h drive)</li>
                                <li><strong>Ouzoud Waterfalls</strong> - Highest in North Africa</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="mt-4 text-center">
                <div class="card">
                    <div class="card-body">
                        <h5>⚠️ Practical Tips</h5>
                        <p><strong>Currency:</strong> Moroccan Dirham (MAD) - 1 EUR ≈ 11 MAD</p>
                        <p><strong>Language:</strong> Arabic (Moroccan dialect), French widely spoken</p>
                        <p><strong>Weather Feb:</strong> Mild days (18-22°C), cool nights (8-12°C)</p>
                        <p class="mt-3"><em>Full guide with photos and links coming soon!</em></p>
                    </div>
                </div>
            </div>
        </div>
        
        <footer class="text-center py-4 text-muted">
            <p>Marrakech Travel Guide • https://marrakech-travel-guide.onrender.com</p>
        </footer>
    </body>
    </html>
    """

@app.route('/health')
def health():
    return "OK"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
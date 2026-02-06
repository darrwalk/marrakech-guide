from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Marrakech Travel Guide 2026</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
        <style>
            :root {
                --moroccan-red: #c1272d;
                --moroccan-blue: #0066cc;
                --moroccan-gold: #ffd700;
                --moroccan-green: #008000;
            }
            
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
                min-height: 100vh;
            }
            
            .hero-section {
                background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), 
                            url('https://images.unsplash.com/photo-1548013146-72479768bada?ixlib=rb-1.2.1&auto=format&fit=crop&w=1600&q=80');
                background-size: cover;
                background-position: center;
                color: white;
                padding: 100px 0;
                margin-bottom: 40px;
                border-radius: 0 0 20px 20px;
            }
            
            .section-card {
                background: white;
                border-radius: 15px;
                padding: 25px;
                margin-bottom: 30px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.1);
                border-left: 5px solid var(--moroccan-blue);
                transition: transform 0.3s ease;
            }
            
            .section-card:hover {
                transform: translateY(-5px);
            }
            
            .experience-img {
                width: 100%;
                height: 200px;
                object-fit: cover;
                border-radius: 10px;
                margin-bottom: 15px;
            }
            
            .tip-badge {
                background: var(--moroccan-red);
                color: white;
                padding: 5px 12px;
                border-radius: 20px;
                font-size: 0.9em;
                margin-right: 8px;
                margin-bottom: 8px;
                display: inline-block;
            }
            
            .link-btn {
                background: var(--moroccan-blue);
                color: white;
                padding: 8px 16px;
                border-radius: 8px;
                text-decoration: none;
                display: inline-block;
                margin: 5px;
                transition: background 0.3s;
            }
            
            .link-btn:hover {
                background: #004d99;
                color: white;
                text-decoration: none;
            }
            
            .fact-box {
                background: white;
                border-radius: 10px;
                padding: 20px;
                margin: 10px 0;
                border-left: 4px solid var(--moroccan-green);
            }
        </style>
    </head>
    <body>
        <!-- Navigation -->
        <nav class="navbar navbar-expand-lg navbar-dark" style="background-color: var(--moroccan-red);">
            <div class="container">
                <a class="navbar-brand" href="#">
                    <i class="fas fa-map-marked-alt"></i> Marrakech Guide 2026
                </a>
            </div>
        </nav>
        
        <!-- Hero Section -->
        <div class="hero-section text-center">
            <div class="container">
                <h1 class="display-4 fw-bold">Marrakech Travel Guide</h1>
                <p class="lead">Your complete guide to the Red City • February 2026</p>
                <div class="mt-4">
                    <span class="badge bg-warning text-dark me-2"><i class="fas fa-sun"></i> 18-22°C Days</span>
                    <span class="badge bg-info me-2"><i class="fas fa-coins"></i> 1 EUR ≈ 11 MAD</span>
                    <span class="badge bg-success"><i class="fas fa-language"></i> Arabic/French</span>
                </div>
            </div>
        </div>
        
        <div class="container">
            <!-- Must-Visit Experiences -->
            <div class="section-card">
                <h2 class="mb-4" style="color: var(--moroccan-red);">
                    <i class="fas fa-landmark"></i> Must-Visit Experiences
                </h2>
                
                <div class="row">
                    <div class="col-md-4 mb-4">
                        <img src="https://images.unsplash.com/photo-1578662996442-48f60103fc96?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" 
                             class="experience-img" alt="Jemaa el-Fnaa Square">
                        <h4>Jemaa el-Fnaa Square</h4>
                        <p>The heart of Marrakech - snake charmers, food stalls, and vibrant energy.</p>
                        <div>
                            <span class="tip-badge">Day: Snake charmers</span>
                            <span class="tip-badge">Night: Food stalls</span>
                            <span class="tip-badge">Sunset: Rooftop cafés</span>
                        </div>
                        <div class="mt-3">
                            <a href="https://goo.gl/maps/example" class="link-btn" target="_blank">
                                <i class="fas fa-map-marker-alt"></i> Map
                            </a>
                        </div>
                    </div>
                    
                    <div class="col-md-4 mb-4">
                        <img src="https://images.unsplash.com/photo-1551632811-561732d1e306?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" 
                             class="experience-img" alt="Majorelle Garden">
                        <h4>Majorelle Garden & YSL Museum</h4>
                        <p>Stunning blue garden and fashion museum.</p>
                        <div>
                            <span class="tip-badge">Book online</span>
                            <span class="tip-badge">Morning visit</span>
                            <span class="tip-badge">Combine with museums</span>
                        </div>
                        <div class="mt-3">
                            <a href="https://www.jardinmajorelle.com" class="link-btn" target="_blank">
                                <i class="fas fa-external-link-alt"></i> Website
                            </a>
                        </div>
                    </div>
                    
                    <div class="col-md-4 mb-4">
                        <img src="https://images.unsplash.com/photo-1548013146-72479768bada?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80" 
                             class="experience-img" alt="Marrakech Medina">
                        <h4>Medina Exploration</h4>
                        <p>Get lost in the ancient walled city.</p>
                        <div>
                            <span class="tip-badge">Get lost intentionally</span>
                            <span class="tip-badge">Key souks: Spices, leather</span>
                            <span class="tip-badge">Negotiate: Start at 30%</span>
                        </div>
                        <div class="mt-3">
                            <a href="https://www.marrakech.net/medina-map" class="link-btn" target="_blank">
                                <i class="fas fa-map"></i> Medina Map
                            </a>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Food & Drink -->
            <div class="section-card">
                <h2 class="mb-4" style="color: var(--moroccan-green);">
                    <i class="fas fa-utensils"></i> Food & Drink
                </h2>
                
                <div class="row">
                    <div class="col-md-6">
                        <div class="fact-box">
                            <h5><i class="fas fa-concierge-bell"></i> Traditional Restaurants</h5>
                            <ul>
                                <li><strong>Le Jardin</strong> - Beautiful courtyard, great lunch</li>
                                <li><strong>Nomad</strong> - Modern Moroccan, rooftop with view</li>
                                <li><strong>Dar Moha</strong> - Fine dining, set menu experience</li>
                            </ul>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="fact-box">
                            <h5><i class="fas fa-stand"></i> Street Food (Jemaa el-Fnaa)</h5>
                            <ul>
                                <li><strong>Snail soup</strong> - Local delicacy</li>
                                <li><strong>Fresh orange juice</strong> - 4 MAD (~0.35€)</li>
                                <li><strong>Msemen</strong> - Flaky pancake with honey</li>
                                <li><strong>Stall #14</strong> - Best tagine according to locals</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Day Trips -->
            <div class="section-card">
                <h2 class="mb-4" style="color: var(--moroccan-blue);">
                    <i class="fas fa-car"></i> Day Trips
                </h2>
                
                <div class="row">
                    <div class="col-md-6">
                        <div class="fact-box">
                            <h5><i class="fas fa-mountain"></i> Atlas Mountains</h5>
                            <ul>
                                <li><strong>Ourika Valley</strong> - Waterfalls, Berber villages (1h drive)</li>
                                <li><strong>Imlil</strong> - Toubkal base camp, mule treks</li>
                                <li><strong>Ouzoud Waterfalls</strong> - Highest in North Africa (3h drive)</li>
                            </ul>
                            <a href="https://www.getyourguide.com/marrakech-l208/atlas-mountains-tours-tc101/" class="link-btn" target="_blank">
                                <i class="fas fa-hiking"></i> Tour Options
                            </a>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="fact-box">
                            <h5><i class="fas fa-umbrella-beach"></i> Essaouira</h5>
                            <ul>
                                <li><strong>2.5 hours drive</strong> from Marrakech</li>
                                <li><strong>Fresh seafood</strong> at the port</li>
                                <li><strong>Windsurfing/kitesurfing</strong> opportunities</li>
                                <li><strong>Historic medina</strong> and ramparts</li>
                            </ul>
                            <a href="https://www.ctm.ma/en/destinations/essaouira" class="link-btn" target="_blank">
                                <i class="fas fa-bus"></i> Bus Schedule
                            </a>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Practical Tips -->
            <div class="section-card">
                <h2 class="mb-4" style="color: var(--moroccan-gold);">
                    <i class="fas fa-info-circle"></i> Practical Tips
                </h2>
                
                <div class="row">
                    <div class="col-md-4">
                        <h5><i class="fas fa-user-check"></i> Safety & Etiquette</h5>
                        <ul>
                            <li>Dress modestly - Cover shoulders/knees</li>
                            <li>Learn "La shukran" (No thank you) to avoid vendors</li>
                            <li>Ask permission before photographing people</li>
                            <li>Carry small change for tips</li>
                        </ul>
                    </div>
                    
                    <div class="col-md-4">
                        <h5><i class="fas fa-taxi"></i> Getting Around</h5>
                        <ul>
                            <li><strong>Petits taxis:</strong> Red, use meter or agree price first</li>
                            <li><strong>Grands taxis:</strong> Shared, for longer distances</li>
                            <li><strong>Walking:</strong> Medina is pedestrian-only</li>
                            <li><strong>Caleches:</strong> Horse-drawn carriages for tourists</li>
                        </ul>
                    </div>
                    
                    <div class="col-md-4">
                        <h5><i class="fas fa-wallet"></i> Money & Costs</h5>
                        <ul>
                            <li><strong>Currency:</strong> Moroccan Dirham (MAD)</li>
                            <li><strong>Exchange:</strong> 1 EUR ≈ 11 MAD, 1 USD ≈ 10 MAD</li>
                            <li><strong>ATMs:</strong> Widely available, notify bank first</li>
                            <li><strong>Bargaining:</strong> Expected in souks, not in fixed-price shops</li>
                        </ul>
                    </div>
                </div>
            </div>
            
            <!-- Footer -->
            <footer class="text-center py-4 mt-4 text-muted" style="border-top: 1px solid #ddd;">
                <p>
                    <i class="fas fa-compass"></i> Marrakech Travel Guide 2026 • 
                    <a href="https://marrakech-2026-guide.onrender.com" class="text-decoration-none">
                        https://marrakech-2026-guide.onrender.com
                    </a>
                </p>
                <p class="small">Photos from Unsplash • Information updated February 2026</p>
                <p class="small"><i class="fas fa-hotel"></i> <em>Have a great trip! Your hotel details can be added here.</em></p>
            </footer>
        </div>
        
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """

@app.route('/health')
def health():
    return "OK"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
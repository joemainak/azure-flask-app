from flask import Flask, render_template_string
from azure.storage.blob import BlobServiceClient
import os

app = Flask(__name__)

# Azure Blob Storage connection (replace with your connection string later)
BLOB_CONNECTION_STRING = os.getenv("BLOB_CONNECTION_STRING", "your-connection-string")
blob_service_client = BlobServiceClient.from_connection_string(BLOB_CONNECTION_STRING)
container_client = blob_service_client.get_container_client("static")


@app.route('/')
def home():
    # Get image URL from Blob Storage
    blob_client = container_client.get_blob_client("logo.png")
    image_url = blob_client.url
    
    # Bootstrap template with modern design
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Azure Web App</title>
        <!-- Bootstrap CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <!-- Custom CSS -->
        <style>
            .hero-section {
                background: linear-gradient(135deg, #0078D4 0%, #004E8C 100%);
                color: white;
                padding: 4rem 0;
                border-radius: 0 0 2rem 2rem;
                margin-bottom: 2rem;
            }
            .logo-container {
                background-color: white;
                padding: 1.5rem;
                border-radius: 1rem;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
                margin-top: 2rem;
                transition: transform 0.3s;
            }
            .logo-container:hover {
                transform: translateY(-5px);
            }
            .feature-card {
                border: none;
                border-radius: 1rem;
                padding: 1.5rem;
                height: 100%;
                box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
                transition: all 0.3s;
            }
            .feature-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
            }
            .azure-icon {
                color: #0078D4;
                font-size: 2.5rem;
                margin-bottom: 1rem;
            }
            footer {
                background-color: #f8f9fa;
                padding: 2rem 0;
                margin-top: 3rem;
            }
        </style>
    </head>
    <body>
        <!-- Navigation -->
        <nav class="navbar navbar-expand-lg navbar-dark" style="background-color: #0078D4;">
            <div class="container">
                <a class="navbar-brand fw-bold" href="#">Azure App Service</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav ms-auto">
                        <li class="nav-item">
                            <a class="nav-link active" href="#">Home</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">About</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">Services</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">Contact</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>

        <!-- Hero Section -->
        <section class="hero-section">
            <div class="container text-center">
                <h1 class="display-4 fw-bold">Hello from Azure!</h1>
                <p class="lead">Welcome to your scalable web app hosted on Azure App Service.</p>
            </div>
        </section>

        <!-- Logo Section -->
        <section class="container mb-5">
            <div class="row justify-content-center">
                <div class="col-md-6 text-center">
                    <div class="logo-container">
                        <img src="{{ image_url }}" alt="Logo" class="img-fluid" style="max-height: 200px;">
                    </div>
                    <p class="mt-3 text-muted">Static assets served via Azure Blob Storage and CDN.</p>
                </div>
            </div>
        </section>

        <!-- Features Section -->
        <section class="container mb-5">
            <h2 class="text-center mb-4">Azure Platform Features</h2>
            <div class="row g-4">
                <div class="col-md-4">
                    <div class="feature-card">
                        <div class="azure-icon">
                            <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" class="bi bi-cloud" viewBox="0 0 16 16">
                                <path d="M4.406 3.342A5.53 5.53 0 0 1 8 2c2.69 0 4.923 2 5.166 4.579C14.758 6.804 16 8.137 16 9.773 16 11.569 14.502 13 12.687 13H3.781C1.708 13 0 11.366 0 9.318c0-1.763 1.266-3.223 2.942-3.593.143-.863.698-1.723 1.464-2.383z"/>
                            </svg>
                        </div>
                        <h3 class="h5">Scalable Infrastructure</h3>
                        <p>Scale your application up or down based on demand with Azure's elastic infrastructure.</p>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="feature-card">
                        <div class="azure-icon">
                            <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" class="bi bi-shield-check" viewBox="0 0 16 16">
                                <path d="M5.338 1.59a61.44 61.44 0 0 0-2.837.856.481.481 0 0 0-.328.39c-.554 4.157.726 7.19 2.253 9.188a10.725 10.725 0 0 0 2.287 2.233c.346.244.652.42.893.533.12.057.218.095.293.118a.55.55 0 0 0 .101.025.615.615 0 0 0 .1-.025c.076-.023.174-.061.294-.118.24-.113.547-.29.893-.533a10.726 10.726 0 0 0 2.287-2.233c1.527-1.997 2.807-5.031 2.253-9.188a.48.48 0 0 0-.328-.39c-.651-.213-1.75-.56-2.837-.855C9.552 1.29 8.531 1.067 8 1.067c-.53 0-1.552.223-2.662.524zM5.072.56C6.157.265 7.31 0 8 0s1.843.265 2.928.56c1.11.3 2.229.655 2.887.87a1.54 1.54 0 0 1 1.044 1.262c.596 4.477-.787 7.795-2.465 9.99a11.775 11.775 0 0 1-2.517 2.453 7.159 7.159 0 0 1-1.048.625c-.28.132-.581.24-.829.24s-.548-.108-.829-.24a7.158 7.158 0 0 1-1.048-.625 11.777 11.777 0 0 1-2.517-2.453C1.928 10.487.545 7.169 1.141 2.692A1.54 1.54 0 0 1 2.185 1.43 62.456 62.456 0 0 1 5.072.56z"/>
                                <path d="M10.854 5.146a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0l-1.5-1.5a.5.5 0 1 1 .708-.708L7.5 7.793l2.646-2.647a.5.5 0 0 1 .708 0z"/>
                            </svg>
                        </div>
                        <h3 class="h5">Enterprise Security</h3>
                        <p>Protect your applications with Azure's comprehensive security features and compliance certifications.</p>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="feature-card">
                        <div class="azure-icon">
                            <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" class="bi bi-graph-up" viewBox="0 0 16 16">
                                <path fill-rule="evenodd" d="M0 0h1v15h15v1H0V0Zm14.817 3.113a.5.5 0 0 1 .07.704l-4.5 5.5a.5.5 0 0 1-.74.037L7.06 6.767l-3.656 5.027a.5.5 0 0 1-.808-.588l4-5.5a.5.5 0 0 1 .758-.06l2.609 2.61 4.15-5.073a.5.5 0 0 1 .704-.07Z"/>
                            </svg>
                        </div>
                        <h3 class="h5">Advanced Analytics</h3>
                        <p>Gain insights from your application data with Azure's powerful analytics and AI capabilities.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Call to Action -->
        <section class="container">
            <div class="row">
                <div class="col-lg-8 mx-auto">
                    <div class="p-4 text-center bg-light rounded-4">
                        <h2 class="mb-3">Ready to get started?</h2>
                        <p class="mb-4">Let me help you with your cloud services needs. Professional solutions at competitive prices.</p>
                        <a href="https://www.fiverr.com/kimjoemaina" class="btn btn-primary btn-lg px-4 py-2">Hire Me on Fiverr</a>
                    </div>
                </div>
            </div>
        </section>

        <!-- Footer -->
        <footer>
            <div class="container text-center">
                <p class="mb-0">© 2025 Azure Web App. Powered by Azure App Service.</p>
            </div>
        </footer>

        <!-- Bootstrap JS Bundle with Popper -->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """
    
    return render_template_string(html, image_url=image_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
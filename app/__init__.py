from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import logging

def create_app():
    app = Flask(__name__)
    
    # Rate limiting
    limiter = Limiter(get_remote_address, app=app, default_limits=["5 per minute"], storage_uri="memory://")
    
    # Logging
    logging.basicConfig(
        filename='logs/app.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logging.info("Application Initialized")
    
    # Register routes
    from .routes import api
    app.register_blueprint(api)
    
    return app

import logging

from flask import Flask, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


def create_app():
    app = Flask(__name__)

    # Rate limiting
    limiter = Limiter(
        get_remote_address,
        app=app,
        default_limits=["15 per minute"],
        storage_uri="memory://",
    )

    # Custom rate-limit error handler
    @app.errorhandler(429)
    def ratelimit_error(e):
        logging.warning("Rate limit exceeded: 429 Too Many Requests")
        return (
            jsonify(
                {
                    "error": "Too Many Requests",
                    "message": "You have exceeded the rate limit. Try again later.",
                    "retry_after": e.description,  # Includes retry timing if provided
                }
            ),
            429,
        )

    # Logging
    logging.basicConfig(
        filename="logs/app.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    logging.info("Application Initialized")

    # Register routes
    from .routes import api

    app.register_blueprint(api)

    return app

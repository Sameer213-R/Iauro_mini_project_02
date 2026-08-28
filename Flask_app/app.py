from flask import Flask
from routes.routes import user_bp

app = Flask(__name__)

# Register user routes
app.register_blueprint(user_bp)


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )
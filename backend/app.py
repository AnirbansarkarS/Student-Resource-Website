from flask import Flask
from backend.models import db
from backend.routes import bba_routes, bca_routes, btech1_routes, user_routes

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database/student_resource.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "supersecretkey"  # For session management

# Initialize DB
db.init_app(app)

# Create tables if they don't exist
with app.app_context():
    db.create_all()

# Register Blueprints
app.register_blueprint(user_routes.bp)   # /user
app.register_blueprint(bba_routes.bp)    # /bba
app.register_blueprint(bca_routes.bp)    # /bca
app.register_blueprint(btech1_routes.bp) # /btech1

# Root route
@app.route('/')
def home():
    return "Welcome to Student Resource Website!"

if __name__ == '__main__':
    app.run(debug=True)

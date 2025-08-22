from flask import Flask
from flask_cors import CORS
from routes.syllabus import syllabus_bp
from routes.notes import notes_bp
from routes.questions import questions_bp

app = Flask(__name__)
CORS(app)  # Allow frontend requests (HTML/JS)

# Register Blueprints (modular routes)
# All Make routes Then I have to change the URL prefix....idont know for now
app.register_blueprint(syllabus_bp, url_prefix="/api/bba")
app.register_blueprint(notes_bp, url_prefix="/api/notes")
app.register_blueprint(questions_bp, url_prefix="/api/questions")

@app.route("/")
def home():
    return {"message": "Welcome to College Edu Portal API"}

if __name__ == "__main__":
    app.run(debug=True)

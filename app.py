# app.py
from flask import Flask, render_template
from routes.route import chatbot_bp

app = Flask(__name__)

# Register the blueprint for chatbot routes
app.register_blueprint(chatbot_bp, url_prefix='/chatbot')

# Route to render the HTML frontend
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

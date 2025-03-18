from flask import Flask
from database import init_db, db
from routes import main
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
init_db(app)
app.register_blueprint(main)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

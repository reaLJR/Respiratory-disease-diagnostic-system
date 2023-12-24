from flask import Flask, request, jsonify, session
from flask_cors import CORS
from flask_login import LoginManager, login_required, current_user


app = Flask(__name__)
app.secret_key = 'my_secret_key'

CORS(app)
login_manager = LoginManager(app)

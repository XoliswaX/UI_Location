from flask import Flask, request, jsonify, render_template
import firebase_admin
from firebase_admin import credentials, auth
import os

app = Flask(__name__)

# Initialize Firebase Admin SDK with credentials
os.environ["AIzaSyABWnW5iZqksWvL6RaKG8ShjmkR-wG1OpI"] = './serviceAccountKey.json'
# cred = credentials.Certificate("secrets/firebase-adminsdk.json")
# firebase_admin.initialize_app(cred)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    try:
        # Create a new user with email and password
        user = auth.create_user(
            email=email,
            password=password
        )
        return jsonify({"message": "User created successfully", "uid": user.uid}), 201
    except firebase_admin.auth.AuthError as e:
        return jsonify({"message": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)

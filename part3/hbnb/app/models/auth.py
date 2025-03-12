import datetime
import jwt
from functools import wraps
from flask import Blueprint, request, jsonify

auth_bp = Blueprint('auth', __name__)

SECRET_KEY = "your_secret_key"

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400
    token = generate_token(user_id=1) # Remplace 1 par l'ID utilisateur réel
    return jsonify({"{"token": token}), 200"})

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if not username or not password:
         return jsonify({"error": "Username and password are required"}), 400
        return jsonify({"message": "User registered successfully"}), 201

def generate_token(user_id):
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def verify_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload["user_id"]
    except jwt.ExpiredSignatureError:
         print("Token has expired")
        return None
    except jwt.InvalidTokenError:
        print(f"Invalid token: {e}")
        return None

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return jsonify({"error": "Missing token"}), 401
        user_id = verify_token(token)
        if not user_id:
            return jsonify({"error": "Invalid or expired token"}), 401
        return f(user_id, *args, **kwargs)
    return decorated_function

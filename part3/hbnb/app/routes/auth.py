# app/models/auth.py
import jwt
import datetime
from functools import wraps
from flask import request, jsonify
from app.routes.user import User

SECRET_KEY = "your_secret_key"

def generate_token(user_id):
    """Génère un token JWT valide pendant 2 heures"""
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def verify_token(token):
    """Vérifie et décode un token JWT"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload["user_id"]
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

def login_required(f):
    """Vérifie que l'utilisateur est connecté via un token JWT"""
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

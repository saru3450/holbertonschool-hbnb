#!/usr/bin/python3
from flask_bcrypt import Bcrypt
from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship
from flask import Blueprint, jsonify, request
from app.routes.base_model import BaseModel, Base
from app.routes.user import User
import re

bcrypt = Bcrypt()

class User(BaseModel, Base):
    __tablename__ = 'users'

    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    is_admin = Column(Boolean, default=False)

    places = relationship('Place', back_populates='owner', cascade="all, delete-orphan")
    reviews = relationship('Review', back_populates='user', cascade="all, delete-orphan")

    def __init__(self, first_name, last_name, email, password, is_admin=False):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.set_password(password)
        self.is_admin = is_admin

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def update(self, data):
        if "first_name" in data:
            self.first_name = data["first_name"]
        if "last_name" in data:
            self.last_name = data["last_name"]
        if "email" in data:
            if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", data["email"]):
                raise ValueError("Invalid email format")
            self.email = data["email"]

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "is_admin": self.is_admin
        }

user_bp = Blueprint('user', __name__)

@user_bp.route('/', methods=['GET'])
def get_users():
    users = []  
    return jsonify(users)

@user_bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(first_name=data["first_name"], last_name=data["last_name"], email=data["email"])
    return jsonify({"message": "User created", "user": user.to_dict()}), 201

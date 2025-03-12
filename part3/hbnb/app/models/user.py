#!/usr/bin/python3
"""This module defines the User model"""

import re
from flask_bcrypt import Bcrypt
from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship
from app.models.base_model import BaseModel, Base

bcrypt = Bcrypt()

class User(BaseModel, Base):
    """User model for database storage and authentication"""
    __tablename__ = 'users'

    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    is_admin = Column(Boolean, default=False)

    # Relations avec d'autres modèles
    places = relationship('Place', back_populates='owner', cascade="all, delete-orphan")
    reviews = relationship('Review', back_populates='user', cascade="all, delete-orphan")

    def __init__(self, first_name, last_name, email, password, is_admin=False):
        """Initialize a User instance"""
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.set_password(password)
        self.is_admin = is_admin

    def set_password(self, password):
        """Hash the password before storing it"""
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Check if the provided password matches the hashed password"""
        return bcrypt.check_password_hash(self.password_hash, password)

    def update(self, data):
        """Update user attributes dynamically"""
        if "first_name" in data:
            self.first_name = data["first_name"]
        if "last_name" in data:
            self.last_name = data["last_name"]
        if "email" in data:
            if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", data["email"]):
                raise ValueError("Invalid email format")
            self.email = data["email"]

    def to_dict(self):
        """Convert the User instance into a dictionary"""
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "is_admin": self.is_admin
        }

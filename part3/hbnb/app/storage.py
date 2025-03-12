#!/usr/bin/python3
"""This module manages the database connection and operations"""

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from app.routes.base_model import Base

class Storage:
    """Storage class to handle database operations"""
    
    def __init__(self):
        """Initialize the database connection"""
        self.engine = create_engine("sqlite:///hbnb.db", echo=False)  # Remplace SQLite par ton SGBD (ex: MySQL)
        self.session_factory = sessionmaker(bind=self.engine, expire_on_commit=False)
        self.session = scoped_session(self.session_factory)

    def new(self, obj):
        """Add a new object to the database session"""
        self.session.add(obj)

    def save(self):
        """Commit all changes to the database"""
        self.session.commit()

    def delete(self, obj):
        """Delete an object from the database"""
        if obj:
            self.session.delete(obj)
            self.save()

    def get(self, cls, id):
        """Retrieve one object by its ID"""
        return self.session.get(cls, id)

    def find_all(self, cls):
        """Retrieve all objects of a given class"""
        return self.session.query(cls).all()

    def find_one(self, cls, filters):
        """Retrieve a single object based on filters (ex: {"email": "test@example.com"})"""
        return self.session.query(cls).filter_by(**filters).first()

    def find_by(self, cls, filters):
        """Retrieve all objects that match certain filters"""
        return self.session.query(cls).filter_by(**filters).all()

    def close(self):
        """Close the current session"""
        self.session.remove()

    def reload(self):
        """Reload the database and create tables if they don't exist"""
        Base.metadata.create_all(self.engine)

# Create a single instance of Storage
storage = Storage()
storage.reload()

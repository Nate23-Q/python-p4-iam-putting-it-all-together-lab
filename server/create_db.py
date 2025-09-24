#!/usr/bin/env python3

from config import db
from models import User, Recipe
from app import app

def create_tables():
    with app.app_context():
        # Create all tables
        db.create_all()
        print("Database tables created successfully!")

if __name__ == '__main__':
    create_tables()

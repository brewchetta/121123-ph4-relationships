#!/usr/bin/env python3

from app import app
from models import db, Doctor, Appointment
from faker import Faker
from random import choice as rc

faker = Faker()

if __name__ == '__main__':
    with app.app_context():
        print("Seeding database...")

        print("Removing old data")

        Appointment.query.delete()
        Doctor.query.delete()

        print("Creating doctors")

        specialties = ["neurosurgery", "pediatrics", "cardiovascular", "general practice", "orthopaedics", "magic"]

        for _ in range(5):
            d = Doctor(name=faker.name(), specialty=rc(specialties))
            db.session.add(d)
            print(f"Created doctor {d.name}")

        db.session.commit()

        print("Seeding complete!")

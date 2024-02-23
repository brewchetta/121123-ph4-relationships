#!/usr/bin/env python3

from app import app
from models import db, Doctor, Appointment, Patient
from faker import Faker
from random import choice as random_choice

faker = Faker()

if __name__ == '__main__':
    with app.app_context():
        print("Seeding database...")

        print("Removing old data")

        Appointment.query.delete()
        Doctor.query.delete()
        Patient.query.delete()

        print("Creating doctors")

        specialties = ["neurosurgery", "pediatrics", "cardiovascular", "general practice", "orthopaedics", "magic"]

        for _ in range(5):
            d = Doctor(name=faker.name(), specialty=random_choice(specialties))
            db.session.add(d)
            print(f"Created doctor {d.name}")

        db.session.commit()



        print("Creating patients")

        for _ in range(5):
            p = Patient(name=faker.name())
            db.session.add(p)
            print(f"Created patient {p.name}")

        db.session.commit()



        print("Creating appointments")

        days = ["Monday", "Tuesday", "Wednesday", "Thursday"]

        for _ in range(50):
            appt = Appointment(
                date=random_choice(days),
                doctor=random_choice( Doctor.query.all() ),
                patient=random_choice( Patient.query.all() )
            )

            db.session.add(appt)

        db.session.commit()

        print("Seeding complete!")

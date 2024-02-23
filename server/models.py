from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Doctor(db.Model):
    __tablename__ = "doctors_table"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    specialty = db.Column(db.String)

    time_created = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
    time_updated = db.Column(db.DateTime(timezone=True), onupdate=db.func.now())

    appointments = db.relationship("Appointment", back_populates="doctor", cascade="all, delete-orphan")
    patients = association_proxy("appointments", "patient")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "specialty": self.specialty,
            "appointments": [ { 
                "date": appt.date, "time_created": appt.time_created, "time_updated": appt.time_updated, "patient_name": appt.patient.name
            } for appt in self.appointments]
        }


class Appointment(db.Model):
    __tablename__ = "appointments_table"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable=False)

    doctor_id = db.Column(db.Integer, db.ForeignKey("doctors_table.id"))
    patient_id = db.Column(db.Integer, db.ForeignKey("patients_table.id"))

    time_created = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
    time_updated = db.Column(db.DateTime(timezone=True), onupdate=db.func.now())

    doctor = db.relationship("Doctor", back_populates="appointments")
    patient = db.relationship("Patient", back_populates="appointments")

class Patient(db.Model):
    __tablename__ = "patients_table"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    appointments = db.relationship("Appointment", back_populates="patient")
    doctors = association_proxy("appointments", "doctor")
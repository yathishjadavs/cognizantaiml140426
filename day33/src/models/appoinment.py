""" create appointment """
from datetime import date,time
from models.docter import Doctor
from models.pationt import Patient
class Appointment:
    def __init__(self, id: int, patient: Patient, doctor: Doctor, appointment_date: datetime):
        self.id = id
        self.patient = patient
        self.doctor = doctor
        self.appointment_date = appointment_date

    def __str__(self):
        return f"Appointment ID: {self.id}, Patient: {self.patient.name}, Doctor: {self.doctor.name}, Date: {self.appointment_date}"
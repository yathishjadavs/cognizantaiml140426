"""create docter curd operations"""
import sys
import os
from models.docter import Doctor
from exceptions.doctor_not_found_exceptions import DoctorNotFoundException

""" add project root to python path
"""

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)
from conf.logger_cof import setup_logger
logger = setup_logger()

class DoctorStore:
    def __init__(self):
        self.doctors = []

    def add_doctor(self, doctor: Doctor):
        logger.info(f"Adding doctor: {doctor}")
        self.doctors.append(doctor)

    def get_doctor_by_id(self, doctor_id: int) -> Doctor:
        logger.info(f"Fetching doctor with ID: {doctor_id}")
        for doctor in self.doctors:
            if doctor.id == doctor_id:
                return doctor
        raise DoctorNotFoundException(f"Doctor with ID {doctor_id} not found")

    def get_all_doctors(self):
        logger.info("Fetching all doctors")
        return self.doctors

    def update_doctor(self, doctor_id: int, name: str = None, specialization: str = None):
        logger.info(f"Updating doctor with ID: {doctor_id}")
        doctor = self.get_doctor_by_id(doctor_id)
        if doctor:
            if name:
                doctor.name = name
            if specialization:
                doctor.specialization = specialization
            logger.info(f"Doctor updated successfully: {doctor}")
            return True
        return False

    def delete_doctor(self, doctor_id: int):
        doctor = self.get_doctor_by_id(doctor_id)
        if doctor:
            self.doctors.remove(doctor)
            logger.info(f"Doctor deleted successfully: {doctor}")
            return True
        return False
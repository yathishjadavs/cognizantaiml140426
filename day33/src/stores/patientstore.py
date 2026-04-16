#create crud operations for patient
"""create crud operations for patient
"""
import sys
import os
from models.patient import Patient
from exceptions.patient_not_found_exceptions import PatientNotFoundException
""" add project root to python path
"""
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)
from conf.logger_cof import setup_logger   
logger = setup_logger()


class PatientStore:
    def __init__(self):
        self.patients = []

    def add_patient(self, patient: Patient):
        logger.info(f"Adding patient: {patient}")
        self.patients.append(patient)

    def get_patient_by_id(self, patient_id: int) -> Patient:
        logger.info(f"Fetching patient with ID: {patient_id}")
        for patient in self.patients:
            if patient.id == patient_id:
                return patient
        return None

    def get_all_patients(self):
        logger.info("Fetching all patients")
        return self.patients

    def update_patient(self, patient_id: int, name: str = None, age: int = None):
        logger.info(f"Updating patient with ID: {patient_id}")
        patient = self.get_patient_by_id(patient_id)
        if patient:
            if name:
                patient.name = name
            if age:
                patient.age = age
            logger.info(f"Patient updated successfully: {patient}")
            return True
        raise PatientNotFoundException(f"Patient with ID {patient_id} not found")

    def delete_patient(self, patient_id: int):
        patient = self.get_patient_by_id(patient_id)
        if patient:
            self.patients.remove(patient)
            logger.info(f"Patient deleted successfully: {patient}")
            return True
        return False
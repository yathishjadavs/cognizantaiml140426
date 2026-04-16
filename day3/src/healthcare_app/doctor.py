class Doctor:
    def __init__(self, doctor_id: int, name: str, specialization: str):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.patients_seen = []

    def get_details(self) -> str:
        """Return doctor details."""
        return (
            f"Doctor ID: {self.doctor_id}, "
            f"Name: {self.name}, "
            f"Specialization: {self.specialization}"
        )

    def consult(self, patient, notes: str) -> str:
        """
        Record a consultation:
        - Save patient ID
        - Add consultation notes to patient's history
        """
        notes = notes.strip()
        if not notes:
            return "❌ Consultation notes cannot be empty."

        if patient.patient_id not in self.patients_seen:
            self.patients_seen.append(patient.patient_id)

        # patient must have add_history()
        patient.add_history(
            f"Consulted by {self.name} ({self.specialization}): {notes}"
        )

        return f"✅ Consultation saved for patient {patient.name}."
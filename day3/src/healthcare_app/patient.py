class Patient:
    def __init__(self, patient_id: int, name: str, age: int, phone: str = ""):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.phone = phone
        self.medical_history = []

    def add_history(self, note: str) -> None:
        note = note.strip()
        if note:
            self.medical_history.append(note)

    def get_details(self) -> str:
        phone_text = f", Phone: {self.phone}" if self.phone else ""
        return f"Patient ID: {self.patient_id}, Name: {self.name}, Age: {self.age}{phone_text}"

    def show_history(self) -> str:
        if not self.medical_history:
            return "No medical history found."
        result = ["Medical History:"]
        for i, item in enumerate(self.medical_history, start=1):
            result.append(f"{i}. {item}")
        return "\n".join(result)

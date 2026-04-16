class Doctor:
    def __init__(self, id, name, specialization):
        self.id = id
        self.name = name
        self.specialization = specialization


    def __str__(self):
        return f"Doctor {self.name} (ID: {self.id}), Specialization: {self.specialization}"
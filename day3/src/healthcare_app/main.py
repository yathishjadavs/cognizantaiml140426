from healthcare_app import Patient, Doctor


def seed_data():
    """Create sample doctor and patient objects (temporary in-memory data)."""
    patient = Patient(patient_id=1, name="Ravi", age=30, phone="9876543210")
    doctor = Doctor(doctor_id=101, name="Dr. Meera", specialization="Cardiology")
    return patient, doctor


def show_menu():
    print("\n===== Healthcare Project (Day 3) =====")
    print("1. Show Patient Details")
    print("2. Show Doctor Details")
    print("3. Add Patient Medical History")
    print("4. Doctor Consultation (adds note to patient history)")
    print("5. View Patient History")
    print("0. Exit")


def main():
    patient, doctor = seed_data()

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print(patient.get_details())

        elif choice == "2":
            print(doctor.get_details())

        elif choice == "3":
            note = input("Enter history note (example: fever, headache): ").strip()
            if not note:
                print("❌ Empty input not allowed. Please type something.")
                continue
            patient.add_history(note)
            print(f"✅ History added: {note}")

        elif choice == "4":
            notes = input("Enter consultation notes: ").strip()
            result = doctor.consult(patient, notes)
            print(result)

        elif choice == "5":
            print(patient.show_history())

        elif choice == "0":
            print("Bye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
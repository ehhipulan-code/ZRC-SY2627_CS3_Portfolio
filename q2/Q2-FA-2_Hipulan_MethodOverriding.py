# Parent class
class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount


    # Getter methods
    def get_name(self):
        return self.__name

    def get_bill_amount(self):
        return self.__bill_amount

    # Setter methods
    def set_name(self, name):
        self.__name = name

    def set_bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount

    # Return full bill
    def calculate_bill(self):
        return self.__bill_amount

# Child class : Senior Patient
class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.8  # 20% discount for senior patients

# Child class : PhilHealth Patient
class PhilHealthPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.85  # 15% discount for PhilHealth patients

# Create patient objects
patient1 = Patient("Juan Dela Cruz", 15000)
patient2 = SeniorPatient("Maria Santos", 15000)
patient3 = PhilHealthPatient("Pedro Reyes", 15000)

# Display hospital billing system
print("Hospital Billing System")
print("-----------------------")

print("Patient Name:", patient1.get_name()) 
print("Original Bill:", f"₱{patient1.calculate_bill():,.2f}")    
print("Final Bill:", f"₱{patient1.calculate_bill():,.2f}") 

print(" ")

print("Patient Name:", patient2.get_name())
print("Original Bill:", f"₱{patient2.get_bill_amount():,.2f}")
print("Final Bill:", f"₱{patient2.calculate_bill():,.2f}")

print(" ")

print("Patient Name:", patient3.get_name())
print("Original Bill:", f"₱{patient3.get_bill_amount():,.2f}")
print("Final Bill:", f"₱{patient3.calculate_bill():,.2f}")

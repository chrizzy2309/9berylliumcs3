class Patient: #create a class called Patient
    def __init__(self, name, bill_amount, type = "Regular"): #constructor method to initialize the attributes of the class
        self.name = name
        self.bill_amount = float(bill_amount)
        self.type = type 

    def get_name(self): #create a method to get the name of the patient
        return self.name
    def set_name(self, name): # create a method to set the name of the patient
        self.name = name

    def get_bill_amount(self): #create a method to get the bill amount of the patient
        return self.bill_amount
    
    def set_bill_amount(self, bill_amount):#create a method to set the bill amount of the patient
        self.bill_amount = float(bill_amount)

    def calculate_bill(self): #create a method to calculate the final bill amount of the patient
        return self.bill_amount  # No discount for regular patients
    
    def display_patient_type(self):#create a method to display the type of the patient
        return (f"{self.type} Patient")

class Senior(Patient): #create a subclass called Senior that inherits from the Patient class
    def __init__(self, name, bill_amount, type="Senior"):#create a constructor method to initialize the attributes of the Senior class
        super().__init__(name, bill_amount, type) #Call the constructor of the parent class to initialize the attributes of the Senior class
        self.type = "Senior"

    def calculate_bill(self): #create a method to calculate the final bill amount of the Senior patient
        return self.bill_amount * 0.8  # 20% discount for seniors


class PhilHealth(Patient): #create a subclass called PhilHealth that inherits from the Patient class
    def __init__(self, name, bill_amount, type="PhilHealth"): #create a constructor method to initialize the attributes of the PhilHealth class
        super().__init__(name, bill_amount, type) #Call the constructor of the parent class to initialize the attributes of the PhilHealth class
        self.type = "PhilHealth"

    def calculate_bill(self): #create a method to calculate the final bill amount of the PhilHealth patient
        return self.bill_amount * 0.85  # 15% discount for PhilHealth members


# Preserve the existing Patient.Senior and Patient.PhilHealth interface.
Patient.Senior = Senior
Patient.PhilHealth = PhilHealth

#Patient Class
patient1 = Patient("Juan Dela Cruz", 15000)
patient2 = Patient.Senior("Maria Santos", 15000, "Senior")
patient3 = Patient.PhilHealth("Pedro Reyes", 15000, "PhilHealth")

#Patient Information Billing

print("Hospital Billing System")
print("------------------------")
print(f"Patient Name: {patient1.get_name()}")
print(f"Patient Type: {patient1.display_patient_type()}")
print(f"Original Bill Amount: ₱{patient1.get_bill_amount()}")
print(f"Final Bill Amount: ₱{patient1.calculate_bill()}")

print()

print("------------------------")
print(f"Patient Name: {patient2.get_name()}")
print(f"Patient Type: {patient2.display_patient_type()}")
print(f"Original Bill Amount: ₱{patient2.get_bill_amount()}")    
print(f"Final Bill Amount: ₱{patient2.calculate_bill()}")

print()

print("------------------------")
print(f"Patient Name: {patient3.get_name()}")
print(f"Patient Type: {patient3.display_patient_type()}")
print(f"Original Bill Amount: ₱{patient3.get_bill_amount()}")
print(f"Final Bill Amount: ₱{patient3.calculate_bill()}")


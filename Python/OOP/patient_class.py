##Q) Create a class for Patient Appointmentwith the methods of 

##    (i) Booking an appointment

##    (ii) Calling the patient

###############################################################################

class Patient:
    '''Class for Patient Appointment'''
    def __init__(self,pname,pmobile,dname,booking_date,booking_time):
        self.pname = pname
        self.pmobile= pmobile  # say 7836457328
        self.dname = dname
        self.bdate = booking_date  # say 10/07/2022
        self.btime = booking_time  # say 3:00
        
    # instance method to display booked appointment details
    def bookAppointment(self):
        print("\n**** Appointment Booked ****\n")
        print("Appointment with Dr. ",self.dname)  
        print("Appointment Date: ",self.bdate)
        print("Appointment Time: ",self.btime)
        
    # instance method to display patient's details
    def callPatient(self):
        print("\n**** Patient Details ****\n ")
        print("Patient Name: ",self.pname)
        print("Patient Mobile No.: ",self.pmobile)


# taking user input to be passed
pname = input("Enter patient name: ")
pmobile = input("Enter your mobile no.: ")
dname = input("Enter name of doctor for appointment: ")
bdate = input("Enter required date for appointment")
btime = input("Enter required time for appointment: ")

# creating objects of class Patient
p1 = Patient(pname,pmobile,dname,bdate,btime)
# calling instance methods of class Patient throught object p1
p1.bookAppointment()
p1.callPatient()

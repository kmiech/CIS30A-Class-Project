
class Person:
    def __init__(self, fname, lname, p_number, e_mail):
        self.f_name = fname
        self.l_name= lname
        self.phone_number = p_number
        self.emal = e_mail
    

class Appointment (Person):
    def __init__(self, fname, lname, p_number, e_mail, month, day, year, time):
        super().__init__(fname, lname, p_number, e_mail)
        self.month = month #month of appointment
        self.day = day #day of appointment
        self.year = year #year of appointment
        self.time = time #time of appointment
    
class Donation (Person):
    pass

"""class Greeting (Appointment):
    def __init__(self, fname, lname, p_number, e_mail, month, day, year, time):
        super().__init__(fname, lname, p_number, e_mail, day, year, time)
""" 

hour_ops = {1:'8:00 A.M.', 2:'9:00 A.M.', 3:'10:00 A.M.', 4:'11:00 A.M.', 5:'12:00 P.M.', 6:'1:00 P.M.', 7:'2:00 P.M.', 8:'3:00 P.M.', 9:'4:00 P.M.', 10:'5:00 P.M.', 11:'6:00 P.M.', 12:'7:00 P.M.', 13:'8:00 P.M.'}
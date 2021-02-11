#functions for Project
#fout = open('Appointment_Text.txt', 'w') #opening textfile to be written

    

def write_info(self):
    fout = open('Appointment_Text.txt', 'w') #opening textfile to be written
    fout.write("{} {}, you have scheduled an appointment for {} {}, {} at {}".format(self.f_name, self.l_name, self.month, self.day, self.year, self.time))
    
    fout.close()
    
def write_donation(self, donate_list):
    fout = open('Donation_Text.txt', 'w') #opening textfile to be written
    fout.write("Thank you {} {}".format(self.f_name ,self.l_name))
    fout.write("\nYour donation of:\n")
    fout.write('\n'.join(map(str,donate_list)))
    
    fout.close()
    


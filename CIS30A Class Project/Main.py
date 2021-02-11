#CIS30A Class Project 2 : MVC Garden Appointment
import FunctionProject
import ModuleProject #imports the classes module created
import datetime #imports the date and time module

fname = ''
lname = ''
p_number = ''
e_mail = ''

w_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
#hour of operations in a dictionary
hour_ops = {1:' 8:00 A.M.', 2:' 9:00 A.M.', 3:' 10:00 A.M.', 4:' 11:00 A.M.', 5:' 12:00 P.M.', 6:' 1:00 P.M.', 7:' 2:00 P.M.', 8:' 3:00 P.M.', 9:' 4:00 P.M.', 10:'5:00 P.M.', 11:'6:00 P.M.', 12:'7:00 P.M.', 13:'8:00 P.M.'}
donate_item = {1:('Seeds'), 2:('Soil'), 3:('Fertilizer')}
donate_list = []
current_date = datetime.date.today() #setting the date and time to current
one_year = current_date.year + 1 #takes current year + 1
print(one_year)
        
print("Welcome to Moreno Valley College's Community Garden Program.")
print("\nOur hours of operation are")
print("Monday - Friday : 8:00 AM - 8:00 PM")
print("Saturday : 8:00 AM - 5:00 PM")
print("Sunday : Closed\n")

print("We are booking appointments up to", current_date.strftime('%B'), current_date.strftime('%d'), one_year)

print("Would you like to make an appointment, or a donation?")
print("Enter '1' to make an appointment")
print("Enter '2' to make a donation")
print("Enter '3' for more information about donations")

choice_1 = 0
while choice_1 < 1 or choice_1 > 3:
    choice_1 = int(input("What would you like to do today: "))
    
    fname = input("Enter first name: ")
    lname = input("Enter last name: ")
    p_number = input("Enter phone number: ")
    e_mail = input("Enter email: ")
    
    if choice_1 == 1:
        
        #info = ModuleProject.Person(fname, lname, p_number, e_mail)
        
        print("\nWe are booking appointments up to ", one_year)
        print("Enter the date and time you would like to make the appointment.")
        
        month = int(input("Enter the month's number (Jaunary = 1 and December = 12): "))
        day = int(input("Enter the day of the month: "))
        #if/else statement to get the year
        if (month <= current_date.month and day < current_date.day) :
            year = current_date.year + 1
        else:
            year = current_date.year
            
        app_date = datetime.date(year, month, day) #initializing app_date with the appointment date
       # print(app_date.day)
        #print(app_date.year)
       #if-elif-else statement for hour of operations for the day
        if app_date.strftime('%A') in w_days: #print hours for Mon - Friday
            for k, v in hour_ops.items():
                print('{}) {}'.format(k, v))
            

        elif app_date.strftime('%A') == 'Saturday': #printing hours for Saturday
            for k, v in hour_ops.items():
                if k <= 10:
                    print('{}) {}'.format(k,v))
                    
        
        else:
            print('\nSorry, we are closed that day') #Closed on Sundays
        
        month_string = app_date.strftime('%B')
        choice_time = int(input('\nPlease choose from the hours listed: '))
        time = hour_ops.get(choice_time)
        
        info1 = ModuleProject.Appointment(fname, lname, p_number, e_mail, month_string, day, year, time)
        print (info1.f_name)
        FunctionProject.write_info(info1)   
        
    elif choice_1 == 2: #choosing to donate
        keep_going = 'Y'
        print("\nThank you for choosing to make a donation.")
        print("We are currently accepting")
        for k,v in donate_item.items():
            print('{}) {}'.format(k,v))
        while keep_going == 'Y':
            donate_choice = int(input('Which would you like to donate: '))
            
            if donate_choice in donate_item.keys():
                donate_list.append((donate_item[donate_choice]))
                
            else:
                print('Invalid Choice')
                
            keep_going = input('Would you like to donate something else(Y for yes, N for no): ').upper()
           
        info2 = ModuleProject.Donation(fname, lname, p_number, e_mail)
        FunctionProject.write_donation(info2,donate_list) #calls the write_donation function
    else:
        print("Needs Update.")
        
        
        
       
     

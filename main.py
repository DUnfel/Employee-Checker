''' 
This defines a code which if the user puts a correct code (4 digits) it writes in the end of "Employees.txt" if the people were present on that day.
This very beneficial in the real world; f.ex. In order to monitor and know if the employees were there on working days. 
An employee have to input a special code given each employee by company in the morning when they start, and optional in the end and that data is sent to manager or whoever is in position of checking it
and then they know when each employee at what time is working or not working, because each employee is given a special code which the code is connected to their name.
the big CON of this, is the security because if other employees know other peoples code they can just input it for them and keep on moving. This is a big con but can be fixed with weekly code change
which can also be unprofessional and annoying for some employees, therefore this is my first project and im looking forward to update it in order to prevent from such.
'''

from datetime import datetime, date

time = datetime.now()
code = input("Input your code:")

Dan = ("1237")
John = ("1235")
Jeniffer = ("1236")
Mike = ("1238")

if code == Dan:
   employe_file = open("Employees.txt", "a")
   employe_file.write("\nDan was here on ")
   employe_file.write(time.strftime("%b-%d-%Y %H:%M:%S"))
   employe_file.close

if code == John:
   employe_file = open("Employees.txt", "a")
   employe_file.write("\nJohn was here on ")
   employe_file.write(time.strftime("%b-%d-%Y %H:%M:%S"))
   employe_file.close

if code == Jeniffer:
   employe_file = open("Employees.txt", "a")
   employe_file.write("\nJeniffer was here on ")
   employe_file.write(time.strftime("%b-%d-%Y %H:%M:%S"))
   employe_file.close

if code == Mike:
   employe_file = open("Employees.txt", "a")
   employe_file.write("\nMike was here on ")
   employe_file.write(time.strftime("%b-%d-%Y %H:%M:%S"))
   employe_file.close



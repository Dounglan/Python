# lab17.py
#Dounglan Cheung
#  This file contains the definition of a new class (Employee),
#     plus a few instances of that class.
################################################################
class Employee: # if not specified, an employee is considered non-exempt
    def __init__ (self,name,pay,exempt=False):
        self.name = name
        self.payrate = pay
        self.exempt = exempt

    def display (self):
        if self.exempt:
            status = "Exempt"
        else:
            status = "Non-exempt"
            
        print ("{0}: {1}, paid ${2:.2f} per hour".format(self.name, status, self.payrate))
#part IC/part III
    def payraise(self, amt):
        self.payrate = self.payrate + amt
        if self.payrate >= 12.00:
            return self.payrate
        else:
            print("Under minimum wage")
#part ID        
    def paycheck(self, hours):
        pay = self.payrate
        if hours <= 0:
            pay = float(0)
            return pay
        elif hours <= 40 or self.exempt == True:
            pay = hours * self.payrate
            return pay
        elif self.exempt == False:
            pay = 40 * self.payrate + (hours - 40)* self.payrate * 1.5
            return pay
##  here ends the definition of the Employee class
################################################################    
# some sample instances of Employee, for testing purposes
#   Because of indentation, we can see that these are *not*
#      part of the class definition.  They are globally scoped,
#      which means you can access them in the shell.
#part II
def tester(emp, hrlist):
    name = emp.name
    pay = emp.payrate
    exempt = emp.exempt
    if emp.exempt:
        status = "Exempt"
    else:
        status = "Non-exempt"
    print ("{0}: {1}, paid ${2:.2f} per hour".format(emp.name, status, emp.payrate))
#    for i in hrlist:
#        if i > 40:
#            pay = 40 * emp.payrate + (i - 40)* emp.payrate * 1.5
#            print("Pay for ", i, "hours: ","$",pay)
#        else:
#            print("Pay for ", i, "hours: ","$",i*pay)
    for i in hrlist:
        paycheck = emp.paycheck(i)
        print("Pay for ", i, "hours: ","$",paycheck)
zeke = Employee ("Ezekial Frekial",20.00,False)
yancey = Employee ("Yanciford Royale",20.00,True)
joule = Employee ("Joule Zooms", 17.00)

#part IV
class SalariedEmployee:
    def __init__(self, name, annualSalary):
        self.name = name
        self.annualSalary = annualSalary
        
    def display(self):
        print ("{0} paid ${1:.2f} annually".format(self.name, self.annualSalary))
    def paycheck(self, weeks):
        self.annualSalary = (self.annualSalary/52)*weeks
        return self.annualSalary
    
al = SalariedEmployee ("AlexTeacher", 44500)
nik = SalariedEmployee ("NikiEngineer",60000)
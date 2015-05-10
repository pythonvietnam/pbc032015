#!/usr/bin/python

class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount

emp1.age = 7  # Add an 'age' attribute.
#emp1.age = 8  # Modify 'age' attribute.
#del emp1.age  # Delete 'age' attribute.

print "co ton tai thuoc tinh tuoi trong emp1:", hasattr(emp1, 'age')    # Returns true if 'age' attribute exists
print "Gia tri tuoi:", getattr(emp1, 'age')    # Returns value of 'age' attribute
setattr(emp1, 'age', 10) # Set attribute 'age' at 8
print "Tuoi moi: ", emp1.age
delattr(emp1, 'age')    # Delete attribute 'age'
#print "Tuoi moi: ", emp1.age

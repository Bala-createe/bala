import mymodule

myfirstcar=mymodule.car("Ford","Black","Ecosport")
mysecondcar=mymodule.car("Hyundai","White","Verna")
print(type(myfirstcar))

mysecondcar.Color="Yellow"

#myfirstcar.printcardetails()
#mysecondcar.printcardetails()

print(len(myfirstcar))

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class childclass(Person):
    def __init__(self, fname, lname):
       super().__init__(fname, lname)
       self.Age=""

a=childclass()
b=Person()
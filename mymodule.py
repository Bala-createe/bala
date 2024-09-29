a=1
b=2
c=23

def printhello():
    print("Hi, there!")

class car:
    def __init__(self,brand,color,model):
        print("Object is created")
        self.Brand=brand
        self.Color=color
        self.Model=model
    def printcardetails(self):
        print(f"Car Brand: {self.Brand}\nCar Color: {self.Color}\nCar Model : {self.Model}")
    def __len__(self) -> int:
        return 10
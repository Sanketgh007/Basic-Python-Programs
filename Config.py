class Computer:
    
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
    def config(self):
        print("config is",self.cpu,self.ram)
comp1=Computer('i7','16gb') 
# alternate waty of invoking function using object in python Computer.config(comp1)      
comp2=Computer('i5','8gb')
comp1.config()
comp2.config()

#__init__is like constructor in java whenever we create an object of class it will call the constructor the same way __init__ is called
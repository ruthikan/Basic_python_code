class Employee:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def display(self):
        print(f"the employee id is {self.id} and name is {self.name}")

#creating and object
emp=Employee(1,"coder")
emp.display()

#2 deleting emp id
del emp.id

#deleting the entire object
del emp

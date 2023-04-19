#Create a class
#Set two parameters 'value' and 'salary'
#here is an example, I assume that the value is 30 million dollars and my salary is 7 million dollars.
print("if I have 7 million dollars, and the value is 30 million dollars")
class calculator(object):
    def __init__(self,value, salary):
        self.value = value
        self.salary = salary
    def add(self):
        if self.value <= 5*self.salary:
            print('Yes')
        else:
            print('No')

man = calculator(30,7)
man.add()

#here you can input whatever you like
class calculator(object):
    def __init__(self,value, salary):
        self.value = value
        self.salary = salary
    def add(self):
        if self.value <= 5*self.salary:
            print('Yes')
        else:
            print('No')
print("\ninput a new house value and salary")
input_value = input('value: ')
input_salary = input('salary: ')
man = calculator(input_value,input_salary)
man.add()

from abc import ABC, abstractclassmethod, abstractmethod

'''
class abstract_class_name(abc):
    [list of attributes]
    [list of methods]
    @abstractmethod
    def method_name(self):
        pass
'''

class Polygon(ABC):

    @abstractmethod
    def draw(self): 
        pass

    def get_area(self): 
        pass

    def get_circle(self):
        pass


class Rectangle(Polygon): 
    def __init__(self,width,height) :
        self.height = height
        self.width = width

    def draw(self):
            print('draw rectangle')
        
    def get_width(self):
            return self.width

    def get_height(self):
            return self.height

    def get_area(self): 
            return self.height * self.width 
            
    def get_perimeter(self):
            return 2*(self.height + self.width)

class Square(Polygon):
    def __init__(self,width):
        self.width = width

    def draw(self):
        print('draw square')

    def get_width(self): 
        return self.width

    def get_area(self):
        return self.width * 2

    def get_perimeter(self):
        return 2 * (self.width + self.width)

obj_rectangle = Rectangle(3,4)

obj_square = Square(3)
        

print('Perimeter =', Square.get_perimeter(), 'Area =', Square.get_area())

print('width =', Rectangle.get_width(), 'height=', Rectangle.get_height())

'''
write a python program to calculate the payroll of employees in a company 
there are 2 type: fulltime, parttime
need to have class: 
- Employee (abstract) with 2 attributes : first_name, last_name, 1 method to return salary for employees

- Fulltime employee: inherited from employee class 1 attribute: salary

- Parttime employee: inherited from employee class 2 attributes: worked_hours and rate

- Payroll: 1 attribute: employee list, 2 methods: 
+ to append employee to list
+ to show fullname and salary for a  given employee

The program will receive information of employee from the keyboard 
'''

print('input type of employee, fulltime is 1, parttime is 2')
input('input here')

class Employee(ABC):
    
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def fullname(self): 
        return self.first_name + self.last_name

    @abstractmethod
    def show_salary(self):
       pass
        
class Fulltime_employee(Employee):
    def __init__(self, salary, first_name, last_name):
        self.salary = salary
        super().__init__(first_name, last_name)

    def get_salary(self): 
        return self.salary
class Parttime_employee(Employee):
    def __init__(self, worked_hours, rate, first_name, last_name):
        self.worked_hours = worked_hours
        self.rate = rate
        super().__init__(first_name, last_name)
    
    def get_salary(self): 
        return self.worked_hours * self.rate

class Payroll:
    def __init__(self):
        self.employees = []

    def append_emp(self, employee):
       self.employees.append(employee)
    
    def show_info(self):
        for employee in self.employees:
            print(employee.fullname())
            print(employee.get_salary())
    
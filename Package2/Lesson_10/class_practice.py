#1 create new class with some properties and methods




class student : 
    def __init__(self, name, height, weight, years_old):
        self.name = name
        self.height = height
        self.weight = weight
        self.years_old = years_old

    def get_name(self):
        return self.name

    def get_height(self): 
        return self.height
    
    def get_weight(self): 
        return self.weight
    
    def get_years_old(self):
        return self.years_old

std1 = student('binh', 162, 62, 21) #create object for student

print('info cua hoc sinh', std1.get_name())



#2 create a child class for student
class pupil(student):
    def __init__(self, strength):
        self.strength = strength
        #student.__init__(self, name, height, weight, years_old)
        super().__init__(name, height, weight, years_old)
pupil1 = pupil('nhat', 169, 82, 21)
print('info cua sinh vien', pupil1.get_name())




#------------------------------------
#1 define a class named student and intialize attributes: name, age, email and sex. create a object of that class
class student: 
    def __init__(self, name, age, email, sex): 
        self.name = name
        self.age = age
        self.email = email
        self.sex = sex
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_email(self):
        return self.email

    def get_sex(self):
        return self.sex


#2 define a class named people with no attribute and method. create a new object of that class

class people:
    def __init__(self) :
        pass
person = people()


#3 define a class named staff with attributes: role, department, salary and a method named show_details() to display all attributes
#department is protected, salary is private
class staff:
    def __init__(self, role, department, salary): 
        self.role = role
        self._department = department
        self.__salary = salary
    def show_salary(self):
        return self.__salary
    def show_detail(self):
        print(self.role, self._department, self.show_salary())

#define a class named student that inheritated from staff class. this class has 2 more attributes: name, age

class studentt(staff):
    def __init__(self,name, age, role, department, salary):
        self.name =  name
        self.age = age
        super().__init__(role, department, salary)
#create new object of student  then show all attributes of that object
std = studentt('binh', 21, 'newbie', 'fresher', '500')
print(std.name, std.age, std.role, std._department, std.show_salary(),)


#4 
#4.1 define class named geometry with attributes: length, width, and 2 methods: get_area() and get_perimeter()
class geometry:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):  
       
       return self.length * self.width
    
    def get_perimeter(self):

        return self.length + self.width
        
#4.2 define a class named square which inheritated from geometry class. this  class has 2 attributes are length and width, Override two methods from its parrent
class square(geometry):
    def __init__(self, length, width):
        super().__init__(length, width)
    
    def get_length(self):
        return self.length

    def get_width(self):
        return self.width

#4.3 define class circle which inherited from geometry class. this class has 1 attribute is radius, override 2 methods of its
class circle(geometry):
    def __init__(self, radius):
        self.radius = radius
    def get_area_circle(self):
        return self.radius * 3.14
    def get_perimeter_circle(self):
        return self.radius * 2 * 3.14
        
#4.4 create a new object of class square and circle, print area and perimeter of those
obj_square = square(1,2) #object for square class

obj_circle = circle(3) #object for circle class



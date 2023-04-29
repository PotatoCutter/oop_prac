class Car():
    def __init__(self):
        self.color =  'black'
        self.model = 'volvo'
        self.speed = 0
        
        
        
    def accelerate(self, speed):
        self.speed += speed
        
    def brake(self):
        self.speed -= 10
        
    def get_speed(self):
        return self.speed
    def get_color(self):
        return self.color
    def get_model(self):
        return self.model

    def __str__(self):
        return f'This car is {self.color} {self.model} and speed is {self.speed}'   
        
        
class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def speak(self):
        pass
    
class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        
    def speak(self):
        return '멍멍'

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        
    def speak(self):
        return '야옹'


class Shape():
    def get_area(self):
        pass        
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def get_area(self):
        return 3.14 * self.radius ** 2
class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def get_area(self):
        return self.width * self.height
                

mycar = Car()

print(mycar.get_color())
print(mycar.get_model())
print(mycar)
mycar.accelerate(100)
print(mycar.get_speed())
mycar.brake()
print(mycar.get_speed())
print(mycar)


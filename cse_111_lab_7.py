# -*- coding: utf-8 -*-
"""CSE 111 Lab 7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PfZCC2K3FshPQ6m0DCc4NFI8wA8q48-G
"""

#1
class Student:
    def __init__(self, name='Just a student', dept='nothing'):
        self.__name = name
        self.__department = dept
    def set_department(self, dept):
        self.__department = dept
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name
    def __str__(self):
        return 'Name: '+self.__name+' Department: '+self.__department
class BBA_Student(Student):
  def __init__(self,name='Default',dept='BBA'):
    super().__init__(name,dept)

print(BBA_Student())
print(BBA_Student('Humpty Dumpty'))
print(BBA_Student('Little Bo Peep'))

#2
class Vehicle:
    def __init__(self):
        self.x = 0
        self.y = 0
    def moveUp(self):
        self.y+=1
    def moveDown(self):
        self.y-=1
    def moveRight(self):
        self.x+=1
    def moveLeft(self):
        self.x-=1
    def __str__(self):
        return '('+str(self.x)+' , '+str(self.y)+')'
class Vehicle2010(Vehicle):
  def __init__(self):
    super().__init__()
  def moveLowerLeft(self):
    super().moveDown()
    super().moveLeft()
  def moveUpperRight(self):
    super().moveUp()
    super().moveRight()
  def moveUpperLeft(self):
    super().moveUp()
    super().moveleft()
  def moveLowerRight(self):
    super().moveDown()
    super().moveRight()
  def equals(self,other):

    if self.y==other.y and self.x==other.x :
      return True
    else:
      return False


print('Part 1')
print('------')
car = Vehicle()
print(car)
car.moveUp()
print(car)
car.moveLeft()
print(car)
car.moveDown()
print(car)
car.moveRight()
print(car)
print('------')
print('Part 2')
print('------')
car1 = Vehicle2010()
print(car1)
car1.moveLowerLeft()
print(car1)
car2 = Vehicle2010()
car2.moveLeft()
print(car1.equals(car2))
car2.moveDown()
print(car1.equals(car2))

#3
class Tournament:
    def __init__(self,name='Default'):
        self.__name = name
    def set_name(self,name):
        self.__name = name
    def get_name(self):
        return self.__name

class Cricket_Tournament(Tournament):
  def __init__(self,name='Default',a=0,b='No type'):
    super().set_name(name)
    self.a=a
    self.b=b

  def detail(self):
    return f"Cricket Tournament Name: {super().get_name()}\nNumber of Team: {self.a}\nType: {self.b}"
class Tennis_Tournament(Tournament):
  def __init__(self,name="Default",a=0):
    super().__init__(name)
    self.a=a
  def detail(self):
    return f"Tennis Tournament Name: {super().get_name()}\nNumber of Players: {self.a}"


ct1 = Cricket_Tournament()
print(ct1.detail())
print("-----------------------")
ct2 = Cricket_Tournament("IPL",10,"t20")
print(ct2.detail())
print("-----------------------")
tt = Tennis_Tournament("Roland Garros",128)
print(tt.detail())

#4
class Product:
    def __init__(self,id, title, price):
        self.__id = id
        self.__title = title
        self.__price = price
    def get_id_title_price(self):
        return "ID: "+str(self.__id)+" Title:"+self.__title+        "Price: "+str(self.__price)
class Book(Product):
  def __init__(self,id,title,price,a,b):
    super().__init__(id,title,price)
    self.a=a
    self.b=b
  def printDetail(self):
    s=f"OUTPUT\n{super().get_id_title_price()}\nISBN: {self.a} Publisher: {self.b}"
    return s
class CD(Product):
  def __init__(self,id,title,price,a,b,c):
   super().__init__(id,title,price)
   self.a=a
   self.b=b
   self.c=c
  def printDetail(self):
    s=f"{super().get_id_title_price()}\nBand: {self.a} Duration: {self.b} minutes\nGenrre: {self.c}"
    return s

book = Book(1,"The Alchemist",500,"97806","HarperCollins")
print(book.printDetail())
print("-----------------------")
cd = CD(2,"Shotto",300,"Warfaze",50,"Hard Rock")
print(cd.printDetail())

#5
class Animal:
    def __init__(self,sound):
        self.__sound = sound

    def makeSound(self):
        return self.__sound



class Printer:
    def printSound(self, a):
        print(a.makeSound())


class Dog(Animal):
  def __init__ (self,sound):
   super().__init__(sound)

class Cat(Animal):
  def __init__ (self,sound):
    super().__init__(sound)

d1 = Dog('bark')
c1 = Cat('meow')
a1 = Animal('Animal does not make sound')
pr = Printer()
pr.printSound(a1)
pr.printSound(c1)
pr.printSound(d1)

#6
class Shape:

  def __init__(self, name='Default', height=0, base=0):
    self.area = 0
    self.name = name
    self.height = height
    self.base = base

  def get_height_base(self):
    return "Height: "+str(self.height)+",Base: "+str(self.base)

class triangle(Shape):
  def __init__(self,name='Default', height=0, base=0):
    super().__init__(name,height,base)
  def calcArea(self):
    self.area=self.height*self.base*0.5
  def printDetail (self):

    s=f"Shape name: {self.name}\n{super().get_height_base()}\n{self.area}"
    return s
class trapezoid(Shape):
  def __init__ (self,name, height, base,a):
    super().__init__(name,height,base)
    self.a=a
  def calcArea(self):
    self.area=(self.a+self.base)*self.height*0.5
  def printDetail (self):

    s=f"Shape name: {self.name}\n{super().get_height_base()}, Side_A:{self.a}\n{self.area}"
    return s

tri_default = triangle()
tri_default.calcArea()
print(tri_default.printDetail())
print('--------------------------')
tri = triangle('Triangle', 10, 5)
tri.calcArea()
print(tri.printDetail())
print('---------------------------')
trap = trapezoid('Trapezoid', 10, 6, 4)
trap.calcArea()
print(trap.printDetail())

#7
class SportsPerson:

  def __init__(self, team_name, name, role):
    self.__team = team_name
    self.__name = name
    self.role = role
    self.earning_per_match = 0

  def get_name_team(self):
    return 'Name: '+self.__name+', Team Name: ' +self.__team

class Player(SportsPerson):
  def __init__ (self,team_name, name, role,a,b):
    super().__init__(team_name, name, role)
    self.a=a
    self.b=b
    self.ratio=0
    self.earning_per_match+=(self.a*1000)+(self.b*10)
  def calculate_ratio(self):
    self.ratio+=self.a/self.b

  def print_details(self):
    s=f"OUTPUT\n{super().get_name_team()}\nTeam Role: {self.role}\nGoal Ratio: {self.ratio}\nMatch Earning: {self.earning_per_match}k "
    print(s)
class Manager(SportsPerson):
  def __init__ (self,team_name, name, role,a):
    super().__init__(team_name, name, role)
    self.a=a
    self.earning_per_match+=self.a*1000

  def print_details(self):
    s=f"{super().get_name_team()}\nTeam Role: {self.role}\nTotal Win: {self.a}\nMatch Earning: {self.earning_per_match}k "
    print(s)

player_one = Player('Juventus', 'Ronaldo', 'Striker', 25, 32)
player_one.calculate_ratio()
player_one.print_details()
print('------------------------------------------')
manager_one = Manager('Real Madrid', 'Zidane', 'Manager', 25)
manager_one.print_details()


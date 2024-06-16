# -*- coding: utf-8 -*-
"""CSE111 Lab 5

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zbUt-cOgqCOUUfs4JtuUILfV6btivAIo
"""

#task 1
class Marks:
  def __init__ (self,n):
    self.mark=n
  def __add__ (self,p):
    sum=self.mark+p.mark
    obj=Marks(sum)
    return obj
Q1 = Marks(int(input("Quiz 1 (out of 10): ")))
Q2 = Marks(int(input("Quiz 2 (out of 10): ")))
Lab = Marks(int(input("Lab (out of 30): ")))
Mid = Marks(int(input("Mid (out of 20): ")))
Final = Marks(int(input("Final (out of 30): ")))
total = Q1 + Q2 + Lab + Mid + Final
print("Total marks: {}".format(total.mark))

#task 4
class Color:
  def __init__ (self,clr):
    self.clr=clr
  def __add__ (self,other):
    if (self.clr=='red' and other.clr=='yellow') or (self.clr=='yellow' and other.clr=='red'):
      obj=Color('Orange')
    elif (self.clr=='red' and other.clr=='blue') or (self.clr=='blue' and other.clr=='red'):
      obj=Color('Violet')
    elif (self.clr=='yellow' and other.clr=='blue') or (self.clr=='blue' and other.clr=='yellow'):
      obj=Color('Green')
    return obj
C1 = Color(input("First Color: ").lower())
C2 = Color(input("Second Color: ").lower())
C3 = C1 + C2
print("Color formed:", C3.clr)

#task 8
class Coordinates:
  def __init__(self,n1,n2):
    self.n1=n1
    self.n2=n2
  def __sub__(self,other):
    new_n1=self.n1-other.n1
    new_n2=self.n2-other.n2
    return Coordinates(new_n1,new_n2)
  def __mul__(self,other):
    new_n1=self.n1*other.n1
    new_n2=self.n2*other.n2
    return Coordinates(new_n1,new_n2)
  def detail(self):
    return self.n1,self.n2
  def __eq__(self, other):
    if (self.n1 == other.n1 and self.n2 == other.n2):
      s='The calculated coordinates are the same'
    else:
      s='The calculated coordinates are NOT the same.'
    return s




p1 = Coordinates(int(input()),int(input()))
p2 = Coordinates(int(input()),int(input()))

p4 = p1 - p2
print(p4.detail())

p5 = p1 * p2
print(p5.detail())

point_check = (p4 == p5)
print(point_check)

#2
class Teacher:
  def __init__ (self,name,dept):
    self.__name=name
    self.__dept=dept
    self.__courses=[]
  def addCourse(self,course):
    self.__courses.append(course.course_name)
  def printDetail(self):
    print('====================================')
    print(f"Name:{self.__name}")
    print(f"Depertment:{self.__dept}")
    print('List of courses')
    print('====================================')
    for i in self.__courses:

      print(i)

class Course:
  def __init__ (self,coursename):
    self.course_name=coursename
t1 = Teacher("Saad Abdullah", "CSE")
t2 = Teacher("Mumit Khan", "CSE")
t3 = Teacher("Sadia Kazi", "CSE")
c1 = Course("CSE 110 Programming Language I")
c2 = Course("CSE 111 Programming Language-II")
c3 = Course("CSE 220 Data Structures")
c4 = Course("CSE 221 Algorithms")
c5 = Course("CCSE 230 Discrete Mathematics")
c6 = Course("CSE 310 Object Oriented Programming")
c7 = Course("CSE 320 Data Communications")
c8 = Course("CSE 340 Computer Architecture")
t1.addCourse(c1)
t1.addCourse(c2)
t2.addCourse(c3)
t2.addCourse(c4)
t2.addCourse(c5)
t3.addCourse(c6)
t3.addCourse(c7)
t3.addCourse(c8)
t1.printDetail()
t2.printDetail()
t3.printDetail()

#6
class Triangle:
  def __init__(self,n1,n2):
    self.__n1=n1
    self.__n2=n2
  def getBase(self):
    return self.__n1
  def getHeight(self):
    return self.__n2
  def setBase(self,update):
    self.__n1=update
  def setHeight(self,update):
    self.__n2=update
  def area(self):
    return (0.5*(self.__n1*self.__n2))
  def __sub__(self,other):
    self.__n1=self.__n1-other.__n1
    self.__n2=self.__n2-other.__n2
    return Triangle(self.__n1,self.__n2)
t1 = Triangle(10, 5)
print("First Triangle Base:" , t1.getBase())
print("First Triangle Height:" , t1.getHeight())
print("First Triangle area:" ,t1.area())

t2 = Triangle(5, 3)
print("Second Triangle Base:" , t2.getBase())
print("Second Triangle Height:" , t2.getHeight())
print("Second Triangle area:" ,t2.area())

t3 = t1 - t2
print("Third Triangle Base:" , t3.getBase())
print("Third Triangle Height:" , t3.getHeight())
print("Third Triangle area:" ,t3.area())

#3
class Team:
  def __init__(self,team=None):
    self.__team=team
    self.__players=[]
  def setName(self,update):
    self.__team=update
  def addPlayer(self,obj):
    self.__players.append(obj.player)
  def printDetail(self):
    print('=====================')
    print(f"Team: {self.__team}\nList of Players:\n{self.__players}")
    print('=====================')
class Player:
  def __init__(self,player):
    self.player=player
b = Team()
b.setName('Bangladesh')
mashrafi = Player("Mashrafi")
b.addPlayer(mashrafi)
tamim = Player("Tamim")
b.addPlayer(tamim)
b.printDetail()
a = Team("Australia")
ponting = Player("Ponting")
a.addPlayer(ponting)
lee = Player("Lee")
a.addPlayer(lee)
a.printDetail()

#5
class Circle:
  def __init__(self, radius):
    self.__radius = radius

  def getRadius(self):
    return self.__radius

  def setRadius(self, num):
    self.__radius = num

  def area(self):
    import math
    return(math.pi * self.__radius ** 2)

  def __add__(self, other):
    obj = Circle(self.__radius + other.__radius)
    return obj
c1 = Circle(4)
print("First circle radius:" , c1.getRadius())
print("First circle area:" , c1.area())

c2 = Circle(5)
print("Second circle radius:" , c2.getRadius())
print("Second circle area:" , c2.area())

c3 = c1 + c2
print("Third circle radius:" , c3.getRadius())
print("Third circle area:" , c3.area())

#7
class Dolls:
  def __init__(self,name,price):
    self.doll=name
    self.price=price
    self.count=0
  def detail(self):
    if self.count==0:
      s=f"Doll: {self.doll}\nTotal price: {self.price} taka"
    else:
      s=f"Dolls: {self.doll}\nTotal price: {self.price} taka"
    return s
  def __add__ (self,other):
    thanks= Dolls(self.doll+''+other.doll,self.price+other.price)
    thanks.count+=1
    return thanks
  def __gt__ (self,other):
    return self.price > other.price
obj_1 = Dolls("Tweety", 2500)
print(obj_1.detail())
if obj_1 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")

print("=========================")
obj_2 = Dolls("Daffy Duck", 1800)
print(obj_2.detail())
if obj_2 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")

print("=========================")
obj_3 = Dolls("Bugs Bunny", 3000)
print(obj_3.detail())
if obj_3 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")

print("=========================")
obj_4 = Dolls("Porky Pig", 1500)
print(obj_4.detail())
if obj_4 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")

print("=========================")
obj_5 = obj_2 + obj_3
print(obj_5.detail())
if obj_5 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")
print("gibson")

#this is indentation
if 5>2:
  print("five is greater than two")
  
  #variables
  """
  x and y is containers for storing data
  """
  x=5
  y="copy"
  print(type(x))
  print(type(y))
  
  #multi values in variables
  x,y,z = "color",2,2.0,
  print(type(x))
  print(type(y))
  print(type(z))
  
  #one value to many variables
  x=y=z="Millions"
  print(x)
  print(y)
  print(z)
  
  #unpack the collection
  fruits = ["apple","strawberry","cherry"]
  x,y,z = fruits
  print(x)
  print(y)
  print(z)
  
  #to combine text and variables
  x = "bright"
  print("Apple is " + x)
  
  x = " am "
  y = "tired"
  z = x + y
  print(z)
  
  #Function
  def gibs():
    x = 20
    y = 60
    z = x + y
    print(z)
  gibs()
  
  #function with parameter & arguments
  def gibs(y):
    x = 20
    z = x + y
    print(z)
  gibs(20)
  
  #write once and use it many times
  
  def star():
    name = "millions"
    print("Give me",name)
  star()
  star()
  
  #global variables
  x = "grad"
  
  def points():
    global x
    x = "water"
points()

print(" Eternity is " + x)
  
 
def mid():
  x = "diamond"
  
mid()

print("may be " + x)

#Datatypes in python
x = 100000
def man():
  y = 1000000
  z = x+y
  print(z)
  
#Type conversion

x = 1
y = 2.1

a = float(x)
b = int(y)

print(a)
print(b)

#Random module

import random

print(random.randrange(1,7))

#Casting in python

x = 2
y = 2.1

print(float(x))
print(int(y))

#String in python

x = "Gibson"

#checking string 

txt = "Million dollar"
print("Million" in txt)

x = "Gibson will be millionaire soon!"
print("millionaire" in x)

#using in "if" statement

room = "Millionaire gibson is in"
if "gibson" in room:
    print("yes,'gibson is present")
    
    
    #Slicing String
    
    g = "hello,world"
    print(g[1:6])
    
    #nagative indexing
    
    z = "gibson coin"
    print(z[-5:-1])
    
    #modify string
    
    #1.uppper case
    
    g = "gibson"
    print(g.upper())
    
    #2.lower case
    
    z = "GIBSON IS MILLIONAIRE BITCH!"
    print(z.lower())
    
    #strip string
    
    ex = " fuck  you  !"
    print(ex.strip())
    
    #Replace string 
    
    a = "Kello,world!"
    print(a.replace("k", "h"))
    
    #Split to make list
    
    x = "gibs"
    print(x.split(","))
    
    #format string
    
    a = 19
    v = "am gibs and ,am {}"
    print(v.format(a))
    
    #Python escape character
    #use \" to add illegal word in string
    
    txt = "we are the so-called \"viking\" from north"
    print(txt)
    
    
          
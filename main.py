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
  
  
  
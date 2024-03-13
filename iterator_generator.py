'''
A for loop using the generator object calls the __iter__ method (implicitly) to initialize the iteration.
The iter() function takes an iterable object (like a list, string, tuple, etc.) as input and returns an iterator object.
__iter__ (for initialization) and __next__ (to retrieve the next element).
you do not need to use iter inside a for loop, python does that for u

A very basic example of both  can be: 

numbers = iter([1, 2, 3, 4, 5])  # Create an iterator object explicitly
print(next(numbers))  # Output: 1
print(next(numbers))  # Output: 2

def fibonacci_generator(n):
  a, b = 0, 1
  for _ in range(n):
      yield a
      a, b = b, a + b
for _ in f(9):
  print(_ , end =",") #output: 0,1,1,2,3,5,8,13,21,
'''
class Numbers :
  def __init__(self,start,end):
      self.uno= start
      self.dos=end
  def __iter__(self): 
      return self #cuz the class is init as an iterator only, i.e. it takes the first and last value as an argument
  def __next__(self):
      if self.uno<=self.dos:
          self.uno+=1
          return self.uno-1 #not to use any extra variable but make sure ur logic is correct
      else :
          raise StopIteration

def num_generator(start,end): #not a part of the class
  while start<=end:
      start = start +1
      yield start -1



iterator = Numbers(1,4) 

generator = num_generator(5,8)

# Looping using both methods
print("Using Iterator:")
for num in iterator:
  print(num,end=",")

print("\nUsing Generator:")
for num in generator:
  print(num,end=",")
    
    
'''
* __str__(self) : takes only self as a parameter and returns a string related to the class or the instance of a class
* @classmethod takes the first input as cls, and functions defined with @classmethods are tied to the class itself, rather than its instances,they can excess modify class-level attributes and call other methods too
BUT,,, You SHOULD NOT use classmethod to set getters for an inherited class
@property : getter
@'parameter'.setter : setter
'''


class Book:
  def __init__(self,name,writer,mrp=0.0):
      self._title=name.strip().title()
      self._author=writer.strip().title()
      self._price=mrp

  @property
  def title(self):
      return self._title 

  @title.setter
  def title(self,newTitle):
      self._title = newTitle

  @property
  def  author(self):
      return self._author

  @author.setter
  def author(self,newAuthor):
      self._author = newAuthor

  @classmethod
  def get(cls):
      naam,lekhak,daam= input("book ka naam : "),input("writer ka naam : "),input("book ka daam kya hai :")
      return cls(naam,lekhak, float (daam))

  def __add__(self,other):
     return self._price + other._price

  def __str__(self):
      return f"The book named '{self.title}' is written by {self.author}"

def main ():       
  print("for book 1 : ")
  a= Book.get()
  print("for book 2 : ")
  b= Book.get()
  hb = Handbook("Randomname", "Rohan", 100, 20)
  print(a)
  print (b)
  print(f"total price of books are {a+b}")
  print(hb)
  #print(book (input("book ka naam : "),input("writer ka naam : ")))

class Handbook(Book) :
  def __init__ (self , name , auther , price, pages ) :
     super().__init__(name,auther,price)
     self._pages = pages

  @property
  def pages(self):
      return self._pages

  def __str__(self):
      return f"{self.title} has Number of Pages: {self.pages} is written by {self.author}"



if  __name__ == '__main__':
 main ()
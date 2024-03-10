def main() :
  x = "this is just a string"
  print (x)
  print (x[-1])
  print (x[2:10])
  print (area(10,10,"rectangle")) #default value function
  pattern (4) #function
  print (f"perimeter of a circle with radius 7 is {circle(7)[1]}, diameter is {circle(7)[2]} and area is {circle(7)[0]}") #multiple return value function
  
def area(b,h,shape='trianle'):
  if (shape == 'rectangle'):
      return b*h
  return 0.5*b*h

def pattern (n):
   for i in range(n):
      s = ''
      for j in range(i+1):
          s = s + '*'
      print(s)
      '''for i in range(1,n+1):
            for j in range (i):
               print ("*",end=" ")
            print ("\n")'''

def circle(r):
  return 22/7*r**2, 2*22/7*r, 2*r
  #returns area, perimeter and diameter as tuple

if __name__ =="__main__":
  main ()


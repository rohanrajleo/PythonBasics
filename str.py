def main() :
  x = "this is just a string"
  print (x)
  print (x[-1])
  print (x[2:10])
  print (jo(10,10,"rectangle")) #default value function
  pattern (4) #function
def jo (b,h,shape='trianle'):
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

if __name__ =="__main__":
  main ()


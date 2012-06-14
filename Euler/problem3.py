'''
Created on Jun 8, 2012

@author: yamilasusta
'''

def prime(x):
  for i in range(x):
    if(x%i==0):
      return False;
  return True;

def main():
  x = 600851475143
  result = 0
  i = 0
  
  while i in range(x):
    if x % i == 0: # es factor
      if prime(i):
        print i
        result = i
        print result
    i += 1

if __name__ == '__main__':
  main()
  
  
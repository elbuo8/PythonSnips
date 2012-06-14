'''
Created on Jun 7, 2012

@author: yamilasusta
'''

total = 2
atotal = 2
first = 1

second = 2

while atotal < 4000000:
  temp = first + second
  atotal = temp
  if temp%2 == 0:
    total += temp
  first = second
  second = temp
  print total

  
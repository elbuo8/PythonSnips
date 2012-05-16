'''
Created on May 16, 2012

@author: yamilasusta
'''

from locale import str
x = 0
for i in range(5): 
    x += float(input("Insert test " + str((i+1)) + " grade\n"))
examenes = float((x/5)*0.5)
print("Exam grade " + str(examenes))

x = 0
for i in range(2):
    x += float(input("Insert project " + str((i+1)) + " grade\n"))    
proyectos12 = float((x/2)*0.15)

proyecto3 = float(float(input("Insert P3 grade\n"))*.10)

print("Project grade " + str((proyectos12+proyecto3)))

bono = float(input("Insert bonus\n"))

final = float(float(input("Insert final\n"))*0.25)

total = examenes + proyecto3 + proyectos12 + final + bono

print total
    


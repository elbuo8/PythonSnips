'''
Created on May 16, 2012

@author: yamilasusta
'''

from locale import str

reader = open("lines.dat","r")

result = ""
total = 0

lines = reader.readlines()
reader.close()

for line in range(lines.__len__()):
    total += lines[line].__len__() - 1
    result += str(lines[line].__len__() - 1) + ", " + str(total) + "\n"

writer = open("lines.dat", "w")
writer.write(result)
writer.close()
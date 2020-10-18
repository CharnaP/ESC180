##Week 1

value_string = "Hewwo" #in quotes is a string
value_int = 4           #an integer
value_float = 4.0       #a float has a decimal
value_booean = True     #True or False are booleans

print("I said", value_string) #comma to seperate
print(value_int+value_float) #addition works (float+int=float)

'''quadratic eqn'''
import math #gets this library

import math

a = 2
b = -20
c = 1
disc = b**2-4*a*c

if disc > 0:
    r1 = (-b + math.sqrt(disc))/(2*a)
    r2 = (-b - math.sqrt(disc))/(2*a)
    print("Two roots:", round(r1,2), round(r2,2))
elif disc == 0: #won't go as it's a complex number
    r = (-b + math.sqrt(disc))/(2*a)
    print("One root:", round(r))
else:
    print("There are no real solutions")

'''converting ints, floats and strings, rounding'''
og_float=8.7
a=int(og_float)   #converts to int (i.e. ignore decimal)
b=float("3.2")   #converts string to float
c=round(5.55, 1)     #rounds 5.55 to 1 dec. places
print("Our converted are:\n", a,b,c) #\n new line



##Conditionals
'''if <condition>: <block1> else: <block2>
if condition is True <block1> is executed ot else <block2> is'''

#A and B --> if A=True, B=False then False
#A or B --->if A=True B=False, then True
#A and not B -> if A=True and B=False then True
lazy = False
smart = True
growthmindset = False

if not lazy and smart and growthmindset:
    print("Go to EngSci") #Mindset was False
elif  lazy and smart:
    print("Go to Physics") #Lazy False
elif not lazy and smart and not growthmindset:
    print("Go to Economics") #runs this
else:
    print("Go to Ryerson")

'''booleans can be transformed: False are "" and 0'''
print(bool(0)) #False
print(bool("")) #False
print(bool(2.3)) #True
print(bool("LMAO")) #True
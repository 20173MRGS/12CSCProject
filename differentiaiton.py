from random import *

a = randint(1,10)
b = randint(1,10)
question = ('f(x)= ' + str(a) +"x^" + str(b))
print(question)
answer = input('differentiate f(x)= ' + str(a) +"x^" + str(b) +": ")
if answer == str(str(a*b) + "x^" + str(b-1)):
    print("Correct")
else:
    print("Incorrect")
    print("dy/dx= " + str(a*b) + "x^" + str(b-1))







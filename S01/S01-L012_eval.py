import math

argument_list = [float(x)/10 for x in range(0,100)]

function = input("Write a function to be evaluated in python, x is argument")

for x in argument_list:
    print("%3.2f, %4.2f " %(x,eval(function)))



#!/usr/bin/env python3

def happy_new_year():
    i = 11
    while i > 1:
        i-=1
        print(i)
        print("Happy New Year!")
    pass

def square_integers(int_list):
    new_list =[]
    for int in int_list:
        square = int**2
        new_list.append(square)
    return new_list
    # code goes here!
    pass

def fizzbuzz():
    for i in range(1,101):
        if(i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz")
        elif(i % 3 == 0):
            print("Fizz")
        elif(i % 5 == 0):
            print("Buzz")
        else: print (i)            
    pass

import math

def introduction_message ():
    print ("This program prints the roots of a second order equation")
    print(" ax^2 +bx + c= 0")
    print()

def input_and_solve ():
    a =int (input("please enter a: "))
    b = int (input ("please enter b: "))
    c = int (input ("please enter c: "))
    delta = b*b - 4*a*c

    x1 = -b + math.sqrt (delta)
    x2 = -b - math.sqrt(delta)

    print("The Roots are:")
    print ("x1 = ", x1)
    print ("x2 = ", x2)

def final_message():
    print("Thank you for the using this Program...")
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
    print ("All rights Preserved.")
    
introduction_message ()
input_and_solve()
final_message ()

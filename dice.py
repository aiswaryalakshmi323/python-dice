#1.random number generaton
#2.design the system
import random


#print(x)#range 1 to 6
#print(x)
userinput='y'

while userinput=='y':
    x=random.randint(1,6)
    if x==1:
        print("--------")
        print("|      |")
        print("|  *   |")
        print("|      |")
        print("--------")
    if x==2:
        print("--------")
        print("|      |")
        print("|*    *|")
        print("|      |")
        print("--------")
    if x==3:
        print("--------")
        print('|*     |')
        print("|   *  |")
        print("|     *|")
        print("--------")
    if x==4:
        print("--------")
        print("|*    *|")
        print("|      |")
        print("|*    *|")
        print("--------")
    if x==5:
        print("--------")
        print("|*    *|")
        print("|   *  |")
        print("|*    *|")
        print("--------")
    if x==6:
        print("--------")
        print("|*    *|")
        print("|*    *|")
        print("|*    *|")
        print("--------")
    userinput = input("Do you want to continue (y or n)??")

import sys
if(len(sys.argv) > 2):
    print("AssertionError: more than one argument are provided")
    exit()
elif not sys.argv[1].isdigit():
    print("AssertionError: argument is not an integer")
    exit()
x=int(sys.argv[1])
if(x == 0):
    print("I'm Zero")
elif ((x % 2) == 0):
    print("I'm Even.")
elif (x % 2):
    print("I'm Odd.")
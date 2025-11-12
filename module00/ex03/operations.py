import sys
if(len(sys.argv) != 3):
    print("AssertionError: too many arguments")
    exit()
try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
except  ValueError:
    print("AssertionError: only integers")
    exit()
print("sum:\t", int(sys.argv[1]) + int(sys.argv[2]))
print("Difference:\t", int(sys.argv[1]) - int(sys.argv[2]))
print("Product:\t", int(sys.argv[1]) * int(sys.argv[2]))
try:
    print("Quotien:\t", int(sys.argv[1]) / int(sys.argv[2]))
except ZeroDivisionError:
    print("Quotien:\t" +"ERROR (division by zero)")
try:
    print("Remainder:\t", int(sys.argv[1]) % int(sys.argv[2]))
except ZeroDivisionError:
    print("Remainder:\t" +"ERROR (division by zero)")
# Difference: A-B
# Product: A*B
# Quotient: A/B
# Remainder: A%B)
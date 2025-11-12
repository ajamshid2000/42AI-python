import sys
newlist = ["".join(reversed(x.swapcase())) for x in sys.argv[1:]]
newlist.reverse()
print(*newlist, sep = " ")


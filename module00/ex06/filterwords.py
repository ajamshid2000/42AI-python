# import re
import sys

if(len(sys.argv) != 3 or not sys.argv[1].isprintable() or not sys.argv[2].isnumeric()):
    print("ERROR")
    exit()

# s = ''.join(filter(str.isalnum, s))
# s = ''.join([i for i in s if i.isalpha()])
# regex = re.compile('[^a-zA-Z]')
# a= regex.sub('', sys.argv[1])
# list_of_words = [regex.sub('', x) for x in sys.argv[1].split()[:int(sys.argv[2])]]

# i could use the mthods above too to do the same thing i have done below
list_of_words = [w for w in (''.join([i for i in x if i.isalpha()]) for x in sys.argv[1].split()) if len(w) > int(sys.argv[2])]
# if(len(list_of_words) < int(sys.argv[2])):
#     list_of_words = []
print(list_of_words)

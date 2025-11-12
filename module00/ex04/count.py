import sys

def text_analyzer(text = None):
    """
    this funtion takes a single string argument and displays
    the sums of its upper-case characters, lower-case characters, punctuation characters and
    spaces.
    it first checks if the argument is str and niether empty nor None,
    prints error and return if the case above is true.
    
    Parameter
    ---------
    text : str
    
    
    return
    ---------
    None
    
    """
    spaces_count = 0
    upper_count = 0
    lower_count = 0
    punc_count = 0
    
    if(text == "" or text == None):
        text = input("What is the text to analyze?\n")
    if(not type(text) == str):
        print ("AssertionError: argument is not a string")
        return
    for x in text:
        if x == ' ': spaces_count += 1
        elif x.isupper(): upper_count += 1
        elif x.islower(): lower_count += 1
        elif x.isprintable() and not x.isdigit(): punc_count += 1
            # print(str(x))
    print("- " + str(upper_count) + " upper letter(s)")
    print("- " + str(lower_count) + " lower letter(s)")
    print("- " + str(punc_count) + " punctuation mark(s)")
    print("- " + str(spaces_count) + " space(s)")

if(len(sys.argv) >= 2):
    print("One argument needed!")
else: text_analyzer(sys.argv[1])    
            
#     - 2 upper letter(s)
# - 113 lower letter(s)
# - 4 punctuation mark(s)
# - 18 space(s
    
    
# text_analyzer("Python 2.0, released 2000, introduced features like List comprehensions and a garbage collection system capable of collecting reference cycles.")

# Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace.
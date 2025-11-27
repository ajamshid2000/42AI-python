
from random import randint
def generator(text, sep=" ", option=None):
    '''
    Splits the text according to sep value and yield the substrings.
    option precise if a action is performed to the substrings before it is yielded.
    '''
    if(not isinstance(text, str) or not text.isprintable()):
        exit(print("ERROR"))
    
    splited_text = text.split(" ")
    
    if(option == "shuffle"):
        for x in range(len(splited_text)):
            number = randint(0 , len(splited_text) - 1)
            splited_text[x], splited_text[number] = splited_text[number], splited_text[x]
    elif(option == "unique"):
        return(list(set(splited_text)))
    elif(option == "ordered"):
        splited_text.sort()
    elif(option != None):
        return("ERROR")

    for x in splited_text:
        yield x

text = "Le Lorem Ipsum est simplement du faux texte."
for word in generator(text, sep=" "):
    print(word)
print("----------------------------")
for word in generator(text, sep=" ", option="shuffle"):
    print(word)
print("----------------------------")
for word in generator(text, sep=" ", option="ordered"):
    print(word)
print("----------------------------")
text = 1
for word in generator(text, sep=" ", option="unique"):
    print(word)

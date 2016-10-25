code 

def stringRev (word):
    worLen = len(word)          #getting the lenght of the list
    if worLen == 1:
        return word
    else:
        return [word[-1]] + stringRev(word[:-1])    #reversing the list using recursion

    
sentence = "This is Awesome"
listWord = sentence.split()         #splitting the string into a list
output = (stringRev(listWord))      #storing the function into a new varible
new = ' '.join(output)              #converting the list back into a string
print(new)

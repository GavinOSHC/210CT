psuedocode 

string <- enter sentance
string <- string.split()

STRINGREV(string):
    stringLength <- length(string)
    if stringLength equal to 1:
        return string
    else:
        return[string[-1]] + STRINGREV(string[:-1])
    
string <- convert back to string


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


#The bigO notation for this algorithm O(n) as if will only through each element of the list and reverse it.
#Meaning it will only run n number of times. 

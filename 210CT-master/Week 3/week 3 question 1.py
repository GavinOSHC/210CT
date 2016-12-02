def stringRev (word):
    worLen = len(word)          #getting the lenght of the list                         
    if worLen == 1:
        return word
    else:
        return [word[-1]] + stringRev(word[:-1])    #reversing the list using recursion

    
sentence = "This is Awesome"
listWord = sentence.split()         #splitting the string into a list
output_of_word = (stringRev(listWord))      #storing the function into a new varible
new_word = ' '.join(output)              #converting the list back into a string
print(new_word)


#The bigO notation for this algorithm O(n) as if will only through each element of the list and reverse it.
#Meaning it will only run n number of times.

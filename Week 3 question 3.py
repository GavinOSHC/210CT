code

def remove_vowels(s):
    if not s:       #is the string is empty return s 
        return s
    elif s[0] in "aeiouAEIOU":      #first character is a vowel
        return remove_vowels(s[1:]) #skip first letter
    return s[0] + remove_vowels(s[1:]) #return the first letter 

s = "beautiful"
print(remove_vowels(s))

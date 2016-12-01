def remove_vowels(s):
    if not s:       #is the string is empty return s 
        return s
    elif s[0] in "aeiouAEIOU":      #first character is a vowel
        return remove_vowels(s[1:]) #skip first letter
    else:
        return s[0] + remove_vowels(s[1:]) #return the first letter 


s = "beautiful"
print(remove_vowels(s))




# The bigO noation for this algorithm if O(n) as the algorithm will only run n number times.
# As is it will go through the whole string and check if each letter is a vowel and remove it.

def anagramCheck(str1, str2):
    """
    anagram is a  word, phrase, or name formed by rearranging the letters of another, such as spar, formed from rasp.
    The function checks if the provided strings are anagrams or not.
    param: str1
    param:
    """
    if (sorted(str1) == sorted(str2)) :  
        return True 
    else :  
        return False 
str1 = input("Please enter String 1 : ")
str2 = input("Please enter String 2 : ")
if anagramCheck(str1,str2):
    print("Anagram")
else:
    print("Not an anagram")
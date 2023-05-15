class Solution:
    def isPalindrome(self, s: str) -> bool:
        string=""
        for char in s:
            if char.isalnum():
                string+=char
        return string[::-1].casefold() == string.casefold()
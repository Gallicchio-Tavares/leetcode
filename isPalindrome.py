class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_string = str(x)
        string_invertida = num_string[::-1]
        if num_string == string_invertida:
            return True
        else:
            return False

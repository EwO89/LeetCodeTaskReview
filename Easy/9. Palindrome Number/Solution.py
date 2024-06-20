# с преобразованием числа в строку:

class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_form = str(x)
        if str_form == str_form[::-1]:
            return True
        return False


# без преобразования числа в строку:

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        input_number = x
        palindrome_number = 0
        while x > 0:
            received = x % 10
            palindrome_number = palindrome_number * 10 + received
            x //= 10
        if input_number == palindrome_number:
            return True
        return False

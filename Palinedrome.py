class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        if x < 10:
            return True  
        div = 1
        while x >= div:
            div *= 10
        div //= 10

        while x > 0:
            if x < div:  
                digit1 = x
                break
            digit1 = x // div
            digit2 = x % 10
            if digit1 != digit2:
                return False
            x = (x % div) // 10
            div //= 10
        return True

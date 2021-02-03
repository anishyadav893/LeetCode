class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x in range(10):
            return True
        
        if (x % 10 == 0) or x < 0:
            return False
        
        s = str(abs(x))
        if s == s[::-1]:
            return True
        
        return False
    
'''
Runtime: 52 ms, faster than 90.78% of Python3 online submissions for Palindrome Number.
Memory Usage: 14.2 MB, less than 51.27% of Python3 online submissions for Palindrome Number.

Can be written in a more elegant way biut this solution covers all the edge cases.
'''
class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            ans = int(str(x)[::-1])
        else:
            ans = -1 * int(str(x * -1)[::-1])
        
        if ans not in range(-2**31, 2**31 - 1):
            return 0
        else:
            return ans
        
        '''
        Runtime: 28 ms, faster than 84.84% of Python3 online submissions for Reverse           Integer.
        Memory Usage: 14.2 MB, less than 48.79% of Python3 online submissions for             Reverse Integer.
        '''
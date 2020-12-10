class Solution:
    def longestPalindrome(self, s: str) -> str:
        def help_func(l, r):
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                l -= 1
                r += 1
            
            return s[l+1:r]
        
        ans = ''
        
        for i in range(len(s)):
            test_case = help_func(i, i)
            if len(test_case) > len(ans):
                ans = test_case
            test_case = help_func(i, i+1)
            if len(test_case) > len(ans):
                ans = test_case
        
        return ans
    
    '''
    Runtime: 1048 ms, faster than 52.77% of Python3 online submissions for Longest       Palindromic Substring.
    Memory Usage: 14.2 MB, less than 63.65% of Python3 online submissions for           Longest Palindromic Substring.
    '''
    
    
    # The below mentioned solutions are correct but exceed runtime
        '''if not s:
            return s

        res = ""
        for i in range(len(s)):
            j = i + 1
            
            while j <= len(s) and len(res) <= len(s[i:]):
                if s[i:j] == s[i:j][::-1] and len(s[i:j]) > len(res):
                    res = s[i:j]
                j += 1

        return res'''
    
    '''ans = ''
        temp = ''
        
        for i in range(1, len(s)):
            p1 = i-1
            p2 = i+1
            
            while p1 >= 0 and p2 < len(s):
                if s[p1] == s[p2]:
                    p1 -= 1
                    p2 += 1
            
            temp = s[p1:p2 + 1]
            
            if len(temp) > len(ans):
                ans = temp
            temp = ''
        
        return ans'''
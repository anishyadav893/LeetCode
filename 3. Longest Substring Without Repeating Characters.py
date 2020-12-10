class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = []
        max_length = 0
        
        for i in s:
            if i in answer:
                answer = answer[answer.index(i) + 1:]
            
            answer.append(i)
            
            max_length = max(len(answer), max_length)
        
        return max_length
    
'''
Runtime: 68 ms, faster than 51.43% of Python3 online submissions for Longest Substring Without Repeating Characters.

Memory Usage: 14.4 MB, less than 11.33% of Python3 online submissions for Longest Substring Without Repeating Characters.
'''
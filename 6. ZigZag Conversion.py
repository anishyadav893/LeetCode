class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows > 1:
            line = 0
            multiplier = 1
            output = [''] * numRows
            
            for i in range(len(s)):
                output[line] += s[i]
                line += multiplier
                
                if (line == 0) or (line == numRows - 1):
                    multiplier *= -1
            
            answer = ''
            for j in output:
                answer += j
                
            return answer
        else:
            return s
        
'''
Runtime = 52 ms
Memory = 14.2 MB

The layout of the output in the question is misleading and the problem
can be solved by using arrays.

Create an empty array with number of elements equal to numRows.
Start with the first element of the input string, add the item in the
new array and move on to the second one.
When you hit either of the end-points (first or the last element of your created array), reverse your direction with the help of a multiplier
'''
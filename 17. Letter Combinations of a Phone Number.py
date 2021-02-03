class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keypad = {
            '' : [],
            '2': 'abc', 
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        if len(digits) < 2:
            return keypad[digits]
        
        result = ['']
        
        for i in digits:
            temp = []
            for char in keypad[i]:
                temp += [r + char for r in result]

            result = temp

        return result
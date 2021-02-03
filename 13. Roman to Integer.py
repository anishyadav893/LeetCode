class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I":1, 
            "IV":4,
            "V":5,
            "IX":9,
            "X":10,
            "XL":40,
            "L":50,
            "XC":90,
            "C":100,
            "CD":400,
            "D":500,
            "CM":900,
            "M":1000
        }
        
        num = 0
        
        arr = ["CM","CD","XC","XL","IX","IV"]
        for i in arr:
            if i in s:
                num = num + roman[i]
                s=s.replace(i,"")
        for i in s:
            num += roman[i]
        return num
class Solution:
    def myAtoi(self, s: str) -> int:
        empty = ''
        r = 0
        s = s.lstrip()
        if s[:1] != '-' and s[:1] != '+' and not s[:1].isdigit():
            return 0
        else:
            counter = 0
            for x in s:            
                if counter == 0 and (x == '-' or x == '+'):
                    counter += 1
                else:
                    if x.isdigit():
                        empty += x
                    else:
                        break
                counter += 1
        if not empty:
            return 0
        else:
            if s.index(empty) == 0:
                r = int(empty)
            else:
                r = int(s[s.index(empty) - 1:s.index(empty)] + empty)

            if r < -2**31:
                return -2**31
            elif r > 2**31-1:
                return 2**31-1
            else:
                return r
            
            
            
'''
Another soluion, more precise and much simpler -
def myAtoi(self, s: str) -> int:
    match = re.match(r'^\s*([+-]?\d+)', s)
    return min(max((int(match.group(1)) if match else 0), -2**31), 2**31 - 1)
'''
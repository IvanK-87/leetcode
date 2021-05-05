class Solution:
    def intToRoman(self, num: int) -> str:
        roman_num = [1, 5, 10, 50, 100, 500, 1000, 5000]
        roman_str = ['I', 'V', 'X', 'L', 'C', 'D', 'M', 'W']
        val = [0]*8
        for i in reversed(range(7)):
            val[i] = num // roman_num[i]
            num = num - val[i]*roman_num[i]
            
        output = ''
        for i in range(0,7,2):
            if val[i+1] == 1:
                if val[i] == 4:
                    output = roman_str[i] + roman_str[i+2] + output
                else:
                    for j in range(val[i]):
                        output = roman_str[i] + output
                    output = roman_str[i+1] + output
            else:
                if val[i] == 4:
                    output = roman_str[i] + roman_str[i+1] + output
                else:
                    for j in range(val[i]):
                        output = roman_str[i] + output
        return output
                        
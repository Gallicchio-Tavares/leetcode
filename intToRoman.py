class Solution:
    def intToRoman(self, num: int) -> str:
        valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romanos = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        
        resp = ""
        for i in range(len(valores)):
            while num >= valores[i]:
                resp += romanos[i]
                num -= valores[i]
        
        return resp

solution = Solution()
print(solution.intToRoman(1994))
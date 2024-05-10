class Solution:
    def romanToInt(self, s: str) -> int:
        romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        anterior = 0
        
        for char in reversed(s):
            atual = romanos[char]
            if atual < anterior:
                total -= atual
            else:
                total += atual
            anterior = atual
        
        return total

solution = Solution()
print(solution.romanToInt("MDIX"))

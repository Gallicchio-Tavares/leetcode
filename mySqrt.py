class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        
        inicio = 1
        fim = x
        while inicio <= fim:
            meio = inicio + (fim - inicio) // 2
            if meio == x // meio:
                return meio
            elif meio > x // meio:
                fim = meio - 1 # significa q esta entre o inicio e o meio
            else:
                inicio = meio + 1 # significa que está entre o meio e o fim
        return fim

sol = Solution()
print(sol.mySqrt(8))
print(sol.mySqrt(1))

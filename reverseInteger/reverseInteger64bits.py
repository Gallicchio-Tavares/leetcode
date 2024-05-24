class Solution:
  def acontecer(self, num: str) -> str:
    if num[-1] != 0:
        return num[::-1]
    else:
        num_alt = ''
        for char in reversed(num):
            if char == '0':
                num_alt = num[:char] + num[char+1]
        return num_alt  
         
  def reverse(self, x: int) -> int:
    num = str(x)
    if x > 0:
      return int(self.acontecer(num))
            
    else: # se for numero negativo
      num_alt = num.replace('-', '')
      num = self.acontecer(num_alt)
      num = '-' + num
      return int(num)

solution = Solution()
print(solution.reverse(123))
print(solution.reverse(-123))
print(solution.reverse(120))
print(solution.reverse(1000))
print(solution.reverse(-1534236469))

from typing import List

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        possivel = set()
        
        for n in unique_nums:
            if n < 0 and -n in unique_nums:
                possivel.add(-n)
        
        if not possivel:
            return -1
        return max(possivel)
    
sol = Solution()
print(sol.findMaxK([-1,2,-3,3]))  #3
print(sol.findMaxK([-1,10,6,7,-7,1]))  #7
print(sol.findMaxK([-10,8,6,7,-2,-3]))  #-1

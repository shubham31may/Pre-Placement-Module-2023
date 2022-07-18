class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new = []
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            
            if abs(nums[left]) < abs(nums[right]):
                new.append(nums[right]**2)
                right -=1
            else:
                new.append(nums[left]**2)
                left +=1
                
                
        return new[::-1]
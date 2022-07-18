class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pointer = 0
        counter = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                counter += 1
                continue
            else:
                nums[pointer] = nums[i]          
                pointer += 1    
        for i in range(counter):
            nums[-i-1] = 0
class Solution:
    def firstBadVersion(self, n: int) -> int:
        nums = range(1, n + 1)
        l = 0
        h = len(nums)
        mid = 0
        while l <= h:
            mid = (h + l) // 2
            if isBadVersion(nums[mid]):
                if mid == 0:
                    return nums[0]  # first ver
                if not isBadVersion(nums[mid-1]):
                    return nums[mid]
                else:
                    h = mid - 1
            else:
                l = mid + 1
        return None
                                                                                                                                                                                                                                                
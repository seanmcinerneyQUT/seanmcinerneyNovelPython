class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums)<=4:
            return 0
        nums = sorted(nums)
        D = [nums[i+1]-nums[i] for i in range(len(nums)-1)]
        return sum(D) - max(
            D[0]+D[1]+D[2],
            D[0]+D[1]+D[-1],
            D[0]+D[-1]+D[-2],
            D[-1]+D[-2]+D[-3])

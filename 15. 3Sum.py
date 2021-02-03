class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums) # O(nlogn)
        result = set()
        for k in range(len(nums)):
            target = -nums[k]
            i,j = k+1, len(nums)-1
            while i < j:
                sum_two = nums[i] + nums[j]
                if sum_two < target:
                    i += 1
                elif sum_two > target:
                    j -= 1
                else:
                    result.add((nums[k],nums[i],nums[j]))
                    i += 1
                    j -= 1
        return result
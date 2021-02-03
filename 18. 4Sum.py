class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        m = collections.defaultdict(list)
        result = set()
        
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                m[nums[i] + nums[j]].append((i,j))
        
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                remaining = target - nums[i] - nums[j]
                for pair in m[remaining]:
                    if i > pair[1]:
                        result.add((nums[pair[0]], nums[pair[1]], nums[i], nums[j]))
        
        return list(result)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if target == nums[i] + nums[j]:
                    result.append(i)
                    result.append(j)
        return result

'''
Time compexity is O(n^2)
and Space complexity is O(1)
Runtime = 472 ms
Memory = 14.5 MB'''

# with the help of hashmap

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    	empty = {}

    	for index, value in enumerate(nums):
    		n = target - value
    		if n not in empty:
    			empty[value] = i
    		else:
    			return [empty[n], i]
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)

        resus = sum(nums[0:3])

        for i in range(len(nums) - 2):
            start = i + 1
            end = len(nums) - 1

            while(start < end):
                tem = nums[i] + nums[start] + nums[end]
                v = tem - target

                if(abs(v) < abs(resus - target)):
                    resus = tem

                if(v == 0):
                    return target
                elif(v > 0):
                    end -= 1
                else:
                    start += 1

        return resus
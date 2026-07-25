class Solution(object):
    def twoSum(self, nums, target):

        hashmap = {}

        for i in range(len(nums)):

            comp = target - nums[i]

            if comp in hashmap:
                return [hashmap[comp], i]

            hashmap[nums[i]] = i
        
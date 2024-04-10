class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        if not nums:
            raise ValueError("Input list cannot be empty")

        map = {}
        for i in range(len(nums)):
            ele = target - nums[i]

            if ele not in map:
                map[nums[i]] = i
            else:
                return [map[ele], i]

        return []  # If no pair is found, return an empty list

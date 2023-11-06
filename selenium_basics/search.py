nums = [3, 4, 9, 6, 4]
target = 12


# for i in nums:
#     for x in nums[nums.index(i)+1:]:
#         if i + x == target:
#             result = [nums.index(i), nums.index(x)]
#             print(result)

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        seen = {}

        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], i]
            elif num not in seen:
                seen[num] = i


sol = Solution()
print(sol.twoSum(nums, target))
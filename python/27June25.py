from typing import List


class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        evenSum = 0
        oddSum = 0

        for i in range(len(nums)):
            if (nums[i] % 2 == 0):
                evenSum += nums[i]
            else:
                oddSum += nums[i]

            if (target[i] % 2 == 0):
                evenSum += target[i]
            else:
                oddSum += target[i]

        return abs(evenSum-oddSum)//4

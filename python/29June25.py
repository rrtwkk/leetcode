class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        top_k = sorted(zip(nums, range(len(nums))),
                       key=lambda x: x[0], reverse=True)[:k]
        top_k.sort(key=lambda x: x[1])

        return [num for num, _ in top_k]

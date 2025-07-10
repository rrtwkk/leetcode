"""
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/submissions/1677505780/
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        length = len(s)
        dict = ("a", "e", "i", "o", "u")

        if (length < k):
            for i in range(length):
                if (s[i] in dict):
                    count += 1
            return count

        for i in range(k):
            if (s[i] in dict):
                count += 1

        max_count = count
        for i in range(k, length):
            if (s[i] in dict):
                count += 1
            if (s[i-k] in dict):
                count -= 1
            max_count = max(max_count, count)

        return max_count

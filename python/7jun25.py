import heapq
"""
https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/?envType=daily-question&envId=2025-06-07
"""


class Solution:
    def clearStars(self, s: str) -> str:
        # Convert string to list for easier character manipulation
        ans = list(s)
        heap = []      # Initialize a heap to track characters

        for i, char in enumerate(s):
            if char == '*' and heap:  # If current char is '*' and heap is not empty
                # Pop the smallest element from heap
                del_char, j = heapq.heappop(heap)
                # Remove the character at position -j (note the negative index)
                ans[-j] = ''
                ans[i] = ''   # Remove the '*' character
            else:
                # Push (char, negative index) to heap
                heapq.heappush(heap, (char, -i))

        return ''.join(ans)  # Join the list back into a string

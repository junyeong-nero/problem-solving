from typing import List
from itertools import accumulate
from bisect import bisect_left, bisect_right

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        
        temp = sorted(list(set(range(1, n + 1)) - set(banned)))
        temp = list(accumulate(temp))
        index = bisect_right(temp, maxSum)

        return index

res = Solution().maxCount()
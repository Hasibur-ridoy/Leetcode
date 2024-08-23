import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # initialize pointers for the binary search tree in the piles array
        l,r = 1, max(piles)

        # result is set to worst case scenario, so it is set to the highest number in the array
        res = r

        # Binary search tree (l and r pointer crosses each-other than the loop will end)
        while l <= r:
            # find the middle value of the array
            # l + ((r-l) // 2) this is used for program not overflowing due to adding integer values
            k = l + ((r-l) // 2)

            # How many hours will koko take to eat one pile of banana. This will be compared with target value(h)
            hours = 0

            for p in piles:

                # Here every pile is getting divided by mean(k) value. ex: [3, 6, 7, 11],
                # for k = 6, math.ceil(3 / 6) = 1 hour
                # math.ceil(6 / 6) = 1 hour
                # math.ceil(7 / 6) = 2 hour
                # math.ceil(11 / 6) = 2 hour
                hours += math.ceil(p/k)

            if hours <= h:
                # updating res value
                res = min(res, k)

                r = k - 1
            else:
                l = k + 1
        return res
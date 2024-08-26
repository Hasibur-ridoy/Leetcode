from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        total = len(a) + len(b)
        half = total // 2

        if len(a) > len(b):
            a, b = b, a

        l, r = 0, len(a) - 1

        while True:
            m = l + ((r-l) // 2)
            n = half - m - 2
            # The subtraction of 2 is actually because m is the index of the last element in the left half of a,
            # and n is the corresponding index in b.
            # The formula n = half - m - 2 is used to maintain the correct alignment of the halves
            # between the two arrays.

            aleft = a[m] if m >= 0 else float("-infinity")
            aright = a[m+1] if (m+1) < len(a) else float("infinity")
            bleft = b[n] if n >= 0 else float("-infinity")
            bright = b[n+1] if (n+1) < len(b) else float("infinity")

            if aleft <= bright and bleft <= aright:
                if total % 2:
                    return min(aright, bright)
                return (max(aleft, bleft) + min(aright, bright)) / 2
                # Incorrect Division Operator: The line return (max(aleft, bleft) + min(aright, bright)) // 2
                # should use floating-point division /
                # instead of integer division // to correctly calculate the average of two numbers
            elif aleft > bright:
                r = m - 1
            else:
                l = m + 1
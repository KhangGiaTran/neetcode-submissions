class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def finishEating(k) -> int:
            hours = 0
            for pile in piles:
                hours += math.ceil(float(pile) / k)
            return hours

        l, r = 1, max(piles)

        min_k = r
        
        while l <= r:
            mid = (l + r) // 2
            hours = finishEating(mid)
            if hours > h:
                l = mid + 1
            else:
                r = mid - 1
                min_k = mid

        return min_k
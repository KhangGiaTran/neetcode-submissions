class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def finish(self, rate):
            hours = h
            for p in piles:
                h_consume = math.ceil(p / rate) 
                hours -= h_consume
            return hours >= 0
        
        left_k = 1
        right_k = 1
        for p in piles:
            right_k = max(p, right_k)
        
        min_k = right_k
        while left_k <= right_k:
            mid = (left_k + right_k) // 2
            
            if finish(self, mid):
                min_k = min(mid, min_k)
                right_k = mid - 1
            else:
                left_k = mid + 1

        return min_k 
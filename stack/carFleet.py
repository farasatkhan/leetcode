from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [float(target - p) / s for p, s in sorted(zip(position, speed))]

        res = cur = 0

        for t in time[::-1]:
            if t > cur:
                res += 1
                cur = t
    


target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]

solution = Solution()
res = solution.carFleet(target, position, speed)
print(res)
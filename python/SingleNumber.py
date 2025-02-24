class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        compteur = 0
        for i in nums:
            for j in nums:
                if i == j:
                    compteur += 1
            if compteur == 1:
                return i
            compteur = 0

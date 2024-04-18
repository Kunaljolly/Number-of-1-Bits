class Solution:
    def hammingWeight(self, n: int) -> int:
        b = list(bin(n)[2:])
        return b.count("1")

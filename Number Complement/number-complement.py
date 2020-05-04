# Answered as a part of Leetcode's May challenge
# https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3319/
#
class Solution:
    def findComplement(self, num: int) -> int:
        return int(''.join([f"{1-int(c)}" for c in bin(num)[2:]]), 2)
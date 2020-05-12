# Answered as a part of leetcode's May challenge
# https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3324/
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return True if num**.5%1 == 0 else False
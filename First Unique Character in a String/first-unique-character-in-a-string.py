# Answered as a part of leetcode's May challenge
# https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3320/
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = defaultdict(lambda:0)
        for c in s:
            d[c]+=1
        for key, value in d.items():
            if value == 1:
                return s.index(key)
        return -1
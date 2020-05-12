# Answered as a part of leetcode's May challenge
# https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3321/
#
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = defaultdict(lambda:0)
        m = len(nums)/2
        for i in nums:
            d[i]+=1
            if(d[i] > m):
                return i
        return false
# Answered as a part of leetcode's May challenge
# https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3327/
#
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        single = True
        if(len(nums) ==1):
            return nums[0]
        for i in range(len(nums)-1):
            if(nums[i] != nums[i+1] and single == True):
                return nums[i]
            single = not single
        return nums[len(nums)-1]
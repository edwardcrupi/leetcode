# Answered as a part of Leetcode's May challenge
# https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3318/
#
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if(ransomNote==''):
            return True
        ransomDict = defaultdict(lambda:0)
        for c in ransomNote:
            ransomDict[c]+=1
        for c in magazine:
            ransomDict[c]-=1
            if(ransomDict[c]==0):
                if(all(i <= 0 for i in ransomDict.values())):
                    return True
        return False
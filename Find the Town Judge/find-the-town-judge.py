# Answered as a part of leetcode's May challenge
# https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3325/
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if(N == 1):
            return 1
        h = defaultdict(lambda:0)
        d = defaultdict(lambda:0)
        max_trust = 0
        judge = -1
        
        for person in trust:
            judge_candidate = person[1]
            truster = person[0]
            h[judge_candidate]+=1
            d[truster] +=1
            if(h[judge_candidate] > max_trust):
                judge = judge_candidate
                max_trust = h[judge]
        if (max_trust >= N-1) and (d[judge] == 0):
             return judge
        else:
            return -1

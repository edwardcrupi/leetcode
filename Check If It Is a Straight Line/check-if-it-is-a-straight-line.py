# Answered as a part of leetcode's May challenge
# https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3323/
# #
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) < 2:
            return False
        if((coordinates[1][0]-coordinates[0][0]) == 0):
            for coord in coordinates[1:]:
                if(coord[0]-coordinates[0][0] != 0):
                    return False
        else:
            gradient = (coordinates[1][1]-coordinates[0][1])/(coordinates[1][0]-coordinates[0][0])
            for coord in coordinates[1:]:
                check = (coord[1] -coordinates[0][1])/(coord[0]-coordinates[0][0])
                if(check != gradient):
                    return False
        return True
# Answered as a part of leetcode's May challenge
# https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3326/
#
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int, oldColor=-1) -> List[List[int]]:
        if(oldColor == -1):
            oldColor = image[sr][sc]
        if(oldColor == newColor):
            return image
        elif(sr >=0 and sc >= 0 and sr < len(image) and sc < len(image[0])):
            if(image[sr][sc] != oldColor):
                return image
            elif(image[sr][sc] == oldColor):
                image[sr][sc] = newColor
                self.floodFill(image, sr-1, sc, newColor, oldColor)
                self.floodFill(image, sr+1, sc, newColor, oldColor)
                self.floodFill(image, sr, sc-1, newColor, oldColor)
                self.floodFill(image, sr, sc+1, newColor, oldColor)
        return image
# Answered as a part of Leetcode's May Challenge
# https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3317/
#
# @param {String} j
# @param {String} s
# @return {Integer}
def num_jewels_in_stones(j, s)
    count = 0
    hash = Hash.new(false)
    j.each_char do |stone|
        hash[stone] = true
    end
    s.each_char do |stone|
        count +=1 if hash[stone]
    end
    count
end
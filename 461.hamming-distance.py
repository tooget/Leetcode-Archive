#
# @lc app=leetcode id=461 lang=python
#
# [461] Hamming Distance
#
# https://leetcode.com/problems/hamming-distance/description/
#
# algorithms
# Easy (70.56%)
# Total Accepted:    251.8K
# Total Submissions: 356.8K
# Testcase Example:  '1\n4'
#
# The Hamming distance between two integers is the number of positions at which
# the corresponding bits are different.
# 
# Given two integers x and y, calculate the Hamming distance.
# 
# Note:
# 0 ≤ x, y < 231.
# 
# 
# Example:
# 
# Input: x = 1, y = 4
# 
# Output: 2
# 
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
# ⁠      ↑   ↑
# 
# The above arrows point to positions where the corresponding bits are
# different.
# 
# 
#
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
        def createListOfBinaryNumber(integerNumber):
            orderedDigitNumber = []
            for i in range(231):
                orderedDigitNumber.append(integerNumber % 2)
                integerNumber = integerNumber // 2
            orderedDigitNumber.reverse()
            # print(orderedDigitNumber)
            return orderedDigitNumber
        
        def calculateHammingDistance(listedNumbers1, listedNumbers2):
            distance = 0
            for i in range(231):
                if listedNumbers1[i] != listedNumbers2[i]:
                    distance += 1
            # print(distance)
            return distance


        listedBinaryOfX = createListOfBinaryNumber(x)
        listedBinaryOfY = createListOfBinaryNumber(y)
        result = calculateHammingDistance(listedBinaryOfX, listedBinaryOfY)

        return result

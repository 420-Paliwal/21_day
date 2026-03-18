class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        n = len(nums)
        for i in range(n):
            need = target - nums[i]
            if need in seen:
                return [seen[need], i]
            seen[nums[i]] = i
        return -1
    
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')
        max_profit=0
        if not prices:
            return 0
        for price in prices:
            if price<min_price:
                min_price=price
            elif price-min_price>max_profit:
                max_profit= price-min_price
        return max_profit

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = {}
        for i in nums:
            if i in seen:
                return True
            else:
                seen[i] = 1
        return False
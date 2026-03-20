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
    
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [1] * n
        left = 1 
        for i in range(n):
            res[i] = left
            left *= nums[i]
        right = 1
        for i in range(n-1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res
    
class Solution(object):
    def maxSubArray(self, nums):
        current_sum = 0
        max_sum = float("-inf")

        for num in nums:
            current_sum += num
            if current_sum > max_sum:
                max_sum = current_sum
            if current_sum < 0:
                current_sum = 0
        return max_sum
    
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_prod = nums[0]
        max_prod = nums[0]
        result = nums[0]
        for num in nums[1:]:
            if num < 0:
                min_prod, max_prod = max_prod, min_prod
            min_prod = min(min_prod*num, num)
            max_prod = max  (max_prod*num, num)
            result = max(result, max_prod)
        return result
    
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        low = 0
        high = n-1
        while low < high:
            mid = (low+high)//2
            if nums[mid] > nums[high]:
                low = mid + 1
            elif nums[mid] <= nums[high]:
                high = mid
        return nums[low]
    
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hash_set1 = {}
        hash_set2 = {}
        for i in s:
            if i not in hash_set1:
                hash_set1[i] = 1
            else:
                hash_set1[i] += 1
        
        for i in t:
            if i not in hash_set2:
                hash_set2[i] = 1
            else:
                hash_set2[i] += 1
        
        return hash_set1 == hash_set2
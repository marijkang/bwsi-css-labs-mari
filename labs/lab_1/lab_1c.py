"""
lab_1c.py

Given a list of numbers, return the maximum sum of any contiguous subarray of the list.

Do not assume anything. Account for all edge cases.

Derived from LeetCode problem: https://leetcode.com/problems/maximum-subarray/ (leetcode medium)
"""

# TODO: Find and resolve the bug in the following implementation. Create unit tests to verify your fix.
def max_subarray_sum(nums: list[int]) -> int:
    """
    Function that takes in a list of integers and returns the maximum sum of any contiguous subarray.

    Args:
        nums (list[int]): List of integers.

    Returns:
        int: The maximum sum of any contiguous subarray.
    """

    total = 0
    result = nums[0]
    
    for num in nums:
        total = max(num, total + num)
        if total > result:
            result = total
            
    return result

# Example usage:
def main():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    #Output: 6
    #Explanation: The subarray [4,-1,2,1] has the largest sum 6.
    result = max_subarray_sum(nums)
    print(f"Maximum subarray sum: {result}")

if __name__ == "__main__":
    main()
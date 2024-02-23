from tdkscripts import LeetCodeTestingScript


'''
Leetcode link : 


Question Title : 268. Missing Number


Question Description : 
    Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.




Sample Input/Output with explanation:
    Example 1:
        Input: nums = [3,0,1]
        Output: 2
        Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
    Example 2:
        Input: nums = [0,1]
        Output: 2
        Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
    Example 3:
        Input: nums = [9,6,4,2,3,5,7,0,1]
        Output: 8
        Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.


Constraints:
    n == nums.length
    1 <= n <= 104
    0 <= nums[i] <= n
    All the numbers of nums are unique.
 
    
    
    
Related Topics: 
    Array
    Hash Table
    Math
    Binary Search
    Bit Manipulation
    Sorting


Follow up: 
    Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?


'''
class Solution:
    #Tested Solution - Please dont alter it
    def solution(self, nums):
        n=len(nums)
        n_sum=(n*(n+1))//2
        return n_sum-sum(nums)
    
    
    # region Section 1: Explanation
    '''
    Solution Desc : 
        Step 1 : FInd the sum 
        Step 2 : Find the sum if all the values are present.. (1+2+3..n) => n(n+1)/2
        Step 3 : Subtract the above two response for the result
    '''
    # endregion
    def missingNumber(self, nums):
        n=len(nums)
        n_sum=(n*(n+1))//2
        return n_sum-sum(nums)
        
    
    

tests_configs={
   "compare_with_solution":0,
    "include_test_exec_comparison":0,
    "include_failed_testcase_comparison":1,
    "include_overall_memory_consumed":1,
    "enable_log":0,
    "memory_log":{
        "enable_memory_log":1,
        "memory_log_details":{
            "enable_peak_memory":1,
            "enable_current_memory":0,
            "byte":1,
            "kilobyte":0,
            "megabyte":0,
        }
    },
    "test_cases":[
        {
            "Input":[[3,0,1]],
            "Output":2
        },
        {
            "Input":[[0,1]],
            "Output":2
                
        },
        {
            "Input":[[9,6,4,2,3,5,7,0,1]],
            "Output":8
        }
    ]
}

sol=Solution()
test= LeetCodeTestingScript(sol)
test.run_tests(sol.missingNumber,tests_configs)
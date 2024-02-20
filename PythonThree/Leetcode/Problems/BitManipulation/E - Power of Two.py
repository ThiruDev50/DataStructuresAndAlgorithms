
from tdkscripts import TestingScript


'''
Leetcode link : https://leetcode.com/problems/power-of-two/

Question Title : 231. Power of Two

Question Description :
    Given an integer n, return true if it is a power of two. Otherwise, return false.
    An integer n is a power of two, if there exists an integer x such that n == 2x.


Sample Input/Output with explanation:
    Example 1:

    Input: n = 1
    Output: true
    Explanation: 20 = 1
    Example 2:

    Input: n = 16
    Output: true
    Explanation: 24 = 16
    Example 3:

    Input: n = 3
    Output: false


Constraints:
    -231 <= n <= 231 - 1
    
    
    
Related Topics: 
    Math
    Bit Manipulation
    Recursion
    
    
    
Follow up: 
    Could you solve it without loops/recursion?




'''
class Solution:
    #Tested Solution - Please dont alter it
    def solution(self,n):
        if(n==0):
            return False
        res =n & (n - 1)
        if(res==0):
            return True
        return False
    
    # region Section 1: Explanation
    '''
    All powers of 2 is the starting point to incease a bit length. 7(111) is 3 bit length, 8(1000) is 4 bit length. 15(1111) is 4 bit length 16(10000) is 5 bit length
    If we do bitwise & with a number and its prev numb, then if the res is 0, It is a power of 2
    
    Eg) 16 as Input 
        16 - 1 0 0 0 0 
        15 - 0 1 1 1 1
        ---------------
        &    0 0 0 0 0 => The Hexadecimal value is 0
        ---------------
    
    '''
    # endregion
    def isPowerOfTwo(self, n: int) -> bool:
        if(n==0):
            return False
        res =n & (n - 1)
        if(res==0):
            return True
        return False
    
    
tests_configs={
    "compare_with_solution":True,
    "enable_log":True,
    "execute_test_case":[1,2,3],
    "test_cases":[
        {
            "Input":[1],
            "Output":True
        },
        {
            "Input":[16],
            "Output":True
                
        },
        {
            "Input":[3],
            "Output":False
        }
    ]
}

sol=Solution()
test= TestingScript(sol)
test.run_tests(sol.isPowerOfTwo,tests_configs)
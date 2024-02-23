

from typing import *
from tdkscripts import LeetCodeTestingScript
'''
Leetcode link : https://leetcode.com/problems/find-the-town-judge/description/


Question Title : 997. Find the Town Judge



Question Description :
    In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

    If the town judge exists, then:

        The town judge trusts nobody.
        Everybody (except for the town judge) trusts the town judge.
        There is exactly one person that satisfies properties 1 and 2.
    You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

    Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.



Sample Input/Output with explanation:
    Example 1:
        Input: n = 2, trust = [[1,2]]
        Output: 2
    Example 2:
        Input: n = 3, trust = [[1,3],[2,3]]
        Output: 3
    Example 3:
        Input: n = 3, trust = [[1,3],[2,3],[3,1]]
        Output: -1


Constraints:
        1 <= n <= 1000
        0 <= trust.length <= 104
        trust[i].length == 2
        All the pairs of trust are unique.
        ai != bi
        1 <= ai, bi <= n
    
    
    
Related Topics: 
    Array
    Hash Table
    Graph


Follow up: 



'''
class Solution:
    #Tested Solution - Please dont alter it
    def solution(self, n: int, trust: List[List[int]]) -> int:
        d={}
        for i in range(1,n+1):
            d[i]=set()
        for i in trust:
            d.get(i[0]).add(i[1])
        judge=None
        for key,value in d.items():
            if len(value)==0:
                judge=key
                break 
        if not judge:
            return -1
        for key,value in d.items():
            if key==judge:
                if (judge in value):
                    return -1
                continue
            if judge not in value:
                return -1
        return judge
    
    
    # region Section 1: Explanation
    '''
    Solution Desc :     
        1. Store in a dictionary key=Person, value=List of persons who key person trust,
        2. Check if judge exists (If He trust no one => value should be empty)=> Yes Step 3, No => return 1
        3. Check if everyone trust judge and judge trust no one.
    '''
    # endregion
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        d={}
        for i in range(1,n+1):
            d[i]=set()
            
        #Key => A, Value => List of TrustedPeople A trust
        for i in trust:
            d.get(i[0]).add(i[1])
        
        judge=None
        # Check if judge exists => Len(TrustedPeople)==0
        for key,value in d.items():
            if len(value)==0:
                judge=key
                break 
        if not judge:
            return -1
       
        #Check everyone trust judge and judge trust no one
        for key,value in d.items():
            if key==judge:
                if (judge in value):
                    return -1
                continue
            if judge not in value:
                return -1
        return judge
                
    

  



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
    "execute_test_case":[],
    "test_cases":[
        {
            "Input":[ 2,[[1,2]]],
            "Output":2
        },
        {
            "Input":[3,[[1,3],[2,3]]],
            "Output":3
        },
        { 
            "Input":[3, [[1,3],[2,3],[3,1]]],
            "Output":-1
        },
        {
            "Input":[ 4,[[1,3],[1,4],[2,3],[2,4],[4,3]]],
            "Output":3
        },
        {
            "Input":[ 3,[[1,2],[2,3]]],
            "Output":-1
        },
    ]
}

sol=Solution()
test= LeetCodeTestingScript(sol)
test.run_tests(sol.findJudge,tests_configs)
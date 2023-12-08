from ast import List
from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums, k) :
        d={}
        for i in nums:
            d[i]=1+d.get(i,0)

        freq=[[] for i in range(len(nums)+1)]
        res=[]
        for key,value in d.items():
            freq[value].append(key)
            
        for i in range(len(freq)-1,0,-1):
            for j in freq[i]:
                res.append(j)
                if len(res)==k:
                    return res
            
a=Solution()
nums =  [1]
k = 1
print(a.topKFrequent(nums,k))
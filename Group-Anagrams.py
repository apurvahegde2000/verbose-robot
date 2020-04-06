'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.

Explanation:
   *here default dict acts like a hashMap
   *sorted(s) sorts the characters in the word without changing the original word
   *tuple(sorted(s)) makes a tuple out of the sorted word
   
   --->s == "eat"
   --->tuple(sorted(s)) == ["a","e","t"]
   
   Now default dict will make a new key and then add the value if the key does not exist but will add a new value to the given key of the 
   dictionary if the key already exits.
   
   the result dictionary will look like:
   result={('a','e','t'):["ate","eat","tea"],('a','n','t'):["nat","tan"],('a','b','t'):["bat"]}
   now result.values()=[["ate","eat","tea"],["nat","tan"],["bat"]]
'''
import collections
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result=collections.defaultdict(list)
        for s in strs:
            result[tuple(sorted(s))].append(s)
        return result.values()    
      
 '''
 Time Complexity: O(NKlogK),, where N is the length of strs, and K is the maximum length of a string in strs. 
 The outer loop has complexity O(N) as we iterate through each string. Then, we sort each string in O(KlogK) time.

Space Complexity: O(NK), the total information content stored in ans.


'''

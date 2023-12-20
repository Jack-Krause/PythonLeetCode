from typing import List
from collections import Counter


class Solution:

    def reverseWords(self, s: str) -> str:
        """151. Reverse Words in a String (Medium)

        Parameters:
        S: String with at least one word

        Returns:
        Returned string should have only a single space separating words.
        No leading or trailing spaces.
        """

        s_list = s.split()
        s_list.reverse()
        ret = ""
        for el in s_list:
            ret += el + " "

        return ret.strip()

    def longestCommonPrefix(self, strs: List[str]) -> str:
        """14. Longest Common Prefix (Easy)

        :param strs:
        an array of strings

        :return:
        A string of the longest common prefix, or an empty string otherwise.
        """

        if not strs:
            return ""

        strs.sort()

        strs_first = strs[0]
        strs_last = strs[-1]
        substrings = ""

        for i in range(len(strs_first)):
            if strs_first[i] == strs_last[i]:
                substrings += strs_first[i]
            else:
                break

        return substrings

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        

solution_inst = Solution()

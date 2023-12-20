from typing import List, Optional
from collections import Counter

from ListNode import ListNode


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
        """21. Merge Two Sorted Lists

        :param list1: head of a sorted linked list
        :param list2: also head node of a sorted linked list
        :return: the head of one sorted list made by splicing together the nodes of the two lists
        """

        ret_list = max(list1, list2)

        return ret_list


solution_inst = Solution()
list_one = ListNode(1, ListNode(2, ListNode(4, None)))
list_two = ListNode(1, ListNode(3, ListNode(4, None)))

temp_list = list_one
temp_list_two = list_two

while temp_list != None:
    print("one ", temp_list.val)
    temp_list = temp_list.next

while temp_list_two != None:
    print("two ", temp_list_two.val)
    temp_list_two = temp_list_two.next
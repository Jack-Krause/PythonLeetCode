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

        # ret_list = ListNode((max(list1.val, list2.val)))
        ret_list = ListNode()
        merged_list = ret_list

        while True:

            if list2 is None:
                merged_list.next = ListNode(list1.val)
                list1 = list1.next
                merged_list = merged_list.next
                break

            if list1 is None:
                merged_list.next = ListNode(list2.val)
                list2 = list2.next
                merged_list = merged_list.next
                break

            if list1.val <= list2.val:
                merged_list.next = ListNode(list1.val)
                list1 = list1.next
            else:
                merged_list.next = ListNode(list2.val)
                list2 = list2.next

            merged_list = merged_list.next

        ret_list = ret_list.next
        while ret_list is not None:
            print("--", ret_list.val, "--")
            ret_list = ret_list.next


solution_inst = Solution()
list_one = ListNode(1, ListNode(2, ListNode(4, None)))
list_two = ListNode(1, ListNode(3, ListNode(4, None)))


solution_inst.mergeTwoLists(list_one, list_two)

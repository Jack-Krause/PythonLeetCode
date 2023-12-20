import unittest
from typing import Optional

from ListNode import ListNode
from Problems import Solution


class Tests151(unittest.TestCase):

    def setUp(self):
        self.test_inst = Solution()

    def test_reverse_words_a(self):
        str_input = "the sky is blue"
        str_exp = "blue is sky the"
        str_out = self.test_inst.reverseWords(str_input)
        self.assertEqual(str_exp, str_out)

    def test_reverse_words_b(self):
        str_input = "  hello world  "
        str_exp = "world hello"
        str_out = self.test_inst.reverseWords(str_input)
        self.assertEqual(str_exp, str_out)

    def test_reverse_words_c(self):
        str_input = "a good   example"
        str_exp = "example good a"
        str_out = self.test_inst.reverseWords(str_input)
        self.assertEqual(str_exp, str_out)


class Tests14(unittest.TestCase):

    def setUp(self):
        self.test_inst = Solution()

    def test_longest_common_prefix_a(self):
        arr_input = ["flower", "flow", "flight"]
        str_exp = "fl"
        str_out = self.test_inst.longestCommonPrefix(arr_input)
        self.assertEqual(str_exp, str_out)

    def test_longest_common_prefix_b(self):
        arr_input = ["dog", "racecar", "car"]
        str_exp = ""
        str_out = self.test_inst.longestCommonPrefix(arr_input)
        self.assertEqual(str_exp, str_out)

    def test_longest_common_prefix_c(self):
        arr_input = ["hello", "there", "hi", "name"]
        str_exp = ""
        str_out = self.test_inst.longestCommonPrefix(arr_input)
        self.assertEqual(str_exp, str_out)

    def test_longest_common_prefix_d(self):
        arr_input = ["aaa", "aa", "aaa"]
        str_exp = "aa"
        str_out = self.test_inst.longestCommonPrefix(arr_input)
        self.assertEqual(str_exp, str_out)


class Tests21(unittest.TestCase):

    def listChecker(self, expected: Optional[ListNode], actual: Optional[ListNode]) -> bool:

        while expected is not None or actual is not None:
            if (expected is None) or (actual is None) or (expected.val != actual.val):
                return False

            actual = actual.next
            expected = expected.next

        return True

    def setUp(self):
        self.testInst = Solution()

    def test_merge_two_lists_a(self):
        list_one = ListNode(1, ListNode(2, ListNode(4)))
        list_two = ListNode(1, ListNode(3, ListNode(4)))
        list_exp = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4))))))
        list_out = self.testInst.mergeTwoLists(list_one, list_two)
        self.assertTrue(self.listChecker(list_exp, list_out))

    def test_merge_two_lists_b(self):
        list_one = ListNode()
        list_two = ListNode()
        list_exp = ListNode()
        list_out = self.testInst.mergeTwoLists(list_one, list_two)
        self.assertTrue(self.listChecker(list_exp, list_out))

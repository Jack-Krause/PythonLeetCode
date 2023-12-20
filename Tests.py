import unittest

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

    def setUp(self):
        self.testInst = Solution()


    def test_merge_two_lists_a(self):
        input_arr_one = [1, 2, 4]
        input_arr_two = [1, 3, 4]
        arr_exp = [1, 1, 2, 3, 4, 4]
        arr_out = self.testInst.mergeTwoLists(input_arr_one, input_arr_two)
        self.assertEqual(arr_exp, arr_out)
import unittest

from Problems import Solution


class Tests(unittest.TestCase):

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



from typing import List


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

        #get all substrings
        substrings = []
        for element in strs:
            temp_arr = [element[i:j] for i in range(len(element)) for j in range(i + 1, len(element) + 1)]
            substrings.append(temp_arr)

        print(substrings[1])



solution_inst = Solution()
temp = ["hello", "there", "hi", "name"]
solution_inst.longestCommonPrefix(temp)

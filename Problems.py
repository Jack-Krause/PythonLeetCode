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

        n = len(strs)
        substrings = [""] * n
        counter = 0

        while len(set(substrings)) == 1:
            for i in range(n):
                if counter < len(strs[i]):
                    substrings[i] += strs[i][counter]
            counter += 1

            if all(substrings[k] == "" for k in range(n)):
                break

        print(substrings)

solution_inst = Solution()
# temp = ["hello", "there", "hi", "name"]
# temp = ["hello", "hello there", "hi", "helloooo"]
temp = ["flower", "flow", "flight"]
solution_inst.longestCommonPrefix(temp)

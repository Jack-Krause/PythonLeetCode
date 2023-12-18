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

        if n == 0:
            return ""

        elif n == 1:
            return strs[0]

        elif all(strs[t] == strs[0] for t in range(len(strs))):
            return strs[0]

        substrings = [""] * n
        counter = 0

        # if len(set(substrings)) is not 0, there are non-duplicates
        while len(set(substrings)) <= 1:
            for i in range(n):
                if counter < len(strs[i]):
                    substrings[i] += strs[i][counter]
            counter += 1

            if all(substrings[k] == "" for k in range(n)):
                break

        if (len(set(substrings))) == 0:
            print("a")
            return list(set(substrings))[0]
        else:
            print("b")
            return min(list(set(substrings)), key=len)[:-1]


solution_inst = Solution()
# temp = ["hello", "there", "hi", "name"]
# temp = ["hello", "hello there", "hi", "helloooo"]
temp = ["flower", "flow", "flight"]
# temp = ["aaa","aa","aaa"]
print(solution_inst.longestCommonPrefix(temp))
# solution_inst.longestCommonPrefix(temp)

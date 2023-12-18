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

        # get all substrings
        n = len(strs)
        prefixes = [""] * n
        counter = 0

        # while there are duplicate prefixes
        while True:
            if len(set(prefixes)) > 1:
                break
            # iterate through strings and add prefix character
            for i in range(n):
                element = strs[i]
                if (counter < len(element)) and element[counter] != " ":
                    prefixes[i] += element[counter]
                if i == n - 1:
                    counter += 1


        print(prefixes)
        ret = {el for el in prefixes if prefixes.count(el) > 1}
        print(ret)


solution_inst = Solution()
# temp = ["hello", "there", "hi", "name"]
# temp = ["hello", "hello there", "hi", "helloooo"]
temp = ["flower", "flow", "flight"]
solution_inst.longestCommonPrefix(temp)

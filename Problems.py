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


solution_inst = Solution()
res = solution_inst.reverseWords("Hello there new user")
print(res)


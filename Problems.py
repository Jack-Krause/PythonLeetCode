class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split()
        s_list.reverse()
        ret = ""
        for el in s_list:
            ret += el + " "

        return ret.strip()


solution_inst = Solution()
res = solution_inst.reverseWords("Hello there new user")
print(res)


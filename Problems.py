class Solution:
    def reverseWords(self, s: str) -> str:
        sList = s.split()
        ret = ""
        for el in reversed(sList):
            ret += el + " "

        return ret.strip()


solution_inst = Solution()
res = solution_inst.reverseWords("Hello there new user")
print(res)


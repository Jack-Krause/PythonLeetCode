from typing import List


def insertion_sort_non_increasing(nums):
    for i in range(len(nums)):
        n = len(nums)

        for i in range(n):
            key = nums[i]
            j = i-1

            while j >= 0 and nums[j] < key:
                nums[j + 1] = nums[j]
                j-=1

            nums[j+1] = key


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

    def maxProduct(self, nums: List[int]) -> int:
        """152. Maximum Product Subarray (Medium)

        :param nums:
        Integer array length [1, 2*10^4]
        elements are integers [-10, 10]
        :return:
        The largest product of subarray elements
        """

        return 0


solution_inst = Solution()
# res = solution_inst.reverseWords("Hello there new user")


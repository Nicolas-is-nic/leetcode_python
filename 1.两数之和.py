class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) <= 1:
            # 若nums的元素不足两个,直接返回None
            return None

        res_dict = {}
        for index, num in enumerate(nums):
            if num in res_dict:
                return [res_dict[num], index]
            else:
                res = target - num
                res_dict[res] = index


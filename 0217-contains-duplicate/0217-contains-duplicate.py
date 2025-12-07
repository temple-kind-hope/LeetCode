class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #リストをセットに変換
        #セットにすると自動的に重複が解除される
        nums_set = set(nums)

        #「元のリストの長さ」と「セットの長さ」がちがうなら重複があった(True)ということ
        return len(nums) != len(nums_set)
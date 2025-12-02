class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # すでに見終わった数字と、そのインデックスを記録する辞書
        # {数字: インデックス} の形
        seen = {}
        
        # enumerateを使うと、インデックス(i)と数値(num)を同時に取れます
        for i, num in enumerate(nums):
            # 相方の数字を計算
            needed = target - num
            
            # 相方がすでに辞書にあるかチェック
            if needed in seen:
                # あれば、そのインデックスと現在のインデックスを返す
                return [seen[needed], i]
            
            # なければ、現在の数字とインデックスを辞書に登録
            seen[num] = i
            
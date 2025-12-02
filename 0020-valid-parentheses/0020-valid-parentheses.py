class Solution:
    def isValid(self, s: str) -> bool:
        # ペアを定義（閉じる括弧をキーにすると検索しやすい）
        pair = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in pair:
                # 閉じる括弧が来たとき
                # スタックが空なら相方がいないので False
                if not stack:
                    return False
                
                # スタックの一番上を取り出して確認
                top_element = stack.pop()
                if top_element != pair[char]:
                    return False
            else:
                # 開く括弧ならスタックに積む
                stack.append(char)
        
        # 最後にスタックが空なら True
        return not stack
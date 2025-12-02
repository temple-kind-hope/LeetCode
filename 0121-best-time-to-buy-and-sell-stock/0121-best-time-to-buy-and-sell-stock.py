class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #1 最小価格の初期値を無限大に設定
        # こうすると、最初の価格が必ず最小価格として登録される
        min_price = float('inf')

        #最大利益の初期値は0
        #利益が出ない場合も返り値は0のため
        max_profit = 0

        for price in prices:
            #もし「今の価格」が「これまでの最安値」より安ければ、最安値を更新
            if price < min_price:
                min_price = price

            #それ以外の場合、「今売ったらいくら儲かるか」を計算
            #「今の価格-最安値」が「これまでの最大利益」を超えていれば更新
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit

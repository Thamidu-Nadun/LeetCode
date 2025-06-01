class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = []

        for i in range(len(prices)):
            rest = prices[i::]
            if len(rest) > 0:
                max_n = max(rest)
                print("N: ", prices[i], " Max: ",max_n)
                diff = max_n-prices[i]
                res.append(diff)
        
        return max(res)
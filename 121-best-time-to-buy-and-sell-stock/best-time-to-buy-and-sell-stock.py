class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit=0
        
        if len(prices)>1:
            buy=prices[0]
            sell=prices[1]

            for x in range(len(prices)-1):
                
                if prices[x]<buy:
                    buy=prices[x]
                    sell=prices[x+1]
                elif prices[x+1]>sell:
                    sell=prices[x+1]


                if sell-buy>profit:
                    profit=sell-buy

        return profit
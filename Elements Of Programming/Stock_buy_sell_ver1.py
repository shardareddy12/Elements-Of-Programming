'''
Stock buy and sell

Input: prices = [7,1,5,3,6,4]
Output: 5

Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
'''
prices = [7,2,5,3,9,10]
def buysell(prices):
    minprice= 9999999
    profit = 0
    for price in prices:
        if price<minprice:
            minprice = price
        elif price-minprice>profit:
            profit = price-minprice

    return profit

print(buysell(prices))
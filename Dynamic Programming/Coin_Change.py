# Source link https://vjudge.net/contest/761092#problem/D
coins = [50,25,10,5,1]
coins.sort()
# 1D数组dp[i]，dp[i]代表着凑目标amount的不同方法数
# 状态转移方程：我们有两种选择，一种是不使用当前coin来凑，一种是使用。如果用coin来凑amount，那么剩下的需要凑的amount就是amount-coin, 而这个的方法总数就是dp[amount-coin]
# 回想dp数组的含义，这个就代表着凑出amount-coin的所有可能方法数量, 因此状态转移方程就是dp[amount]=dp[amount]+dp[amount−coin]，
# 两种情况，方法数量之和是不使用当前coin的方法数量+使用的方法数量
# 初始化数组dp[0] = 1, 因为要换0 cent只有一种方法, 其他全部初始化为0
# 结果dp[n], 凑到n cents的最大方法数，也就是数组的最后一位
import sys
output = []
def res(amount):
    dp = [0] * (amount+1)
    dp[0] = 1
    # 循环嵌套的逻辑, 遍历每一种硬币凑i分(实际是从coin到amount，枚举所有情况，这样子dp[amount]就是结果，之所以
    # coin是下界，因为比coin的amount无法用当前的coin来凑)的方式，累加在dp数组中，结果就是总的方法数量
    # dp[i] ：原本凑i分的方法数（不考虑当前硬币）
    # dp[i - coin] ：如果用这个硬币凑i分，剩下的要凑的就是i-coin, 加起来就是：用或不用当前硬币的总方法数(之前提到的两种选择)
    for coin in coins:
        # i 是每次要凑的amount
        for i in range(coin, amount+1):
            dp[i] = dp[i] + dp[i-coin]
    return dp[amount]

for line in sys.stdin:
    line = line.strip()
    output.append(res(int(line)))
for j in output:
    print(j)


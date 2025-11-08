# 拆分后赋值给a,b
a,b = input().split()
# 判断长度
m,n = len(a),len(b)
# dp数组的定义是dp[i][j]代表数组A的前i个字符和数组B的前j个字符的最长公共子序列长度，因此，二维数组的
# 行数，也就是一共有多少个嵌套的列表的数量应该是m，列数，就是每一个嵌套的列表的长度，也就是n
# 长度为m+1和n+1，因为要1-based indexing，可以防止判断-1的时候越界
dp = [[0]*(n+1) for _ in range(m+1)]
# 从1开始遍历，到m也就是数组末位的索引，防止越界
for i in range(1,m+1):
    for j in range(1,n+1):
        # 判断两个数组的上一项，是否相等，回忆一下dp数组的定义，如果相等，就说明又多了一个公共字串，因此长度+1
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
print(dp[m][n])
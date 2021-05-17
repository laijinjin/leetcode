# 有台奇怪的打印机有以下两个特殊要求： 
# 
#  
#  打印机每次只能打印由 同一个字符 组成的序列。 
#  每次可以在任意起始和结束位置打印新字符，并且会覆盖掉原来已有的字符。 
#  
# 
#  给你一个字符串 s ，你的任务是计算这个打印机打印它需要的最少打印次数。 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "aaabbb"
# 输出：2
# 解释：首先打印 "aaa" 然后打印 "bbb"。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "aba"
# 输出：2
# 解释：首先打印 "aaa" 然后在第二个位置打印 "b" 覆盖掉原来的字符 'a'。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 100 
#  s 由小写英文字母组成 
#  
#  Related Topics 深度优先搜索 动态规划 
#  👍 190 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def strangePrinter(self, s: str) -> int:
        # 区间dp问题，随着操作的进行，判断的区间范围越来越大，因此从小窗口进行判断
        if not s: return 0
        n = len(s)
        # 用dp[i][j]来代表i，j区间内的最小打印次数
        dp = [[0] * n for _ in range(n + 1)]
        # 首先规定打印子区间的长度
        for l in range(n):
            # 确定区间的起点
            for i in range(n - l):
                # 确定区间的终点
                j = i + l
                # 对当前的打印次数进行初始化
                dp[i][j] = dp[i + 1][j] + 1
                # 在区间内部对可能的分割点进行讨论
                for k in range(i + 1, j + 1):
                    # 当分割点与起始点相同时，可以减少打印次数
                    if s[i] == s[k]:
                        dp[i][j] = min(dp[i][j], dp[i][k - 1] + dp[k + 1][j])
        return dp[0][-1]
# leetcode submit region end(Prohibit modification and deletion)

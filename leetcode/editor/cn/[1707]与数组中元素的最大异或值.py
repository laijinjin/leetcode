# 给你一个由非负整数组成的数组 nums 。另有一个查询数组 queries ，其中 queries[i] = [xi, mi] 。 
# 
#  第 i 个查询的答案是 xi 和任何 nums 数组中不超过 mi 的元素按位异或（XOR）得到的最大值。换句话说，答案是 max(nums[j] XOR
#  xi) ，其中所有 j 均满足 nums[j] <= mi 。如果 nums 中的所有元素都大于 mi，最终答案就是 -1 。 
# 
#  返回一个整数数组 answer 作为查询的答案，其中 answer.length == queries.length 且 answer[i] 是第 i 个
# 查询的答案。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]
# 输出：[3,3,7]
# 解释：
# 1) 0 和 1 是仅有的两个不超过 1 的整数。0 XOR 3 = 3 而 1 XOR 3 = 2 。二者中的更大值是 3 。
# 2) 1 XOR 2 = 3.
# 3) 5 XOR 2 = 7.
#  
# 
#  示例 2： 
# 
#  输入：nums = [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]]
# 输出：[15,-1,5]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length, queries.length <= 105 
#  queries[i].length == 2 
#  0 <= nums[j], xi, mi <= 109 
#  
#  Related Topics 位运算 字典树 
#  👍 94 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Trie:
    def __init__(self, left = None, right = None) -> None:
        self.left = left
        self.right = right
    def build(self, ele):
        L = 30
        cur = self
        for i in range(L-1, -1, -1):
            v = (ele >> i) & 1
            if v:
                if not cur.left:
                    cur.left = Trie()
                cur = cur.left
            else:
                if not cur.right:
                    cur.right = Trie()
                cur = cur.right


import bisect
class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        L = 30
        tree_root = Trie()
        queries = [(a, b, i) for i, (a, b) in enumerate(queries)]
        queries.sort(key=lambda x: x[1])
        nums.sort()
        res = [0] * len(queries)
        idx = 0
        for x, m, index in queries:
            while idx < len(nums) and nums[idx] <= m:
                tree_root.build(nums[idx])
                idx += 1

            if idx == 0:
                res[index] = -1
                continue

            total = 0
            cur = tree_root
            for k in range(L - 1, -1, -1):
                v = (x >> k) & 1
                if v:  # 如果该位是1， 往右子树搜
                    if cur.right:
                        cur = cur.right
                        total = 2 * total + 1
                    # 若右子树不存在，搜左子树
                    else:
                        cur = cur.left
                        total = 2 * total
                else:  # 如果该位是0， 往左子树搜
                    if cur.left:
                        cur = cur.left
                        total = 2 * total + 1
                    else:
                        cur = cur.right
                        total = 2 * total
            res[index] = total
        return res

# leetcode submit region end(Prohibit modification and deletion)

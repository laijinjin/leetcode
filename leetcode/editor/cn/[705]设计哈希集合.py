# 不使用任何内建的哈希表库设计一个哈希集合（HashSet）。 
# 
#  实现 MyHashSet 类： 
# 
#  
#  void add(key) 向哈希集合中插入值 key 。 
#  bool contains(key) 返回哈希集合中是否存在这个值 key 。 
#  void remove(key) 将给定值 key 从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。 
#  
#  
# 
#  示例： 
# 
#  
# 输入：
# ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove
# ", "contains"]
# [[], [1], [2], [1], [3], [2], [2], [2], [2]]
# 输出：
# [null, null, null, true, false, null, true, null, false]
# 
# 解释：
# MyHashSet myHashSet = new MyHashSet();
# myHashSet.add(1);      // set = [1]
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(1); // 返回 True
# myHashSet.contains(3); // 返回 False ，（未找到）
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(2); // 返回 True
# myHashSet.remove(2);   // set = [1]
# myHashSet.contains(2); // 返回 False ，（已移除） 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= key <= 106 
#  最多调用 104 次 add、remove 和 contains 。 
#  
# 
#  
# 
#  进阶：你可以不使用内建的哈希集合库解决此问题吗？ 
#  Related Topics 设计 哈希表 
#  👍 106 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tab=SortedList()
        self.tab.

    def add(self, key: int) -> None:
        if key not in self.tab:
                self.tab.append(key)

    def remove(self, key: int) -> None:
        if key in self.tab:
            self.tab.remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return True if key in self.tab else False



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# leetcode submit region end(Prohibit modification and deletion)

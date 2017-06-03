# python小练习（006）：传送门

# 维基百科对字典树的定义如下：
# 在计算机科学中，trie，又称前缀树或字典树，是一种有序树，用于保存关联数组，其中的键通常是字符串。与二叉查找树不同，键不是直接保存在节点中，而是由节点在树中的位置决定。一个节点的所有子孙都有相同的前缀，也就是这个节点对应的字符串，而根节点对应空字符串。一般情况下，不是所有的节点都有对应的值，只有叶子节点和部分内部节点所对应的键才有相关的值。

# 字典树的好处是可以对关键字进行预先处理，生成字典树后，可以在搜索时按照字典树的前缀进行依次搜索大大加快搜索速度。


# 一个保存了8个键的trie结构，"A", "to", "tea", "ted", "ten", "i", "in", and "inn".
# 你能否做成一个简单的字典树呢？（在单词结尾，记得带上结束标记'/'，也可以你自行定义）
# 请打印出你生成的字典树。

# 例如：
# {'A': {'/': None}, 'i': {'/': None, 'n': {'/': None, 'n': {'/': None}}}, 't': {'e': {'a': {'/': None}, 'd': {'/': None}, 'n': {'/': None}}, 'o': {'/': None}}}
# 复制代码

class DictTree:

    def __init__(self):
        self.END = "/"
        self.root = {}

    def getTree(self, word):
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node[self.END] = None

    def findWord(self,word):
        node=self.root
        for c in word:
            if c not in node:
                return False
            node=node[c]
        return self.END in node
           

tree = DictTree()
List = ["A", "to", "tea", "ted", "ten", "i", "in", "inn"]
for i in List:
    tree.getTree(i)
print(tree.root)

print(tree.findWord('ted'))
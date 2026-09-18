class TrieNode:
    def __init__(self):
        self.children={}
        self.terminal=False

class Trie:
    """Prefix index for fast command and capability lookup."""
    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str):
        node=self.root
        for char in word.lower():
            node=node.children.setdefault(char,TrieNode())
        node.terminal=True

    def contains(self, word: str) -> bool:
        node=self.root
        for char in word.lower():
            if char not in node.children:return False
            node=node.children[char]
        return node.terminal

    def starts_with(self,prefix: str) -> list[str]:
        node=self.root
        for char in prefix.lower():
            if char not in node.children:return []
            node=node.children[char]
        out=[]
        def walk(n,path):
            if n.terminal: out.append(path)
            for c,child in n.children.items(): walk(child,path+c)
        walk(node,prefix.lower())
        return out

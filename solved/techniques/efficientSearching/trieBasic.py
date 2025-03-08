class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_leaf = False

root = TrieNode()
    
def insert(s: str):
    now = root
    for ch in s:
        if now.children[ord(ch) - ord('a')] is None:
            now.children[ord(ch) - ord('a')] = TrieNode()
        now = now.children[ord(ch) - ord('a')]
    now.is_leaf = True
    
def search(s: str):
    now = root
    i = 0
    while i < len(s) and now.children[ord(s[i]) - ord('a')] is not None:
        now = now.children[ord(s[i]) - ord('a')]
        i += 1
    return i >= len(s) and now.is_leaf

def hasPrefix(pref: str):
    now = root
    i = 0
    while i < len(pref) and now.children[ord(pref[i]) - ord('a')] is not None:
        now = now.children[ord(pref[i]) - ord('a')]
        i += 1
    return i >= len(pref)


#Topic is Trie Data Structure.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    #Insert word into Trie.
    def insert(self, word):

        node = self.root

        for char in word:

            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.is_end = True
        
    #Searching the exact word.
    def search(self, word):

        node = self.root

        for char in word:

            if char not in node.children:
                return False

            node = node.children[char]

        return node.is_end
    
    #Prefix Word.
    def startsWith(self, prefix):

        node = self.root

        for char in prefix:

            if char not in node.children:
                return False

            node = node.children[char]

        return True


trie = Trie()

trie.insert("apple")
trie.insert("app")
trie.insert("ball")

print(trie.search("apple"))      # True
print(trie.search("app"))        # True
print(trie.search("ap"))         # False

print(trie.startsWith("ap"))     # True
print(trie.startsWith("ba"))     # True
print(trie.startsWith("cat"))    # False
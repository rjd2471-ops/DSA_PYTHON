#Ques Complete String .


words = ["n", "ni", "nin", "ninj", "ninja", "ninga"]

class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end = False


class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):

        node = self.root

        for char in word:

            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.is_end = True

    def check(self, word):

        node = self.root

        for char in word:

            if char not in node.children:
                return False

            node = node.children[char]

            if node.is_end == False:
                return False

        return True


words = ["n", "ni", "nin", "ninj", "ninja", "ninga"]

trie = Trie()

for word in words:
    trie.insert(word)

answer = ""

for word in words:

    if trie.check(word):

        if len(word) > len(answer):
            answer = word

        elif len(word) == len(answer) and word < answer:
            answer = word

if answer == "":
    print("None")
else:
    print(answer)
    
    
"""
Overall:

O(N×L)
	​


Space complexity:

O(N×L)
	​
"""
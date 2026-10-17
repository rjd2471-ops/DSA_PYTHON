#Implement Trie II.

# Topic: Trie Data Structure

class TrieNode:

    def __init__(self):
        self.children = {}
        self.word_count = 0
        self.prefix_count = 0


class Trie:

    def __init__(self):
        self.root = TrieNode()

    # Insert Word
    def insert(self, word):

        node = self.root

        for char in word:

            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]
            node.prefix_count += 1

        node.word_count += 1

    # Search Exact Word
    def search(self, word):

        node = self.root

        for char in word:

            if char not in node.children:
                return False

            node = node.children[char]

        return node.word_count > 0

    # Prefix Search
    def startsWith(self, prefix):

        node = self.root

        for char in prefix:

            if char not in node.children:
                return False

            node = node.children[char]

        return True

    # Count Exact Word
    def countWordsEqualTo(self, word):

        node = self.root

        for char in word:

            if char not in node.children:
                return 0

            node = node.children[char]

        return node.word_count

    # Count Prefix
    def countWordsStartingWith(self, prefix):

        node = self.root

        for char in prefix:

            if char not in node.children:
                return 0

            node = node.children[char]

        return node.prefix_count

    # Erase Word
    def erase(self, word):

        node = self.root

        nodes = []

        for char in word:

            if char not in node.children:
                return

            node = node.children[char]
            nodes.append(node)

        if node.word_count == 0:
            return

        node.word_count -= 1

        for node in nodes:
            node.prefix_count -= 1
            
            
            
trie = Trie()

trie.insert("apple")
trie.insert("apple")
trie.insert("app")
trie.insert("ball")

print(trie.search("apple"))
print(trie.countWordsEqualTo("apple"))
print(trie.countWordsStartingWith("app"))

trie.erase("apple")

print(trie.countWordsEqualTo("apple"))
print(trie.countWordsStartingWith("app"))


"""
Time Complexity
Operation	Complexity
Insert	O(L)
Search	O(L)
startsWith	O(L)
countWordsEqualTo	O(L)
countWordsStartingWith	O(L)
Erase	O(L)

where L is the length of the word.

"""
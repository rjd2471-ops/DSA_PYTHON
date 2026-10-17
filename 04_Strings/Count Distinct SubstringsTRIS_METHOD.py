#Count Distinct Substrings | Brute Force vs Trie Approach.


s = "abab"

distinct = set()

for i in range(len(s)):

    temp = ""

    for j in range(i, len(s)):

        temp += s[j]

        distinct.add(temp)

print(len(distinct) + 1)      # +1 for empty string

"""
Time:-
O(n³)
(Generating + copying substrings.)

Space:-
O(n²)

"""



class TrieNode:

    def __init__(self):
        self.children = {}


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def countDistinct(self, s):

        count = 0

        for i in range(len(s)):

            node = self.root

            for j in range(i, len(s)):

                ch = s[j]

                if ch not in node.children:

                    node.children[ch] = TrieNode()

                    count += 1

                node = node.children[ch]

        return count + 1          # Empty substring


trie = Trie()

print(trie.countDistinct("abab"))

"""
Comparison
Method	                               Time	                  Space
Brute Force (set)	                    O(n³)	               O(n²)
Trie	                                O(n²)	               O(n²)
"""
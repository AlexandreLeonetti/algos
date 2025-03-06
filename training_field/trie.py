class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary of next possible letters
        self.is_end_of_word = False  # Marks if this node is the end of a word

class Trie:
    """
    Basic Trie (Prefix Tree) implementation with debug print statements.
    """
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Insert a word into the Trie.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True  # Mark the last node as the end of a valid word

    def search(self, word):
        """
        Search for a word in the Trie with debug prints.
        Returns True if the word exists, otherwise False.
        """
        node = self.root
        print(f"🔍 Searching for '{word}' in Trie...")

        for char in word:
            print(f"  ➡ Checking character: '{char}'in the for string")
            print(f"     Current node content children: {list(node.children.keys())}")

            if char not in node.children:
                print(f"  ❌ Character '{char}' not found. Word does NOT exist.\n")
                return False  # If the letter is not found, return False
            print(f"going to {node.children[char]} from {char}")
            node = node.children[char]  # Move to the next character in the Trie

        print(f"  🎯 Reached end of word.{list(node.children.keys())} is_end_of_word = {node.is_end_of_word}\n")
        return node.is_end_of_word  # Return True if this is a valid word

    def starts_with(self, prefix):
        """
        Check if there exists any word in the Trie that starts with the given prefix.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

trie = Trie()
trie.insert("cat")
trie.insert("car")
trie.insert("dog")


trie.search("cat")


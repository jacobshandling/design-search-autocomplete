from typing import *

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.nodes = {}
        for i in range(len(sentences)):
            self.insert(sentences[i], times[i])
        self.cur_input = ''

    def insert(self, sentence: str, counts_to_add: int):
        cur = self.nodes
        for c in sentence:
            if c not in cur:
                cur[c] = {'*': 0}  # {'*': number of times this sentence has been entered (0 if never)
            cur = cur[c]
        cur['*'] += counts_to_add
        cur = self.nodes

    def input(self, c: str) -> List[str]:
        if c == '#':
            self.insert(''.join(self.cur_input), 1)
            self.reset_input()
            return []
        else:
            self.cur_input += c
            return self.get_hot_history()

    def reset_input(self):
        self.cur_input = ''

    def get_hot_history(self, num_results: int = 3):
        # get all words containing self.cur_input as a prefix
        matches = self.get_prefix_words_and_counts(self.cur_input)
        # sort these results based on their count (fallback to ASCII), and return the first num_results of them
        matches.sort(key=lambda match_tup: (-match_tup[1], match_tup[0]))

        # return matches[:num_results]
        return [match[0] for match in matches[:num_results]]
    
    def get_prefix_words_and_counts(self, prefix: str) -> List[Tuple[str, int]]:
        cur = self.nodes 
        for c in prefix:
            if c not in cur:
                return []  # prefix not in trie
            cur = cur[c]
        # cur now pointing to common parent
        matches = self.get_suffixes_and_counts(prefix, cur)
        return matches
    
    def get_suffixes_and_counts(self, prefix: str, cur: dict):
        matches = []
        if cur['*']:
            matches.append((prefix, cur['*']))  # the prefix itself is a previously entered word, include it in matches with its count
        for c in cur:
            if c != '*':
                matches.extend(self.get_suffixes_and_counts(prefix + c, cur[c]))
        return matches




# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)

if __name__ == '__main__':
    ac = AutocompleteSystem(["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2])
    print(ac.input('i'))
    print(ac.input(' '))
    print(ac.input('a'))
    print(ac.input('#'))
    print(ac.input('i'))
    print(ac.input(' '))
    print(ac.input('a'))
    print(ac.input('#'))
    print(ac.input('i'))
    print(ac.input(' '))
    print(ac.input('a'))
    print(ac.input('#'))

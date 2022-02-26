# design-search-autocomplete

`autocomplete.py` contains my solution to the [Leetcode problem, "Design Search Autocomplete System"](https://leetcode.com/problems/design-search-autocomplete-system/)

# The problem:

Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character '#').

You are given a string array sentences and an integer array times both of length n where sentences[i] is a previously typed sentence and times[i] is the corresponding number of times the sentence was typed. For each input character except '#', return the top 3 historical hot sentences that have the same prefix as the part of the sentence already typed.

Here are the specific rules:

- The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
- The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have the same hot degree, use ASCII-code order (smaller one appears first).
- If less than 3 hot sentences exist, return as many as you can.
- When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.

Implement the AutocompleteSystem class:
- `AutocompleteSystem(sentences, times)` Initializes the object with the sentences and times arrays.
- `input(c)` indicates that the user typed the character `c`.
  - Returns an empty array `[]` if `c == '#'` and stores the inputted sentence in the system.
  - Returns the top 3 historical hot sentences that have the same prefix as the part of the sentence already typed. If there are fewer than 3 matches, return them all.

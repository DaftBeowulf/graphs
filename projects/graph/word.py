'''
Given two words (begin_word and end_word), and a dictionary's word list,
return the shortest transformation sequence from begin_word to end_word, such that:
Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Each transformed word must be the same length
Note that begin_word is not a transformed word.
​
Note:
Return None if there is no such transformation sequence.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume begin_word and end_word are non-empty and are not the same.
'''
from util import Stack, Queue  # These may come in handy
​
'''
Sample:
begin_word = "hit"
end_word = "cog"
return: ['hit', 'hot', 'cot', 'cog']
begin_word = "sail"
end_word = "boat"
['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']
beginWord = "hungry"
endWord = "happy"
None
'''
​
# 2. Build our graph
​
​
# words are nodes, one-letter-apart is edges
# Do a BFS from start word to end word
# Load word list
# ! grab word file in linux built-ins or this won't work
f = open('words.txt', 'r')
words = f.read().split("\n")
f.close()
​
​
word_set = set()
for word in words:
    word_set.add(word.lower())
​
​
​
​


def get_neighbors(word):
    '''
    return all words from word_list that are 1 letter different
    '''
    # change one letter to another letter in the alphabet incrementally
    # search the graph for that
    # then repeat for each letter in the word
    neighbors = []
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # For each letter in the word,
    for i in range(len(word)):
        # For each letter in the alphabet
        for letter in alphabet:
            # Change the word letter to the alphabet letter
            list_word = list(word)
            list_word[i] = letter
            w = "".join(list_word)
            # If the new word is in the word_set:
            if w != word and w in word_set:
                # Add it to neighbors
                neighbors.append(w)
    return neighbors


​
​
​
​


def find_ladders(begin_word, end_word):
    # DO BFS
    # Create a queue
    q = Queue()
    # Enqueue a path to the starting word
    q.enqueue([begin_word])
    # Create a visited set
    visited = set()
    # While the queue is not empty:
    while q.size() > 0:
        # Dequeue the next path
        path = q.dequeue()
        # Grab the last word from the path
        v = path[-1]
        # If it's not been visited
        if v not in visited:
            # Check if the word is our end word, if so return path
            if v == end_word:
                return path
            # Mark it as visited
            visited.add(v)
            # Enqueue a path to each neighbor
            for neighbor in get_neighbors(v):
                path_copy = path.copy()
                path_copy.append(neighbor)
                q.enqueue(path_copy)


​
​
print(find_ladders("happy", "hungry"))

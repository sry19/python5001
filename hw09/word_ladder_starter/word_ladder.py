from queue import Queue
from stack import Stack

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


class WordLadder:
    """A class providing functionality to create word ladders"""
    def __init__(self, w1, w2, wordlist):
        '''Construct a WordLadder'''
        self.start_word = w1
        self.end_word = w2
        self.word_set = wordlist

    def make_ladder(self):
        '''Find the shortest path from start word to end word
            None -> stack object'''
        if len(self.start_word) != len(self.end_word):
            return None
        if self.start_word not in self.word_set:
            return None
        if self.end_word not in self.word_set:
            return None
        path_queue = Queue()
        path_stack = Stack()
        path_stack.push(self.start_word)
        path_queue.enqueue(path_stack)
        visited = set()
        visited.add(self.start_word)
        while not path_queue.isEmpty():
            curr_stack = path_queue.dequeue()
            curr_word = curr_stack.peek()
            for idx in range(len(curr_word)):
                for alpha in ALPHABET:
                    new_word = curr_word[:idx] + alpha + curr_word[idx + 1:]
                    if (new_word in self.word_set) and (
                                new_word not in visited):
                        visited.add(new_word)
                        new_stack = curr_stack.copy()
                        new_stack.push(new_word)
                        if new_word == self.end_word:
                            return new_stack
                        else:
                            path_queue.enqueue(new_stack)
        return None

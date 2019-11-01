from queue import Queue
from stack import Stack

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


class WordLadder:
    """A class providing functionality to create word ladders"""
    def __init__(self, w1, w2, wordlist):
        self.start_word = w1
        self.end_word = w2
        self.word_set = wordlist
        self.visited = set()
        self.visited.add(self.start_word)

    def make_ladder(self):
        '''Find the shortest path from start word to end word
            None -> stack object'''
        if self.start_word not in self.word_set[len(self.start_word)]:
            return None
        if self.end_word not in self.word_set[len(self.end_word)]:
            return None
        self.path_queue = Queue()
        self.path_stack = Stack()
        self.path_stack.push(self.start_word)
        self.path_queue.enqueue(self.path_stack)
        while not self.path_queue.isEmpty():
            curr_stack = self.path_queue.dequeue()
            curr_word = curr_stack.peek()
            for idx in range(len(curr_word)):
                new_word = curr_word[:idx] + curr_word[idx + 1:]
                res = self.deal_new_word(new_word, curr_word, curr_stack)
                if res:
                    return res
            for idx in range(len(curr_word)):
                for alpha in ALPHABET:
                    new_word = curr_word[:idx] + alpha + curr_word[idx + 1:]
                    res = self.deal_new_word(new_word, curr_word,
                                             curr_stack)
                    if res:
                        return res
            for idx in range(len(curr_word)+1):
                for alpha in ALPHABET:
                    new_word = curr_word[:idx] + alpha + curr_word[idx:]
                    res = self.deal_new_word(new_word, curr_word,
                                             curr_stack)
                    if res:
                        return res
        return None

    def deal_new_word(self, new_word, curr_word, curr_stack):
        '''Judge if this new word can be added to a path'''
        if len(new_word) < 1:
            return None
        if (new_word in self.word_set[len(new_word)]) and (
                                    new_word not in self.visited):
            self.visited.add(new_word)
            new_stack = curr_stack.copy()
            new_stack.push(new_word)
            if new_word == self.end_word:
                return new_stack
            else:
                self.path_queue.enqueue(new_stack)
        return None

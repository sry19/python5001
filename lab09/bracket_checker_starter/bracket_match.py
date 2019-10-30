from stack import Stack


class BracketMatch:
    """Class for evaluating parenthetical strings"""
    def __init__(self):
        '''Construct matched brackets patterns'''
        self.match_dict = {'(': ')', '[': ']', '{': '}'}

    def brackets_match(self, line):
        '''Check if the brackets in the string are matched'''
        ch_stack = Stack()
        for ch in line:
            if ch in self.match_dict.keys():
                ch_stack.push(ch)
            elif ch in self.match_dict.values():
                if not ch_stack.peek():
                    return False
                cloce_ch = ch_stack.pop()
                if self.match_dict[cloce_ch] != ch:
                    return False
        return ch_stack.peek() is None

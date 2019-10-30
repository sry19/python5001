from stack import Stack


class StringProcessor:
    """Class for processing strings"""
    def process_string(self, line):
        '''return a string that has been decoded
            string -> string'''
        CARET = '^'
        ASTERISK = '*'
        CARET_TIMES = 2
        ASTERISK_TIMES = 1

        ch_stack = Stack()
        ans = ''
        for ch in line:
            if ch == ASTERISK:
                for _ in range(ASTERISK_TIMES):
                    if ch_stack.peek():
                        ans += ch_stack.pop()
            elif ch == CARET:
                for _ in range(CARET_TIMES):
                    if ch_stack.peek():
                        ans += ch_stack.pop()
            else:
                ch_stack.push(ch)
        return ans

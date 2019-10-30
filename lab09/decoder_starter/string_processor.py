from stack import Stack


class StringProcessor:
    """Class for processing strings"""
    def process_string(self, line):
        CARET = '^'
        ASTERISK = '*'

        ch_stack = Stack()
        ans = ''
        for ch in line:
            if ch == ASTERISK:
                if ch_stack.peek():
                    ans += ch_stack.pop()
            elif ch == CARET:
                if ch_stack.peek():
                    ans += ch_stack.pop()
                if ch_stack.peek():
                    ans += ch_stack.pop()
            else:
                ch_stack.push(ch)
        return ans

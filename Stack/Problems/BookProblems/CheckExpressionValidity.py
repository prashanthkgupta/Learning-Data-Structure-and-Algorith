def is_exp_valid(exp=''):
    mappings = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for symbol in exp:
        if symbol in mappings:
            stack.append(symbol)
        elif symbol in mappings.values():
            if len(stack) == 0 or mappings[stack.pop()] != symbol:
                return False
    return len(stack) == 0




if __name__ == '__main__':
    exp = input()
    print(is_exp_valid(exp))

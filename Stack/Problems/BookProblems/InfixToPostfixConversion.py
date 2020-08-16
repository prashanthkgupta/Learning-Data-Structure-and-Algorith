mappings = {')': '(', '}': '{', ']': '['}
opr_priority = {'*': 2, '/': 2, '+': 1, '-': 1}
stack = []


def pop_all_opr_until_closing_braces(closing_braces, postfix_exp=""):
    while stack[-1] != mappings[closing_braces]:
        postfix_exp += stack.pop()
    stack.pop()
    return postfix_exp


def pop_all_opr_until_gte_priority(operator, postfix_exp=""):
    while len(stack) > 0 and stack[-1] in opr_priority and opr_priority[stack[-1]] >= opr_priority[operator]:
        postfix_exp += stack.pop()
    stack.append(operator)
    return postfix_exp


def pop_remaining_opr(postfix_exp=''):
    while len(stack) > 0:
        postfix_exp += stack.pop()
    return postfix_exp


def infix_to_postfix(exp=''):
    postfix_exp = ''
    global stack
    stack = []

    for symbol in exp:
        if symbol in mappings.values():
            stack.append(symbol)
        elif symbol in mappings:
            postfix_exp += pop_all_opr_until_closing_braces(symbol)
        elif symbol in opr_priority:
            postfix_exp += pop_all_opr_until_gte_priority(symbol)
        else:
            postfix_exp += symbol
    postfix_exp += pop_remaining_opr()
    return postfix_exp


if __name__ == '__main__':
    exp = input()
    print(infix_to_postfix(exp))

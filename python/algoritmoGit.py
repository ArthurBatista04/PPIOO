# LICENSE: MIT

import collections


RIGHT, LEFT = range(2)

Op = collections.namedtuple('Op', [
    'precedence',
    'associativity'])

OPS = {
    '^': Op(precedence=4, associativity=RIGHT),
    '*': Op(precedence=3, associativity=LEFT),
    '/': Op(precedence=3, associativity=LEFT),
    '+': Op(precedence=2, associativity=LEFT),
    '-': Op(precedence=2, associativity=LEFT)}


def has_precedence(a, b):
    return ((OPS[b].associativity == RIGHT and
             OPS[a].precedence > OPS[b].precedence) or
            (OPS[b].associativity == LEFT and
             OPS[a].precedence >= OPS[b].precedence))


def _pop_greater_than(ops, op):
    out = []

    while True:
        if not ops:
            break

        if ops[-1] not in OPS:
            break

        if not has_precedence(ops[-1], op):
            break

        out.append(ops.pop())

    return out


def _pop_until_group_start(ops):
    out = []

    while True:
        op = ops.pop()

        if op == '(':
            break

        out.append(op)

    return out


def rpn(expression):
    """
    An implementation of the Shunting-yard algorithm\
    for producing Reverse Polish notation out of\
    an expression specified in infix notation
    """
    output = []
    operators = []

    for char in expression:
        if char == '(':
            operators.append(char)
            continue

        if char == ')':
            output.extend(_pop_until_group_start(operators))
            continue

        if char in OPS:
            output.extend(_pop_greater_than(operators, char))
            operators.append(char)
            continue

        if char.isdigit():
            output.append(char)

    output.extend(reversed(operators))

    return ''.join(output)
expression = input()
while expression:
    paser = rpn(expression)
    paser = str(paser) + "\n"
    print(paser)
    expression = input()  
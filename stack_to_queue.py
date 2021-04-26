"""
Stack to queue converter.
"""

from arraystack import ArrayStack   # or from linkedstack import LinkedStack
from arrayqueue import ArrayQueue   # or from linkedqueue import LinkedQueue


def stack_to_queue(stack):
    """
    Return queue from stack (front of queue is peek of stack).
    """
    copy_stack = ArrayStack()
    queue = ArrayQueue()
    for element in stack:
        copy_stack.push(element)

    while len(copy_stack) != 0:
        queue.add(copy_stack.pop())

    return queue




if __name__ == "__main__":
    pass

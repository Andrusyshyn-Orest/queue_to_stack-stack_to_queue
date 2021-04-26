"""
Queue to stack converter.
"""

from arrayqueue import ArrayQueue    # or from linkedqueue import LinkedQueue
from arraystack import ArrayStack    # or from linkedstack import LinkedStack



def reverse_queue(queue: ArrayQueue) -> ArrayQueue:
    """
    Return reversed queue. (Destructive! Clear queue).
    """

    if len(queue) <= 1:
        return queue

    element = queue.pop()
    reversed_queue = reverse_queue(queue)
    reversed_queue.add(element)

    return reversed_queue

def queue_to_stack(queue: ArrayQueue) -> ArrayStack:
    """
    Return stack from queue (front of queue is peek of stack).
    """

    copy_queue = ArrayQueue()
    stack = ArrayStack()
    for element in queue:
        copy_queue.add(element)

    reversed_queue = reverse_queue(copy_queue)
    for element in reversed_queue:
        stack.push(element)

    return stack



if __name__ == "__main__":
    pass

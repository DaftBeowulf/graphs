# will be searching for the longest valid path -- calls for DFS using a stack
class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


def earliest_ancestor(ancestors, starting_node):
    # create function to return parents (neighbors) of children
    def get_parents(child):
        return [pair[0] for pair in ancestors if pair[1] == child]
    # graph will be DIRECTIONAL -- we only want to consider ancestors, so
    # we will only search upwards through the parental heritage, never searching downward
    return get_parents(10)


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 1))

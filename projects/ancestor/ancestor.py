class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


def get_parents(ancestors, node):
    parents = []
    for group in ancestors:
        if group[1] == node:
            parents.append(group[0])
    return parents


def earliest_ancestor(ancestors, node, visited=None, paths=None):
    if visited == None:
        visited = set()
    if paths == None:
        paths = []

    if len(get_parents(ancestors, node)) == 0:
        return -1

    q = Queue()
    q.enqueue([node])

    while q.size() > 0:
        path = q.dequeue()
        last_node = path[-1]

        if len(get_parents(ancestors, last_node)) == 0:
            paths.append(path)

        for parent in get_parents(ancestors, last_node):
            path_copy = path.copy()
            path_copy.append(parent)
            q.enqueue(path_copy)

    longest_path = paths[0]
    for path in paths:
        if len(path) > len(longest_path):
            longest_path = path
        elif len(path) == len(longest_path) and path[-1] < longest_path[-1]:
            longest_path = path
    earliest_node = longest_path[-1]
    return earliest_node

    # # Initialize first_node to be starting_node
    # if starting_node == None:
    #     starting_node = node

    # # For each item in ancestors, check if node has any parents
    # if len(get_parents(ancestors, node)) == 0:
    #     # If there are no parents, and node is starting_node, return -1
    #     if node == starting_node:
    #         return -1
    #     # Else return starting_node, as this is the earliest ancestor
    #     else:
    #         return node
    # # For each parent of starting node, recurse earliest_ancestor function
    # else:
    #     for p in get_parents(ancestors, node):
    #         return earliest_ancestor(ancestors, p, starting_node)

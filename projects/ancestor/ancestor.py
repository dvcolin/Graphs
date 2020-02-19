
def get_parents(ancestors, node):
    parents = []
    for group in ancestors:
        if group[1] == node:
            parents.append(group[0])
    return parents


def earliest_ancestor(ancestors, node, starting_node=None):
    # Initialize first_node to be starting_node
    if starting_node == None:
        starting_node = node

    # For each item in ancestors, check if node has any parents
    if len(get_parents(ancestors, node)) == 0:
        # If there are no parents, and node is starting_node, return -1
        if node == starting_node:
            return -1
        # Else return starting_node, as this is the earliest ancestor
        else:
            return node
    # For each parent of starting node, recurse earliest_ancestor function
    else:
        for p in get_parents(ancestors, node):
            return earliest_ancestor(ancestors, p, starting_node)

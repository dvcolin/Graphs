
def get_parents(ancestors, starting_node):
    parents = []
    for group in ancestors:
        if group[1] == starting_node:
            parents.append(group[0])
    return parents


def earliest_ancestor(ancestors, starting_node, first_node=None):
    # Initialize first_node to be starting_node and visited to be a set
    if first_node == None:
        first_node = starting_node

    # For each item in ancestors, check if starting_node has any parents
    if len(get_parents(ancestors, starting_node)) == 0:
        # If there are no parents, and starting_node is first_node, return -1
        if starting_node == first_node:
            return -1
        # Else return starting_node, as this is earliest ancestor
        else:
            return starting_node
    # For each parent of starting node, recurse earliest_ancestor function
    else:
        for p in get_parents(ancestors, starting_node):
            return earliest_ancestor(ancestors, p, first_node)

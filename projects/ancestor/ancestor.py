import sys

sys.path.append("../graph")

from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    """
    Part 1:
    Go through provided ancestors and build a graph
    Add vertices
    Add edges
    ---
    Part 2:
    Return -1 if starting_node has no parent nodes
    else
    go through starting_node's ancestry until the earliest ancestor
    is reached
    Return that node
    """
    graph = Graph()

    for (parent, child) in ancestors:
        # Add vertices
        if not graph.vertex_exists(parent):
            graph.add_vertex(parent)
        if not graph.vertex_exists(child):
            graph.add_vertex(child)

        # Add edges (flipped)
        graph.add_edge(child, parent)

    # Initial ancestors of starting node
    node_ancestors = graph.get_neighbors(starting_node)

    if len(node_ancestors) == 0:
        # -1 if node has no parents
        return -1

    # Setup
    current_node = starting_node

    # As long as we have ancestors
    while len(graph.get_neighbors(current_node)) > 0:
        node_ancestors = graph.get_neighbors(current_node)
        # Get the ancestor with the smaller ID value
        ancestor = min(node_ancestors)
        # Move current_node pointer to selected ancestor
        current_node = ancestor

    # Return earliest connected ancestor from starting_node
    return current_node


# DEBUG
# test_ancestors = [
#     (1, 3),
#     (2, 3),
#     (3, 6),
#     (5, 6),
#     (5, 7),
#     (4, 5),
#     (4, 8),
#     (8, 9),
#     (11, 8),
#     (10, 1),
# ]

# print(earliest_ancestor(test_ancestors, 1))
# print(earliest_ancestor(test_ancestors, 2))
# print(earliest_ancestor(test_ancestors, 3))
# print(earliest_ancestor(test_ancestors, 4))
# print(earliest_ancestor(test_ancestors, 5))
# print(earliest_ancestor(test_ancestors, 6))
# print(earliest_ancestor(test_ancestors, 7))
# print(earliest_ancestor(test_ancestors, 8))
# print(earliest_ancestor(test_ancestors, 9))
# print(earliest_ancestor(test_ancestors, 10))
# print(earliest_ancestor(test_ancestors, 11))
